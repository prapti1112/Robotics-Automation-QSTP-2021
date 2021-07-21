#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import message_filters

def callback(hello_str, world_str):
	final_str = str(hello_str.data) + str(world_str.data)
	rospy.loginfo(final_str)

	pub.publish(final_str)
	rate.sleep()


def helloWorldListener():
	

	hello_str = message_filters.Subscriber("hello", String)
	world_str = message_filters.Subscriber("world", String)
	
	synchronizer = message_filters.ApproximateTimeSynchronizer([hello_str, world_str], 10, 0.1, allow_headerless=True)
	synchronizer.registerCallback(callback)

	rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node("helloWorldListener", anonymous=True)
	
        pub = rospy.Publisher("helloWorld", String, queue_size=10)
        rate = rospy.Rate(15)
		
        helloWorldListener()
    except rospy.ROSInterruptException:
        print("Error occured")
	