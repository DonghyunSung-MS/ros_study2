#! /usr/bin/env python
import rospy
import system
import tf2
import tf2_ros
import geometry_msgs.msg

if __name__=="__main__":
    # 입력 갯수 제한
    if len(sys.argv) < 8:
        rospy.logerr('Invalid number of parameters\nusage: '
                        './static_turtle_tf2_broadcaster.py '
                        'child_frame_name x y z roll pitch yaw')
        sys.exit(0)
    else:
        if sys.argv[1] == "world":
            rospy.logerr('Your static turtle name cannot be "world"')
            sys.exit(0)

        rospy.init_node('my_static_tf2_broadcaster')
        # This class provides an easy way to publish coordinate frame transform information
        broadcaster = tf2_ros.StaticTransformBroadcaster()
        # geometry_msgs.TransformStamped
        # Header header
        # string child_frame_id # the frame id of the child frame
        # Transform transform
        static_transformationStamped = geometry_msgs.msg.TransformStamped()

        static_transformationStamped.header.stamp = rospy.Time.now()
        static_transformationStamped.header.frame_id = "world"
        static_transformationStamped.child_frame_id = sys.argv[1] # get value from user

        # translation part of homogeneous transform
        static_transformationStamped.transform.translation.x = float(sys.argv[2])
        static_transformationStamped.transform.translation.y = float(sys.argv[3])
        static_transformationStamped.transform.translation.z = float(sys.argv[4])

        quat = tf.transformation.quaternion_from_euler(
            float(sys.argv[5]) float(sys.argv[6]) float(sys.argv[7])) # get rpy from user and convert it to quat
        static_transformationStamped.transform.rotation.x = quat[0]
        static_transformationStamped.transform.rotation.y = quat[1]
        static_transformationStamped.transform.rotation.z = quat[2]
        static_transformationStamped.transform.rotation.w = quat[3]

        broadcaster.sendTransform(static_transformationStamped)
        rospy.spin()
