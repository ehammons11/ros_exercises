#!/usr/bin/env python2
import rospy
import random
from std_msgs.msg import Float32

def simple_publisher():
	pub = rospy.Publisher("my_random_float",Float32)
	rospy.init_node("simple_publisher")
	rate = rospy.Rate(20)
	while not rospy.is_shutdown():
		num =  random.uniform(0,10.0)
		rospy.loginfo(num)
		pub.publish(num)
		rate.sleep()
if __name__ == '__main__':
	try:
		simple_publisher()
	except rospy.ROSInterruptException:
		pass
