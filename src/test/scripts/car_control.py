import rospy
#��������Ҫ��Python for ROS��
from geometry_msgs.msg import Twist
from math import pi
#����geometry_msgs���е�Twist��Ϣ����
class OutAndBack():
    def __init__(self):
        # �ڵ�����
        rospy.init_node('out_and_back', anonymous=False)
        # ���ն˰���Ctrl��C֮�������ֹ�ڵ�      
        rospy.on_shutdown(self.shutdown) 
        # ������/cmd_vel Topic�з���Twist��Ϣ�����ƻ������ٶ�
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
        rate = 50 
        # ���ø���Ƶ��Ϊ50HZ
        r = rospy.Rate(rate) 
        # ���ٶ�
        linear_speed = 0.2 
        # Ŀ�����
        goal_distance = 1.0
        # ����Ŀ���ʱ��
        linear_duration = goal_distance / linear_speed
        # ���ٶ� 1.0rad/s
        angular_speed = 1.0 
        # ת��ΪPi(180 degrees)
        goal_angle = pi
        # How long should it take to rotate?
        angular_duration = goal_angle / angular_speed

        # Loop through the two legs of the trip  
        for i in range(2):
            # Initialize the movement command
            move_cmd = Twist()

            # Set the forward speed
            move_cmd.linear.x = linear_speed
            # ��������ǰ�˶�����ʱһ��ʱ��
            ticks = int(linear_duration * rate)
            for t in range(ticks):
                self.cmd_vel.publish(move_cmd)
                r.sleep()

            # ����һ���յ�Twist��Ϣ�ǻ�����ֹͣ
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)

            move_cmd.angular.z = angular_speed
            # �����˿�ʼ��ת����ʱһ��ʱ��ʹ������ת180��
            ticks = int(goal_angle * rate)
            for t in range(ticks):
                self.cmd_vel.publish(move_cmd)
                r.sleep()

            # ͣ����
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)

        # ѭ������֮��ֹͣ
        self.cmd_vel.publish(Twist())

        # ���� shutdown(self)�����ֶ�ֹͣ������
    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        OutAndBack()
    except:
        rospy.loginfo("Out-and-Back node terminated.")
