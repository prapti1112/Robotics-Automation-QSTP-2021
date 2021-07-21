#!/usr/bin/env python

import rospy 
from std_msgs.msg import Int32

radius = 5

def radius_talker():
	radius_pub = rospy.Publisher('radius', Int32, queue_size=10)
	rospy.init_node('radius_talker', anonymous=True)
	rate =rospy.Rate(10)

	while not rospy.is_shutdown():
		rospy.loginfo(radius)
		radius_pub.publish(radius)
		rate.sleep()

if __name__ == '__main__':
	try:
		radius_talker()
	except rospy.ROSInterruptException:
		print("Error occured")