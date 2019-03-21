import rospy
from geometry_msgs.msg import Twist
from math import pi

class CarControl():
    def __init__(self):
        rospy.init_node('car_control', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	self.rate = 50
        self.r = rospy.Rate(self.rate)
	self.motion_time=1

    def motion(self,command,linear_speed,angular_speed):
	move_cmd = Twist()

	if (command=='go'):
	    for i in range(self.motion_time*self.rate):
	        move_cmd.linear.x = linear_speed
	        self.cmd_vel.publish(move_cmd)
		self.r.sleep()
	    return
    
	if (command=='turn'):
	    for i in range(self.motion_time*self.rate):
	        move_cmd.angular.z = angular_speed
	        self.cmd_vel.publish(move_cmd)
		self.r.sleep()
	    return

	else: 
		print('wrong command, will stop')
		move_cmd = Twist()
		self.cmd_vel.publish(move_cmd)
		rospy.sleep(1)

    def stop():
	move_cmd = Twist()
	self.cmd_vel.publish(move_cmd)
	rospy.sleep(1)


    def shutdown(self):
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
        lit_car=CarControl()
	lit_car.motion('go',0.2,0)
	lit_car.motion('turn',0,-0.5)
	lit_car.motion('turn',0,0.5)
