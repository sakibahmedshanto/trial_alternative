#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

START_MARKER = '<'
END_MARKER = '>'

def send_data_to_arduino(data):
    ser.write(f"{START_MARKER}{data}{END_MARKER}".encode())
    print(f"Sent to Arduino: {data}")

def receive_data_from_arduino():
    data = ser.readline().decode().strip()
    if data and data.startswith(START_MARKER) and data.endswith(END_MARKER):
        print(f"Received from Arduino: {data}")
        return int(data[len(START_MARKER):-len(END_MARKER)])
    else:
        return 0

def callback_ros(data):
    rospy.loginfo(f"Received from ROS: {data.data}")
    send_data_to_arduino(data.data)

def talker_ros():
    pub_ros = rospy.Publisher('output_topic_ros', Int32, queue_size=10)
    rospy.init_node('python_node_ros', anonymous=True)
    rospy.Subscriber('input_topic_ros', Int32, callback_ros)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        message_ros = receive_data_from_arduino()

        rospy.loginfo(f"Published to ROS: {message_ros}")
        pub_ros.publish(message_ros)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_ros()
    except rospy.ROSInterruptException:
        pass
    finally:
        ser.close()
        print("Serial connection closed.")
