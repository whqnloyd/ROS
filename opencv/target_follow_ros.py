import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

template = cv2.imread('image/test_target.jpg', 0)
w, h = template.shape[::-1]
# first 2 are good for color change, and next 2 are good for distort
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
methods = ['cv2.TM_CCOEFF_NORMED']
method = eval(methods[0])

def callback(data):
    # define picture to_down' coefficient of ratio
    scaling_factor = 0.5
    global count,bridge
    count = count + 1
    if count == 1:
        count = 0
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
	img_1 = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_1, template, method)
	threshold = 0.5
	thresh_loc = np.where(res >= threshold)

	# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	# if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
	#     top_left = min_loc
	# else:
	#     top_left = max_loc
	# bottom_right = (top_left[0] + w, top_left[1] + h)
	# target_img = img_1[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
	# cv2.rectangle(img_0, top_left, bottom_right, 255, 2)

	#for pt in zip(*thresh_loc[::-1]):
	#	cv2.rectangle(cv_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
	loc_x=np.median(thresh_loc[::-1][0])
	loc_y=np.median(thresh_loc[::-1][1])
	if loc_x > 0 and loc_y > 0:
		cv2.rectangle(cv_img, (int(loc_x), int(loc_y)), (int(loc_x+w), int(loc_y+h)), (0, 0, 255), 2)
	print(loc_x)
	print(loc_y)

	if 220<(loc_x+w/2) and (loc_x+w/2)<440:
		print('go ahead')
	elif (loc_x+w/2)<=220:
		print('turn left')
	elif (loc_x+w/2)>=440:
		print('turn right')
	else:
		print('no object')
        cv2.imshow("frame" , cv_img)
        cv2.waitKey(1)
    else:
        pass
 
def displayWebcam():
    rospy.init_node('webcam_display', anonymous=True)
 
    # make a video_object and init the video object
    global count,bridge
    count = 0
    bridge = CvBridge()
    rospy.Subscriber('/camera/rgb/image_raw', Image, callback)
    rospy.spin()
 
if __name__ == '__main__':
    displayWebcam()



