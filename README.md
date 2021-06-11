# garageNav

This repo holds the files that were added to the ROS package dependencies in order to
get the garageNav project to work.

## Dependencies:

We used our TA's package [ucsd_robo_car_simple_ros](https://gitlab.com/djnighti/ucsd_robo_car_simple_ros) to use his convenient launch file for throttle and steering,
and to house our script and launch file.

Our project also depends on the [apriltag_ros](http://wiki.ros.org/apriltag_ros) package
as well as the [rplidar](http://wiki.ros.org/rplidar) package to support both identifying AprilTags through the webcam and getting the sensor data from the lidar

## Directions:

Clone the apriltag, rplidar, and ucsd_robo_car_simple_ros packages as well as any dependencies listed on their repositories. Then add the file in this repo's scripts dir to ucsd_robo_car_simple_ros's scripts dir, and this repo's launch file to ucsd_robo_car_simple_ros's launch dir. Additionally, the cv_ros and camera_info python files must be added to the apriltag_ros scripts directory to publish the camera topics for apriltag_ros to use. Our launch file will find the packages we depend on and launch their respective launch files.