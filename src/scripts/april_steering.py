#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32, Int32
from tf2_msgs.msg import TFMessage
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan

APRILTAG_CAMERA_TOPIC_NAME = '/tag_detections_image'
APRILTAG_GUIDANCE_NODE_NAME = 'apriltag_guidance_node'
LIDAR_TOPIC_NAME = '/scan'
STEERING_TOPIC_NAME = '/steering'
THROTTLE_TOPIC_NAME = '/throttle'
APRILTAG_TOPIC_NAME = '/tf'

global steering_float, throttle_float
steering_float = Float32()
throttle_float = Float32()


class Car:
    def __init__(self):
        self.apriltagMsg = None
        self.lidarMsg = None
        self.garageFound = False

    def apriltag_callback(self, msg):
        # "Store" message received.
        self.apriltagMsg = msg

        # Compute stuff.
        self.garageFinder()

    def lidar_callback(self, msg):
        # "Store" the message received.
        self.lidarMsg = msg

        # Compute stuff.
        self.garageFinder()

    def isNearWall(self):
        #for distance in range(270, 450):
        if self.lidarMsg.ranges[360] < 0.2:
            rospy.loginfo(distance)
            return True
        else:
            return False
    def garageFinder(self):
        kp = 2.0
        global steering_float, throttle_float
        steering_float = Float32()
        throttle_float = Float32()
        steering_float_temp = 0.0

        if self.lidarMsg.ranges[360] < 1.5:
            throttle_float = 0.05
        elif (self.apriltagMsg.transforms[0].child_frame_id == "TURN_LEFT") and (not self.garageFound):
            throttle_float = 0.19
            steering_float_temp = -0.2
        
        elif (self.apriltagMsg.transforms[0].child_frame_id == "TURN_RIGHT") and (not self.garageFound):
            throttle_float = 0.19
            steering_float_temp = 0.2
        elif (self.apriltagMsg.transforms[0].child_frame_id == "TURN_AROUND") and (not self.garageFound):
            throttle_float = 0.19
            if self.lidarMsg.ranges[180] < self.lidarMsg.ranges[540]:
                steering_float_temp = -0.2
            else:
                steering_float_temp = 0.2
        elif self.apriltagMsg.transforms[0].child_frame_id == "GARAGE":
            self.garageFound = True
            throttle_float = 0.19
            steering_float_temp = (kp * self.apriltagMsg.transforms[0].transform.translation.x) - 0.05
            
        if steering_float_temp < -0.25:
            steering_float_temp = -0.25
        elif steering_float_temp > 0.25:
            steering_float_temp = 0.25
        else:
            pass

        steering_float = steering_float_temp
        steering_pub.publish(steering_float)
        throttle_pub.publish(throttle_float)

if __name__ == '__main__':
    rospy.init_node(APRILTAG_GUIDANCE_NODE_NAME, anonymous=False)

    car = Car()

    apriltag_subscriber = rospy.Subscriber(APRILTAG_TOPIC_NAME, TFMessage, car.apriltag_callback)
    lidar_subscriber = rospy.Subscriber(LIDAR_TOPIC_NAME, LaserScan, car.lidar_callback)


    steering_pub = rospy.Publisher(STEERING_TOPIC_NAME, Float32, queue_size=1)
    throttle_pub = rospy.Publisher(THROTTLE_TOPIC_NAME, Float32, queue_size=1)
    rate = rospy.Rate(15)
    while not rospy.is_shutdown():
        rospy.spin()
        rate.sleep()
