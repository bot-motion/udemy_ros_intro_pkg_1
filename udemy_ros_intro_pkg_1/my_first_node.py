#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello ROS2")


def main(args=None):
    # init ros2 comm
    rclpy.init(args=args)
    ## my code here
    node = MyNode()
    rclpy.spin(node)  # spin up node (blocks)
    # shutdown ros2 comm
    rclpy.shutdown()

if __name__ == "__main__":
    main()