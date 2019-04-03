#include <ros/ros.h>
#include <sensor_msgs/Range.h>

float distFL = 0;
float distFR = 0;
float average_dist = 0;
float desired_dist = 0.2;

void distFL_callback(const sensor_msgs::Range &range) {
       distFL = range.range;
       printf("distFL: %d", distFL);
    }

void distFR_callback(const sensor_msgs::Range &range) {
       distFR = range.range;
       printf("distFR: %d", distFR);
    }

int main(int argc, char **argv){
        ros::Rate loop_rate(50);
        ros::Subscriber distFL_sub = n.subscribe("/range/fl", 1, distFL_callback);
        ros::Subscriber distFR_sub = n.subscribe("/range/fr", 1, distFR_callback);
        while (ros::ok()) {
	ros::spinOnce();
	loop_rate.sleep();
    }
