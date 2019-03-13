#include <ros/ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <geometry_msgs/Twist.h>

int id = 0;
ros::Publisher action_pub;
geometry_msgs::Twist set_vel;

void objectCallback(const std_msgs::Float32MultiArrayPtr &object) {
   if (object->data.size() <= 0) {
      // not object detected
      set_vel.linear.x = 1;
      set_vel.angular.z = 0;
      }
      action_pub.publish(set_vel);
   }
   else {
      // object detected
      set_vel.linear.x = 0;
      set_vel.angular.z = 0;
      action_pub.publish(set_vel);
   }
}

int main(int argc, char **argv) {

   ros::init(argc, argv, "action_controller");
   ros::NodeHandle n("~");
   ros::Rate loop_rate(50);
   ros::Subscriber sub = n.subscribe("/objects", 1, objectCallback);
   action_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
   set_vel.linear.x = 1;
   set_vel.linear.y = 0;
   set_vel.linear.z = 0;
   set_vel.angular.x = 1;
   set_vel.angular.y = 0;
   set_vel.angular.z = 0;
   while (ros::ok()) {
      ros::spinOnce();
      loop_rate.sleep();
   }
}
