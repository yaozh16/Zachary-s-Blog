# ROS learning [1]
## ros command
### rospack
rospack find [package_name]
### roscd
roscd [locationname[/subdir]]
### $ROS_PACKAGE_PATH
echo $ROS_PACKAGE_PATH
### roscd log
file log directory
### rosls
rosls [locationname[/subdir]]
## Create package
### Create catkin_ws
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
```
### Packages in a Catkin Workspace
```
workspace_folder/        -- WORKSPACE
  src/                   -- SOURCE SPACE
    CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
    package_1/
      CMakeLists.txt     -- CMakeLists.txt file for package_1
      package.xml        -- Package manifest for package_1
    ...
    package_n/
      CMakeLists.txt     -- CMakeLists.txt file for package_n
      package.xml        -- Package manifest for package_n
```
### Creating a Catkin Package
```
cd ~/catkin_ws/src
# example: catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
cd ..
catkin_make
```
### Package Dependency
查询直接依赖项
```
rospack depends1 beginner_tutorials
```
以上可以在package.xml中查到

查询所有依赖项
```
rospack depends beginner_tutorials
```
### Customizing Your Package
#### Customizing the package.xml
1. description tags
2. maintainer tags
3. license tags
more at [Licenses](http://opensource.org/licenses/alphabetical)
4. dependencies tags
more at [Dependencies](http://wiki.ros.org/catkin/package.xml#Build.2C_Run.2C_and_Test_Dependencies)
&emsp;1) build_depend
&emsp;2) buildtool_depend
&emsp;3) exec_depend
&emsp;4) test_depend
## Building a ROS Package
### Building Packages
Using catkin_make
```
catkin_make [make_targets] [-DCMAKE_VARIABLES=...]
```
## Understanding ROS Nodes
### Overview
* Nodes: A node is an executable that uses ROS to communicate with other nodes.

* Messages: ROS data type used when subscribing or publishing to a topic.

* Topics: Nodes can publish messages to a topic as well as subscribe to a topic to receive messages.

* Master: Name service for ROS (i.e. helps nodes find each other)

* rosout: ROS equivalent of stdout/stderr

* roscore: Master + rosout + parameter server (parameter server will be introduced later)
### Using rosnode
所有node
```
rosnode list
```
查看node
```
rosnode info /rosout
```
已经关闭的node仍然在表中则可以使用
```
rosnode cleanup
```
交互
```
rosnode ping my_turtle
```
### Using rosrun
```
rosrun [package_name] [node_name]
# example:
rosrun turtlesim turtlesim_node
rosrun turtlesim turtle_teleop_key
```
* [remap](http://wiki.ros.org/Remapping%20Arguments)
```
rosrun turtlesim turtlesim_node __name:=my_turtle
```
## Understanding ROS Topics
### Rqt rqt_graph
```
rosrun rqt_graph rqt_graph
```
### get helps
```
rostopic -h
```
可以看到
```
rostopic type [topic]

rostopic list [-v-h等]

rostopic echo [topic]

rostopic pub [topic] [msg_type] [args]
# 例如rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```
* rosmessage
```
rosmsg show geometry_msgs/Twist
```
## Understanding ROS Services and Parameters
* request
* response
### overview
```
rosservice list         print information about active services
rosservice call         call the service with the provided args
rosservice type         print service type
rosservice find         find services by service type
rosservice uri          print service ROSRPC uri
```
### rosservice type
查看service与arg类型
```
rosservice type [service]

# 可以rosservice type [service]|rossrv show

```
### rosservice call
```
rosservice call [service] [args]
```
### Using rosparam
```
rosparam set [param]            set parameter
rosparam get [param]           get parameter
rosparam dump [file_name] [namespace]     dump params to file
rosparam load [file_name] [namespace]     load params from file
rosparam delete [param]         delete parameter
rosparam list           list parameter names
```
## Using rqt_console and roslaunch
### Using Rqt
```
rosrun rqt_console rqt_console
rosrun rqt_logger_level rqt_logger_level
```
信息优先级，设置在低级可以接收到上级与自身等级的消息
```
Fatal
Error
Warn
Info
Debug
```
### Using roslaunch
```
roslaunch [package] [filename.launch]
```
* 创建launch文件
```
roscd packagename
# 这一步如果失败找不到要重新到catkin_ws里面source一下devel/setup.bash

roscd beginner_tutorials
mkdir launch
cd launch
```
创建.launch文件如下
```
<launch>

  <group ns="turtlesim1">
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>

  <group ns="turtlesim2">
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>

  <node pkg="turtlesim" name="mimic" type="mimic">
    <remap from="input" to="turtlesim1/turtle1"/>
    <remap from="output" to="turtlesim2/turtle1"/>
  </node>

</launch>
```
其中mimic使得turtlesim2模仿turtlesim1
## Using rosed to edit files in ROS
```
 rosed [package_name] [filename]
 # rosed roscpp Logger.msg
```
## Creating a ROS msg and srv
* msg: msg files are simple text files that describe the fields of a ROS message. They are used to generate source code for messages in different languages.

* srv: an srv file describes a service. It is composed of two parts: a request and a response.

### steps
1. [m/s]write .msg/.srv文件在[package]/msg(srv)目录下
2. [m]修改package.xml
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
3. [m/s]修改CMakeList.txt共同步骤1
```
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
```
4. [m]
```
catkin_package(
  ...
  CATKIN_DEPENDS message_runtime ...
  ...)

add_message_files(
    FILES
    Num.msg
  )
```
5. [s]
```
add_service_files(
  FILES
  AddTwoInts.srv
)
```
6. [m/s]修改CMakeList.txt共同步骤2
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```
7. [m/s]在catkin_ws中catkin_make install
