This project:\
One node-> subscribes to /odom gazebo rostopic, reads position of turtlebot, compare to landmarks 
position(which are actually hard-coded). You can access to landmark position by opening:
roslaunch turtlebot_gazebo turtlebot_world.launch.
The comparison robot-landmarks is done through euclidean distance. 
  
Same node->Publish the nearest_landmark topic with name and distance of the nearest landmark

Steps to execute this package(do it in separated terminals):
1. roslaunch turtlebot_gazebo turtlebot_world.launch
2. rosrun turtle_monitor location_monitor_node.py
3. rostopic echo /closest_landmark\
To see if it works, execute the turtlebot teleop package and move the robot
4. roslaunch turtlebot_teleop keyboard_teleop.launch 
