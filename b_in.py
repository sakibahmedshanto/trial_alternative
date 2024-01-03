#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def publisher_ros():
    rospy.init_node('publisher_node_ros', anonymous=True)
    pub_ros = rospy.Publisher('input_topic_ros', Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    count = 0
    while not rospy.is_shutdown():
        # Publish integers to 'input_topic_ros'
        rospy.loginfo(f"Publishing to input_topic_ros: {count}")
        pub_ros.publish(count)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_ros()
    except rospy.ROSInterruptException:
        pass
