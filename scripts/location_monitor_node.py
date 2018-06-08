#!/usr/bin/env python
import rospy
from  nav_msgs.msg import Odometry

#Position of landmarks in turtlebot gazebo enviroment
landmarks = []
#name, x, y
landmarks.append(("cylinder", -2.0, -3.48))
landmarks.append(("Barrier", -4.0, -1.0))
landmarks.append(("Bookshelve", 0, 1.53026))

def distance(x, y, l_x, l_y):
	pass

def callback(msg):
	#we can access to this data through executing turtlebot_gazebo
	#then we execute: rostopic type /odom
	#and: rosmsg show /nav_msgs/Odometry
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	#We show the position with odometry
	#rospy.loginfo('x: {}, y: {}'.format(x,y))
	closest_name = None
	closest_distance = None
	for l_name, l_x, l_y in landmarks:
		landDistance = distance(x,y, l_x, l_y)

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
