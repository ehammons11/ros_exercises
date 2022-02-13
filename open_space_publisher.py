#!/usr/bin/env python2
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from ros_exercises.msg import OpenSpace

def publisher(Laser):
	Ranges = Laser.ranges
	Ranges_sorted  = sorted(Ranges)
	num = Ranges_sorted[len(Ranges)-1]
	pos = Ranges.index(num)
	angle_num = Laser.angle_min + pos*Laser.angle_increment
	space = OpenSpace()
	space.angle = angle_num
	space.distance = num
	pub = rospy.Publisher(ropsy.get_param("/open_space_publisher/pub_topic", 'open_space'), OpenSpace, queue_size = 10)
	rate = rospy.Rate(20)
	while not rospy.is_shutdown():
		pub.publish(space)
		rate.sleep()


def subscriber():
	rospy.init_node("open_space_publisher")
	rospy.Subscriber(rospy.get_param("/open_space_publisher/sub_topic", 'fake_scan'), LaserScan, publisher)
	rospy.spin()

if __name__ == '__main__':
	subscriber()
