#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def worldChatter():
	hello_pub = rospy.Publisher('world', String, queue_size=10)
	rospy.init_node('worldChatter', anonymous=True)
	rate = rospy.Rate(12)

	while not rospy.is_shutdown():
		rospy.loginfo("World!!!")
		hello_pub.publish(" World!!!")
		rate.sleep()

if __name__ == '__main__':
    try:
        worldChatter()
    except rospy.ROSInterruptException:
        print("Error occured")
		