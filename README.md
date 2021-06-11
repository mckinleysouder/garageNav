# garageNav

This repo holds the files that were added to the ROS package dependencies in order to
get the garageNav project to work.

## Dependencies:

We used our TA's package [ucsd_robo_car_simple_ros](https://gitlab.com/djnighti/ucsd_robo_car_simple_ros) to use his convenient launch file for throttle and steering,
and to house our script and launch file.

Our project also depends on the [apriltag_ros](http://wiki.ros.org/apriltag_ros) package
as well as the [rplidar](http://wiki.ros.org/rplidar) package to support both identifying AprilTags through the webcam and getting the sensor data from the lidar