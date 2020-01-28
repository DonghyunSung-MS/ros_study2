
static transform
```
$ rosrun ros_study2 tf2_static_broadcaster_cpp myturtle 0 0 1 0 0 0
$ rostopic echo /tf2_static

``` 
```
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
'''
