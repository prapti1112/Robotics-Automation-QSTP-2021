#!/usr/bin/env python

import rospy
from week2.srv import ComputeAnfVel, ComputeAnfVelResponse
from __future__ import print_function

lin_vel = 0.1

def handle_compute_ang_vel(req):
	print("Angular velocity: " + str(req.radius*lin_vel))
	return ComputeAnfVelResponse(req.radius*lin_vel)

def compute_ang_vel_server():
	rospy.init_node('compute_ang_vel_server', anonymous=True)
	srv = Service('compute_ang_vel', handle_compute_ang_vel)
	rospy.spin()

if __name__ == '__main__':
	compute_ang_vel_server()