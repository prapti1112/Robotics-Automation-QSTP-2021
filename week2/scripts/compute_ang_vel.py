#!/usr/bin/env python

from __future__ import print_function
import rospy
from week2.srv import ComputeAngVel, ComputeAngVelResponse

lin_vel = 0.1

def handle_compute_ang_vel(req):
	rospy.loginfo("Angular velocity: " + str(req.radius*lin_vel))
	return ComputeAngVelResponse(req.radius*lin_vel)

def compute_ang_vel_server():
	rospy.init_node('compute_ang_vel_server', anonymous=True)
	srv = rospy.Service('compute_ang_vel', ComputeAngVel, handle_compute_ang_vel)
	rospy.spin()

if __name__ == '__main__':
	compute_ang_vel_server()