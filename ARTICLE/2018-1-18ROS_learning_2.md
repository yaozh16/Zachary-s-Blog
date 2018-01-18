# ROS learning [2]
## Writing a Simple Publisher and Subscriber (Python)
1. create code in [package]/scripts/ folder
```
roscd beginner_tutorials
mkdir scripts
cd scripts
wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
chmod +x talker.py
chmod +x listener.py
```
### import rospy
### Publisher
1. 创建publisher
pub = rospy.Publisher([TopicName], [MessageType], queue_size=10)
2. 创建node
rospy.init_node([Node Name], anonymous=True)
3. 配置周期
rate = rospy.Rate(10)
4. 发送消息
```
while not rospy.is_shutdown():
      hello_str = "hello world %s" % rospy.get_time()
      rospy.loginfo(hello_str) # 输出到屏幕、log、rosout
      pub.publish(hello_str)
      rate.sleep()
```
消息也可以直接先默认创建然后修改data域

### Subscriber
1. 创建node
rospy.init_node([node name]'listener', anonymous=True)
2. 订阅topic
rospy.Subscriber([topic name]"chatter", [Message Type]String, callback)
其中callback的参数类型就是MessageType
调用其中的data域获取原始值
```
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
```
3. 运行
rospy.spin()
## Examining the Simple Publisher and Subscriber
```
roscore
rosrun beginner_tutorials talker.py
rosrun beginner_tutorials listener.py
```
