#!/usr/bin/env python2
import rospy
from std_msgs.msg import Float32
import math
def publisher(num):
	num =  math.log(num.data)
	pub = rospy.Publisher('random_float_log', Float32)
	rate = rospy.Rate(20)
	while not rospy.is_shutdown():
		pub.publish(num)
		rate.sleep()

def subscriber():

	rospy.init_node('simple_subscriber')
	rospy.Subscriber('my_random_float', Float32, publisher)
	rospy.spin()

if __name__ == '__main__':
	subscriber()
