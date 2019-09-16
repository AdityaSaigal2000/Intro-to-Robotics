#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String


def publisher_node():
   rospy.init_node('motor') 
   cmd_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
   speedx=0.2
   twist=Twist()
   twist.linear.x=speedx
   twist.angular.z=0
   begin=rospy.get_rostime().to_sec()
   t=rospy.get_rostime().to_sec()
   distance=0
   while (distance<1):
	t=rospy.get_rostime().to_sec()
	rospy.loginfo(twist.linear.x)
	cmd_pub.publish(twist)
	print(t-begin)
	distance=twist.linear.x*(t-begin)
	rospy.sleep(0.2)
   angle=0
   variance=0.12
   finalA=6.28
   begin=rospy.get_rostime().to_sec()
   while (angle<(finalA-variance)):
	t=rospy.get_rostime().to_sec()
   	rospy.loginfo(twist.linear.x)
   	twist.linear.x=0
	twist.angular.z=1
        angle=1*(t-begin)
   	cmd_pub.publish(twist)
   	print("hello")
	print(twist.linear.x)
	rospy.sleep(0.2)
   twist.angular.z=0
   cmd_pub.publish(twist)
   pass

def main():
  
    try:
	publisher_node()
    except rospy.ROSInterruptException:
        pass
    
if __name__ == '__main__':
    main()
