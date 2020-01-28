#include <ros/ros.h>
#include <tf/LinearMath/Quaternion.h>
#include <tf2_ros/static_transform_broadcaster.h>
#include <geometry_msgs/TransformStamped.h>


int main(int argc,char** argv)
{
  ros::init(argc,argv,"my_static_tf2_bradcaster");
  ros::NodeHandle nh;
  if (argc < 8)
  {
    ROS_ERROR("usage %s name x y z r p y ",argv[0]);
    return 1;
  }
  else
  {
    if (argv[1]=="world")
    {
      ROS_ERROR("your static turtle name cannot be 'wolrd'");
      return 1;
    }
    //declartion
    static tf2_ros::StaticTransformBroadcaster broadcaster;
    geometry_msgs::TransformStamped static_transformationStamped;

    static_transformationStamped.header.stamp = ros::Time::now();
    static_transformationStamped.header.frame_id = "world";
    static_transformationStamped.child_frame_id = argv[1]; // get value from user

    // translation part of homogeneous transform
    static_transformationStamped.transform.translation.x = atof(argv[2]);
    static_transformationStamped.transform.translation.y = atof(argv[3]);
    static_transformationStamped.transform.translation.z = atof(argv[4]);

    tf::Quaternion quat;
    quat.setRPY(atof(argv[5]),atof(argv[6]),atof(argv[7]));

    static_transformationStamped.transform.rotation.x = quat[0];
    static_transformationStamped.transform.rotation.y = quat[1];
    static_transformationStamped.transform.rotation.z = quat[2];
    static_transformationStamped.transform.rotation.w = quat[3];

    broadcaster.sendTransform(static_transformationStamped);
    ros::spin();
    return 0;
  }
}
