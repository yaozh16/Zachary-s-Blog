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
1. Using catkin_make
```
catkin_make [make_targets] [-DCMAKE_VARIABLES=...]
```
