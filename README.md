ROS STUDY DAY2
==============
## Enviroment
ros-kinetic(ubuntu 16.04)
##### Ref : [robot_state_publisher](http://wiki.ros.org/robot_state_publisher) , [tf2](http://wiki.ros.org/tf2/Tutorials)
## 1. URDF(Ex. planar 3R mainipulator)
```
$ roslaunch ros_study2 my_simple_urdf_disply.launch
```
## 2. Static Transform Broadcaster
#### Execute
```
$ rosrun ros_study2 tf2_static_broadcaster_cpp myturtle 0 0 1 0 0 0
                              or
$ rosrun ros_study2 tf2_static_broadcaster.py myturtle 0 0 1 0 0 0 #may need chmod to execute

```
#### Output

```
$ rostopic echo /tf2_static
  transforms:
    -
      header:
        seq: 0
        stamp:
          secs: 1580193420
          nsecs: 460367279
        frame_id: "world"
      child_frame_id: "myturtle"
      transform:
        translation:
          x: 0.0
          y: 0.0
          z: 1.0
        rotation:
          x: 0.0
          y: 0.0
          z: 0.0
          w: 1.0
  ---
```
## 3. Transform Broadcaster
#### Execute
```
$ rosrun ros_study2 tf2_broadcaster_cpp turtle1
                              or
$ rosrun ros_study2 tf2_broadcaster.py turtle1 #may need chmod to execute
```
#### Output
```
rosrun tf tf_echo /world /turtle1
At time 1580195645.381
- Translation: [5.544, 5.544, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.000, 1.000]
            in RPY (radian) [0.000, -0.000, 0.000]
            in RPY (degree) [0.000, -0.000, 0.000]
```
## 4. Transform Listener
#### Run node seperately
```
$ rosrun ros_study2 tf2_broadcaster_cpp turtle1
                              or
$ rosrun ros_study2 tf2_broadcaster.py turtle1 #may need chmod to execute
```
```
$ rosrun ros_study2 tf2_broadcaster_cpp turtle2
                              or
$ rosrun ros_study2 tf2_broadcaster.py turtle2 #may need chmod to execute
```
```
$ rosrun ros_study2 tf2_listener_cpp
                              or
$ rosrun ros_study2 tf2_listener.py #may need chmod to execute
```
#### Run node at once
```
$ roslaunch ros_study2 turtle_sim_tf_tutorial.launch  #python
                               or
$ roslaunch ros_study2 turtle_sim_tf_tutorial_cpp.launch
