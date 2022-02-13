#!/usr/bin/env python2
import rospy
from sensor_msgs.msg import LaserScan
import math
import random

def publisher():
	pub = rospy.Publisher("fake_scan", LaserScan)
	rospy.init_node('fake_scan_publisher')
	rate = rospy.Rate(20)
	while not rospy.is_shutdown():
		scan = LaserScan()
		scan.header.stamp = rospy.Time.now()
		scan.header.frame_id = "base_link"
		scan.angle_min = -2./3*math.pi
		scan.angle_max = 2./3*math.pi
		scan.angle_increment = 1./300*math.pi
		scan.scan_time = 1/20
		scan.range_min = 1.0
		scan.range_max = 10.0
		ranges_ = []
		for i in range(400):
			ranges_.append(random.uniform(1.0, 10.0))
		scan.ranges = ranges_
		pub.publish(scan)
		rate.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
