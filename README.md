# kthfs_recruitment

For all exercises ROS melodic is required. Make sure that you have put all packages in a catkin workspace, sourced the setup.bash and ran catkin build.
## Exercise 1

Open 3 terminals in your terminal emulator of coice and run the following:

Terminal 3
```
roscore #(duh)
```

Terminal 1
```
rosrun package1 nodeA.py
```

Terminal 2
```
rosrun package2 nodeB.py
```

## Exercise 2

### Prerequisites
Make sure that PlotJuggler is installed. On Ubuntu 18.04 this is done by executing
```
apt install ros-melodic-plotjuggler-ros
```
in a terminal.

To call the plotting, make sure you have a rosmaster running and then run the following:
```
cd exercise2
rosrun plotjuggler plotjuggler -ntl hairy_plotter.xml
```