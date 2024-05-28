#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        self.pub_vel = self.create_publisher(Float64, '/commands/motor/speed', 1)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def scan_callback(self, msg):
        min_distance = min(msg.ranges[0:10])

        vel_msg = Float64()
        vel_msg.data = 0.0
        print("Min Distance: " + str(min_distance))
        
        if min_distance > 0.3:
            vel_msg.data = 1500.0
        else:
            vel_msg.data = 0.0

        

        self.pub_vel.publish(vel_msg) 

        


def main(args=None):
    print("Node gestartet")
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)

    lidar_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
