#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback_output_topic(data):
    rospy.loginfo(f"Received from output_topic_ros: {data.data}")

def subscriber_ros():
    rospy.init_node('subscriber_node_ros', anonymous=True)
    rospy.Subscriber('output_topic_ros', Int32, callback_output_topic)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_ros()
    except rospy.ROSInterruptException:
        pass
