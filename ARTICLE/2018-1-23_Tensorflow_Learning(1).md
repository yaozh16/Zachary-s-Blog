# 2018/1/24 Tensorflow学习(1)
##  Tutorial 1
### 1. dataset
<class 'tensorflow.contrib.learn.python.learn.datasets.base.Datasets'>
### 2. 使用placeholder为输入输出做占位，之后的标准输入输出都直接以字典形式传入
```python
x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])
```
### 3. 创建中间参数的形式，以及输出的形式
对于一层的网络
```python
W = tf.Variable(tf.zeros([784, 10]))        # 784 x  10
b = tf.Variable(tf.zeros([10]))             # 1   x  10
y = tf.nn.softmax(tf.matmul(x, W) + b)
```
### 4. 构造信息熵，之后就是使得这个数最小化
```python
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
```
上面的reduction_indices[1]表示为一次方
### 5. 确定迭代方法
```python
train_step = tf.train.GradientDescentOptimizer(1.0).minimize(cross_entropy)
```
### 6. 初始化参数
```python
init = tf.global_variables_initializer()
```
### 7. 开始运行、导入输入输出
```python
sess = tf.Session()
sess.run(init)
```
迭代导入输入输出
```python
for i in range(1000):
    # aquire new data from the dataset
    batch_xs, batch_ys = mnist.train.next_batch(100)
    # run a round：
    # use feed_dict to replace placeholder
    # use train_step to dicide param modification
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
```
