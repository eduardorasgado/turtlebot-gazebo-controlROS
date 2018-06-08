#!/usr/bin/env python
import rospy
import math
from  nav_msgs.msg import Odometry
from turtle_monitor.msg import LandmarkDistance

def distance(x, y, l_x, l_y):
	xdistance = x - l_x
	ydistance = y - l_y
	#calculating the euclidean distance
	return math.sqrt((xdistance*xdistance) + (ydistance*ydistance))

class LandmarkMonitor(object):
	def __init__(self, pub, landmarks):
		self._pub = pub
		self._landmarks = landmarks

	def callback(self, msg):
		#we can access to this data through executing turtlebot_gazebo
		#then we execute: rostopic type /odom
		#and: rosmsg show /nav_msgs/Odometry
		x = msg.pose.pose.position.x
		y = msg.pose.pose.position.y
		#We show the position with odometry
		#rospy.loginfo('-----------------x: {}, y: {}'.format(x,y))

		#variables for the close landmark
		closest_name = None
		closest_distance = None
		#comparison landmark to robot distance
		for l_name, l_x, l_y in self._landmarks:
			landDistance = distance(x, y, l_x, l_y)
			if closest_distance is None or landDistance < closest_distance:
				#setting new closest one
				closest_name = l_name
				closest_distance = landDistance

		#lets do something with closest distance

		#Publish the data to closest_landmark topic
		landmarkPub = LandmarkDistance()
		landmarkPub.name = closest_name
		landmarkPub.distance = closest_distance
		self._pub.publish(landmarkPub)
		
		#Print in screen
		"""
		l = []
		l.append(closest_name)
		l.append(closest_distance)
		logD = "The closest obstacule is: {}, its distance is: {}".format(l[0],l[1])
		rospy.loginfo(logD)
		"""
		#rospy.loginfo(len(l))

def main():
	#Position of landmarks in turtlebot gazebo enviroment
	landmarks = []
	#name, x, y
	landmarks.append(("cylinder", -2.0, -3.48))
	landmarks.append(("Barrier", -4.0, -1.0))
	landmarks.append(("Bookshelve", 0, 1.53026))

	#initialize ros node
	rospy.init_node('location_monitor')

	#Create a publisher--------------------------
	#what topic to publish, message type
	pub = 	rospy.Publisher('closest_landmark', LandmarkDistance, queue_size=0)
	#create a landmark monitor
	monitor = LandmarkMonitor(pub, landmarks)

	#subscribe to odom topic--------------------
	#Odometry is the actual msg class
	rospy.Subscriber('/odom', Odometry, monitor.callback)
	#loop for rospy
	rospy.spin()
	#print("hello world")

if __name__=='__main__':
	main()
