#include <sensor_msgs/Image.h>
#include <ros/ros.h>
#include <std_msgs/UInt8.h>
#include <std_srvs/Empty.h>
#include <std_srvs/Trigger.h>

bool print_b;
ros::Publisher light_pub;
int frame_passed = 0;
int saved_imgs = 0;

void imageCallback(const sensor_msgs::ImageConstPtr &image){
	long long sum = 0;
	for(int value : image->data){
		sum+=value;
}
	int avg = sum/image->data.size();
	if (print_b){
		std::cout<<"lights"<<avg<<std::endl;
	}
	std_msgs::UInt8 light_value;
	light_value.data=avg;
	light_pub.publish(light_value);
	frame_passed++;
}

bool saved_img(std_srvs::Trigger::Request &req, std_srvs::Trigger::Response &res){
	res.success=1;
	std::string str("Saved images: ");
	std::string num=std::to_string(saved_imgs);
	str.append(num);
	res.message=str;
	return true;
}

int main(int argc, char **argv){
	ros::init(argc, argv, "example_node");
	ros::NodeHandle n("~");
	ros::Subscriber sub = n.subscribe("/camera/rgb/image_raw", 10, imageCallback);
	n.param<bool>("print_lights", print_b, true);
	light_pub = n.advertise<std_msgs::UInt8>("lights", 1);
	ros::ServiceClient client=n.serviceClient<std_srvs::Empty>("/image_saver/save");
	std_srvs::Empty srv;
	ros::ServiceServer service=n.advertiseService("saved_images", saved_img);
	ros::Rate loop_rate(50);
	while (ros::ok()){
		ros::spinOnce();
		if(frame_passed>30){
			frame_passed=0;
			client.call(srv);
			saved_imgs++;
		}
		loop_rate.sleep();	
	}
}
