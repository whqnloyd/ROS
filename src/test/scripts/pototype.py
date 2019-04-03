#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from geometry_msgs.msg import Twist

def motion(command,linear_speed,angular_speed):	
	global cmd_vel
	move_cmd = Twist()
	if (command=='go'):
		move_cmd.linear.x = linear_speed
	elif (command=='turn'):
		move_cmd.angular.z = angular_speed
	else:
		print('wrong command, will stop')
	cmd_vel.publish(move_cmd)

	return

def stop():
	rospy.loginfo("Stopping the robot...")
	cmd_vel.publish(Twist())
	return

def img_recog(data):
    global count,bridge
    count = count + 1
    if count > 100:
	count == 0
    if count % 5 == 0:
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
	cv_img = cv2.resize(cv_img,(320,240))
	img_1 = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_1, template, method)
	threshold = 0.6
	thresh_loc = np.where(res >= threshold)
	loc_x=np.median(thresh_loc[::-1][0])
	loc_y=np.median(thresh_loc[::-1][1])
	if loc_x > 0 and loc_y > 0:
		cv2.rectangle(cv_img, (int(loc_x), int(loc_y)), (int(loc_x+w), int(loc_y+h)), (0, 0, 255), 2)
		print('x: %.2f, y: %.2f' % (loc_x, loc_y))

	if 100<(loc_x+w/2) and (loc_x+w/2)<220:
		motion('go',0.2,0)
		print('go ahead')
	elif (loc_x+w/2)<=100:
		motion('turn',0,-1)
		print('turn left')
	elif (loc_x+w/2)>=220:
		motion('turn',0,1)
		print('turn right')
	else:
		stop()
		print('no object')
        cv2.imshow("frame" , cv_img)
        cv2.waitKey(1)
    else:
        pass
    return

template = cv2.imread('image/ttee.jpg', 0)
w, h = template.shape[::-1]
methods = ['cv2.TM_CCOEFF_NORMED']
method = eval(methods[0])

rospy.init_node('pototype', anonymous=True)
count = 0
bridge = CvBridge()
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.Subscriber('/camera/rgb/image_raw', Image, img_recog)
rospy.spin()
