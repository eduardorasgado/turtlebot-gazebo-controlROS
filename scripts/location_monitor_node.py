#!/usr/bin/env python
import rospy
from  nav_msgs.msg import Odometry

def callback(msg):
	#we can access to this data through executing turtlebot_gazebo
	#then we execute: rostopic type /odom
	#and: rosmsg show /nav_msgs/Odometry
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	#We show the position with odometry
	rospy.loginfo('x: {}, y: {}'.format(x,y))

def main():
	#initialize ros node
	rospy.init_node('location_monitor')
	#subscribe to odom topic
	#Odometry is the actual msg class
	rospy.Subscriber('/odom', Odometry, callback)
	#loop for rospy
	rospy.spin()
	#print("hello world")

if __name__=='__main__':
	main()
