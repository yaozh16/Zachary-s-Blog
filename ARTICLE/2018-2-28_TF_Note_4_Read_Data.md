# TF Read Data
## 主要方法
1. Feeding：代码送入 ```Python code provides the data when running each step.```
2. Reading from files：管道送入 ```an input pipeline reads the data from files at the beginning of a TensorFlow graph.```
3. Preloaded data: ```a constant or variable in the TensorFlow graph holds all the data (for small data sets).```
## Feeding
>Supply feed data through the feed_dict argument to a run() or eval() call that initiates computation.

```python
with tf.Session():
  input = tf.placeholder(tf.float32)
  classifier = ...
  print(classifier.eval(feed_dict={input: my_python_preprocessing_fn()}))
```

An example using placeholder and feeding to train on MNIST data can be found in [tensorflow/examples/tutorials/mnist/fully_connected_feed.py](https://raw.githubusercontent.com/tensorflow/tensorflow/r0.12/tensorflow/examples/tutorials/mnist/fully_connected_feed.py), and is described in the MNIST tutorial
## Reading from files
* The list of filenames
* Optional filename shuffling
* Optional epoch limit
* Filename queue
* A Reader for the file format
* A decoder for a record read by the reader
* Optional preprocessing
* Example queue
### Filenames, shuffling, and epoch limits
#### the list of filenames
1. a constant string Tensor (like ["file0", "file1"] or [("file%d" % i) for i in range(2)])
2. the ```tf.train.match_filenames_once``` function
### File formats
choose decoder to transform the data into tensors
#### CSV(comma-separated value) files
for examle:
```python
# read data
filename_queue = tf.train.string_input_producer(["file0.csv", "file1.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
record_defaults = [[1], [1], [1], [1], [1]]
col1, col2, col3, col4, col5 = tf.decode_csv(
    value, record_defaults=record_defaults)
features = tf.pack([col1, col2, col3, col4])

with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)# 需要先执行这一步才能防止阻塞

  for i in range(1200):
    # Retrieve a single instance:
    example, label = sess.run([features, col5])

  coord.request_stop()
  coord.join(threads)

```
#### Fixed length records
>To read binary files in which each record is a fixed number of bytes, use ```tf.FixedLengthRecordReader``` with the ```tf.decode_raw``` operation. The decode_raw op converts from a string to a uint8 tensor.

the CIFAR-10 dataset uses a file format where each record is represented using a fixed number of bytes: 1 byte for the label followed by 3072 bytes of image data.Once you have a uint8 tensor, standard operations can slice out each piece and reformat as needed. For CIFAR-10, you can see how to do the reading and decoding in [tensorflow/models/image/cifar10/cifar10_input.py](https://raw.githubusercontent.com/tensorflow/tensorflow/r0.12/tensorflow/models/image/cifar10/cifar10_input.py) and described in [this tutorial](https://www.tensorflow.org/versions/r0.12/tutorials/deep_cnn/index.html#prepare-the-data).
#### Standard TensorFlow format
>Another approach is to convert whatever data you have into a supported format. This approach makes it easier to mix and match data sets and network architectures. The recommended format for TensorFlow is a ```TFRecords``` file containing ```tf.train.Example``` protocol buffers (which contain ```Features``` as a field). You write a little program that gets your data, stuffs it in an Example protocol buffer, serializes the protocol buffer to a string, and then writes the string to a TFRecords file using the tf.python_io.TFRecordWriter class. For example, [tensorflow/examples/how_tos/reading_data/convert_to_records.py](https://raw.githubusercontent.com/tensorflow/tensorflow/r0.12/tensorflow/examples/how_tos/reading_data/convert_to_records.py) converts MNIST data to this format.
### Preprocessing
*  This would be any processing that **doesn't** depend on trainable parameters

example at [tensorflow/models/image/cifar10/cifar10_input.py](https://www.tensorflow.org/code/tensorflow/models/image/cifar10/cifar10_input.py)
### Batching
At the end of the pipeline we use another queue to batch together examples for training, evaluation, or inference. For this we use a queue that randomizes the order of examples, using the ```tf.train.shuffle_batch``` function.
| variable          | function                                                                                                                         |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| min_after_dequeue | defines how big a buffer we will randomly sample from -- bigger means better shuffling but slower start up and more memory used. |
| capacity          | must be larger than ```min_after_dequeue``` and the amount larger  determines the maximum we will prefetch.                      |

Recommendation: 
\[
capacity=min_{}After_{}Dequeue + (num_{}Threads + a Small Safety Margin) * batch_{}Size
\]
```python
def read_my_file_format(filename_queue):
  reader = tf.SomeReader()
  key, record_string = reader.read(filename_queue)
  example, label = tf.some_decoder(record_string)
  processed_example = some_processing(example)
  return processed_example, label

def input_pipeline(filenames, batch_size, num_epochs=None):
  filename_queue = tf.train.string_input_producer(
      filenames, num_epochs=num_epochs, shuffle=True)
  example, label = read_my_file_format(filename_queue)
  min_after_dequeue = 10000
  capacity = min_after_dequeue + 3 * batch_size
  example_batch, label_batch = tf.train.shuffle_batch(
      [example, label], batch_size=batch_size, capacity=capacity,
      min_after_dequeue=min_after_dequeue)
  return example_batch, label_batch
```
>if you need more parallelism or shuffling of examples between files, use multiple reader instances using the ```tf.train.shuffle_batch_join``` function

```python
def input_pipeline(filenames, batch_size, read_threads, num_epochs=None):
  filename_queue = tf.train.string_input_producer(
      filenames, num_epochs=num_epochs, shuffle=True)
  example_list = [read_my_file_format(filename_queue)
                  for _ in range(read_threads)]
  min_after_dequeue = 10000
  capacity = min_after_dequeue + 3 * batch_size
  example_batch, label_batch = tf.train.shuffle_batch_join(
      example_list, batch_size=batch_size, capacity=capacity,
      min_after_dequeue=min_after_dequeue)
  return example_batch, label_batch
```
###Creating threads to prefetch using QueueRunner objects
启动读取，否则永远阻塞等待数据
>call ```tf.train.start_queue_runners``` before running any training or inference steps, or it will hang forever. This will start threads that run the input pipeline, filling the example queue so that the dequeue to get the examples will succeed. This is best combined with a ```tf.train.Coordinator``` to cleanly shut down these threads when there are errors. If you set a limit on the number of epochs, that will use an epoch counter that will need to be initialized. 

Example:
```python
# Create the graph, etc.
init_op = tf.global_variables_initializer()

# Create a session for running operations in the Graph.
sess = tf.Session()

# Initialize the variables (like the epoch counter).
sess.run(init_op)

# Start input enqueue threads.
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

try:
    while not coord.should_stop():
        # Run training steps or whatever
        sess.run(train_op)

except tf.errors.OutOfRangeError:
    print('Done training -- epoch limit reached')
finally:
    # When done, ask the threads to stop.
    coord.request_stop()

# Wait for threads to finish.
coord.join(threads)
sess.close()
```
![](assets/AnimatedFileQueues.gif)