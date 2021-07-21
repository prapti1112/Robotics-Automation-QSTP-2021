#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def helloChatter():
	hello_pub = rospy.Publisher('hello', String, queue_size=10)
	rospy.init_node('helloChatter', anonymous=True)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		rospy.loginfo("Hello,")
		hello_pub.publish("Hello,")
		rate.sleep()

if __name__ == '__main__':
    try:
        helloChatter()
    except rospy.ROSInterruptException:
        print("Error occured")
		