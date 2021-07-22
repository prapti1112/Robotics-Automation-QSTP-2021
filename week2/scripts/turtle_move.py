#!/usr/bin/env python

from __future__ import print_function
import rospy
from std_msgs.msg import Int32
from week2.srv import *

def compute_ang_vel_client(radius):
	rospy.wait_for_service('compute_ang_vel')
	try:
		compute_ang_vel = rospy.ServiceProxy('compute_ang_vel', ComputeAngVel)
		resp = compute_ang_vel(radius)
		return resp.ang_vel
	except rospy.ServiceException as e:
		print("Serivce call failed: " + str(e))

def radiusCallback(radius):
	ang_vel = compute_ang_vel_client(radius.data)
	rospy.loginfo("Radius recieved: " + str(radius.data))
	rospy.loginfo("Calculated angular velocity: " + str(ang_vel))

def turtle_move():
	rospy.init_node('turtle_move', anonymous=True)
	rospy.Subscriber('radius', Int32, radiusCallback)
	rospy.spin()

if __name__ == '__main__':
	try:
		turtle_move()
	except rospy.ROSInterruptException:
		print("Error occured....")
	