# Tensorflow学习（1）
* tensors
* operations
* graphs
* sessions
## 概念解释
* A scalar : 0-d array (a 0th-order tensor). 

For example, 
```
"Howdy" or 5
```
* A vector : 1-d array (a 1st-order tensor). 

For example, 
```
[2, 3, 5, 7, 11] or [5]
```
* A matrix : 2-d array (a 2nd-order tensor). 

For example, 
```
[[3.1, 8.2, 5.9][4.3, -2.7, 6.5]]
```
* dataflow graph:
A graph's nodes are operations; a graph's edges are tensors

* Tensors can be stored in the graph as
 1. constants 
 2. variables
```
x = tf.constant(5.2)
y = tf.Variable([5])
#或者先设置，后修改
y = tf.Variable([0])
y = y.assign([5])
或者
ass=tf.assign(y,[5])
sses.run(ass)
```
* session: Graphs must run within a TensorFlow **session**, which holds the state for the graph(s) it runs:
```python
with tf.Session() as sess:
  initialization = tf.global_variables_initializer()
  print y.eval()
```