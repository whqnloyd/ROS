//#include "hFramework.h"
//#include "hCloudClient.h"
#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/BatteryState.h"
#include "std_msgs/Bool.h"
//#include "ROSbot.h"

using namespace hFramework;

// Uncomment one of these lines, accordingly to range sensor type of your ROSbot
// If you have version with infared sensor:
// static const SensorType sensor_type = SENSOR_INFRARED;
// If you have version with laser sensor:
static const SensorType sensor_type = SENSOR_LASER;
// If you want to use your own sensor:
// static const SensorType sensor_type = NO_DISTANCE_SENSOR;

// Uncomment one of these lines, accordingly to IMU sensor type of your device
// If you have version with MPU9250:
static const ImuType imu_type = MPU9250;
// If you want to use your own sensor:
// static const ImuType imu_type = NO_IMU;

ros::NodeHandle nh;
sensor_msgs::BatteryState battery;
ros::Publisher *battery_pub;

int publish_counter = 0;

void twistCallback(const geometry_msgs::Twist &twist)
{
    rosbot.setSpeed(twist.linear.x, twist.angular.z);
}

void initCmdVelSubscriber()
{
    ros::Subscriber<geometry_msgs::Twist> *cmd_sub = new ros::Subscriber<geometry_msgs::Twist>("/cmd_vel", &twistCallback);
    nh.subscribe(*cmd_sub);
}

void resetCallback(const std_msgs::Bool &msg)
{
    if (msg.data == true)
    {
        rosbot.reset_odometry();
    }
}

void initResetOdomSubscriber()
{
    ros::Subscriber<std_msgs::Bool> *odom_reset_sub = new ros::Subscriber<std_msgs::Bool>("/reset_odom", &resetCallback);
    nh.subscribe(*odom_reset_sub);
}

void initBatteryPublisher()
{
    battery_pub = new ros::Publisher("/battery", &battery);
    nh.advertise(*battery_pub);
}

void hMain()
{
    rosbot.initROSbot(sensor_type, imu_type);
    platform.begin(&RPi);
    nh.getHardware()->initWithDevice(&platform.LocalSerial);
    nh.initNode();

    initBatteryPublisher();
    initCmdVelSubscriber();
    initResetOdomSubscriber();

    while (true)
    {
        nh.spinOnce();
        publish_counter++;
        if (publish_counter > 10)
        {
            // get battery voltage
            battery.voltage = rosbot.getBatteryLevel();
            // publish battery voltage
            battery_pub->publish(&battery);
            publish_counter = 0;
        }
        sys.delay(10);
    }
}
