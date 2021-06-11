#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import CameraInfo

rospy.init_node('camera_info', anonymous=True)

pub = rospy.Publisher('/camera_rect/camera_info', CameraInfo, queue_size=10)
rate = rospy.Rate(60)
while not rospy.is_shutdown():
    q=CameraInfo()

    q.header.frame_id='usb_cam'
    q.height=480
    q.width=640
    q.D=[-0.33103167198475064, 0.09772179898578282, 0.0008292381650090525, -0.0006677843828297919, 0.0]
    q.K=[371.2032342831248, 0.0, 349.28473358200955, 0.0, 372.0393501292635, 248.9239364474581, 0.0, 0.0, 1.0]
    q.R=[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    q.P=[279.1053161621094, 0.0, 349.7372998494793, 0.0, 0.0, 309.8751525878906, 253.04511004714732, 0.0, 0.0, 0.0, 1.0, 0.0]
    q.binning_x=0
    q.binning_y=0
    q.roi.x_offset=0
    q.roi.y_offset=0
    q.roi.height=0
    q.roi.width=0
    q.roi.do_rectify=False
    pub.publish(q)
    rate.sleep()

