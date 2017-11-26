#/bin/bash
passWord="yourpassword"
directoryPath="~/catkin_ws"
sudo -S su root << EOF
$passWord
EOF
sudo apt-get update
sudo -S apt-get install -y python-wstool python-rosdep ninja-build git google-mock libboost-all-dev  libeigen3-dev libgflags-dev libgoogle-glog-dev liblua5.2-dev libprotobuf-dev  libsuitesparse-dev libwebp-dev ninja-build protobuf-compiler python-sphinx  ros-kinetic-tf2-eigen libatlas-base-dev libsuitesparse-dev liblapack-dev
<<EOF
Y
EOF

if [! -d "$directoryPath"];
then
	mkdir $directoryPath
	echo "Create Path"
else
	echo "Path exists"
fi
cd $directoryPath
echo "In directory"
wstool init src
echo "Init Done"
wstool merge -t src https://raw.githubusercontent.com/googlecartographer/cartographer_ros/master/cartographer_ros.rosinstall
echo "merge Done"
wstool update -t src
cd src
git clone https://github.com/hitcm/cartographer_ros.git
if [! rosdep init]
	echo "Inited..."
then
	sudo rm /etc/ros/rosdep/sources.list.d/20-default.list
	sudo rosdep init
fi
rosdep update
cd ..
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
echo "The next step  may take long time please quit only when \"Finished\" appears "
catkin_make_isolated --install --use-ninja
source install_isolated/setup.bash
echo "Finished"


