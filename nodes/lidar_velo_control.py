import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def scan_callback(self, msg):
        # Assuming a 360-degree LiDAR, front is typically at 0 degrees
        front_index = len(msg.ranges) // 2
        
        # We assume the front 60 degrees (-30 to +30 degrees) for obstacle detection
        angle_range = 30  # Degrees
        start_index = front_index - angle_range
        end_index = front_index + angle_range
        
        min_distance = min(msg.ranges[start_index:end_index])
        
        if min_distance < 0.5:  # 0.5 meters (50 cm)
            self.send_signal()

    def send_signal(self):
        self.get_logger().info('Obstacle detected within 50 cm in the front area!')

def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)

    lidar_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
