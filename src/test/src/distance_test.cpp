#include <ros/ros.h>
#include <sensor_msgs/Range.h>
#include <geometry_msgs/Twist.h>

float distFL = 0;
float distFR = 0;
float mim_dist = 0.1;

ros::Publisher action_pub;
geometry_msgs::Twist set_vel;

void distFL_callback(const sensor_msgs::Range &range) {
       distFL = range.range;
       printf("distFL: %.2f\n", distFL);
    }

void distFR_callback(const sensor_msgs::Range &range) {
       distFR = range.range;
       printf("distFR: %.2f\n", distFR);
    }

void cal(){
        if (distFR < mim_dist && distFL < mim_dist){
		printf("both direction not pass, back\n");
		set_vel.linear.x = -0.5;
                set_vel.angular.z = 0;
	}
	else if (distFR < mim_dist && distFL > mim_dist){
		printf("turn left\n");
		set_vel.linear.x = 0;
                set_vel.angular.z = 1;
	}
	else if (distFR > mim_dist && distFL < mim_dist){
		printf("turn right\n");
		set_vel.linear.x = 0;
                set_vel.angular.z = -1;
	}
	else{
		printf("go ahead\n");
		set_vel.linear.x = 0.5;
                set_vel.angular.z = 0;
	}
	action_pub.publish(set_vel);
    }

int main(int argc, char **argv){
	ros::init(argc, argv, "action_controller");
	ros::NodeHandle n("~");
        ros::Rate loop_rate(50);
        ros::Subscriber distFL_sub = n.subscribe("/range/fl", 1, distFL_callback);
        ros::Subscriber distFR_sub = n.subscribe("/range/fr", 1, distFR_callback);
	action_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
        while (ros::ok()) {
		cal();
		ros::spinOnce();
		loop_rate.sleep();
    }
}
