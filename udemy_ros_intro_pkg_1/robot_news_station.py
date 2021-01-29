#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
# need to register all dependencies in package.xml!
from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        # String is the message type; robot_news is the topic on which we publish
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot news station has been started")

    def publish_news(self):
        msg = String()
        msg.data = "My news is cool"
        self.publisher_.publish(msg)

def main(args=None):
    # init ros2 comm
    rclpy.init(args=args)
    ## my code here
    node = RobotNewsStationNode()
    rclpy.spin(node)  # spin up node (blocks)
    # shutdown ros2 comm
    rclpy.shutdown()

if __name__ == "__main__":
    main()