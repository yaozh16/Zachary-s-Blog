# 2018/1/24 Tensorflow Learning(2) Note of Lecture
## Lecture 1
### tensor and session
创建Graph(默认有一个defaultGraph)
```
g=tf.get_default_graph() # 获取默认图句柄
```
然后在session中计算graph
```
tf.Session().run(node)
```
### multi CPU/GPU
```
with tf.device("/gpu:2"):
  op=.......
tf.Session().run(op)

```
### 创建新的Graph
需要设置为default_graph才可以加入节点
```
g=tf.Graph()
with g.as_default():
  operations...
```
使用时则指定graph
```
sess=tf.Session(graph=g)
```
## Lecture 2
### tensorboard
在sess的graph写到./graph文件夹中
```
with tf.Session() as sess:
  tf.summary.FileWriter('./graph',sess.graph)
```
terminal运行tensorboard
```
tensorboard --logdir="./graph" --pt 6006
```
然后在上面相对应的端口中(http://localhost:6006/ 去查看)
### tf.constant
```
tf.constant(value,dtype=None,shape=None,name="Const",verify_shape=False)
```
其中
* value可以是n维矩阵
1
[2,2]
[[1,2][2,3]]
[[[1,2][2,3]][[1,2][2,3]]]
* shape为
[1,2,...]向量：对应于value为矩阵（包括[p]这种1x1的）
()空：对应于value为常数
* verify_shape：
默认为False:当value和shape不对应的时候，将value转化为shape并少位填充末尾数字
设置为True:强制value和shape对应
**当维度不同的node运算时会取小维度的node作高维度的复制直到和大维度node相同再运算**
例如<br>
[ [1,2],[3,4] ]+[1,2]=[ [1,2],[3,4] ]+[ [1,2],[1,2] ]=[ [2,4],[4,6] ] <br>
[ [1,2],[3,4] ]x[1,2]=[ [1,2],[3,4] ]x[ [1,2],[1,2] ]=[ [1,4],[3,8] ]
* others：
1. tf.zeros(shape,dtype,name)
2. tf.zeros_like(tensor_with_shape,name)
3. tf.ones(shape,dtype,name)
4. tf.ones_like(tensor_with_shape,name)
5. tf.fill(shape,value,name)
## Lecture 3
### structure type
* tf.Variable
* tf.constant
* tf.placeholder<br>have to be feed in data by **feed_dict**

**Attension:** Avoid lazy loading
### ***model building***
| Step                              | Usage                                |
|:----------------------------------|:-------------------------------------|
| decide placeholder                | for data input                       |
| decide variable                   | for learning                         |
| decide loss function              | with graph node relationship         |
| decide optimizer                  | it will modify variables when runned |
| create session and init variables |                                      |
| **loop**                          |                                      |

**loop中的步骤：**
1. 读取数据
2. session.run(optimizer,feed_dict={...})运行迭代

* 在optimizer被run的时候会自动修改那些允许修改的variable
* feed_dict需要保证loss_function有结果，需要填充所有place_holder
