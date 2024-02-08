cmake_minimum_required(VERSION 3.16)
project(keyboard_control)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)

install(PROGRAMS
    nodes/ackermann_teleop_node.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()