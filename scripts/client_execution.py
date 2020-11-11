#!/usr/bin/env python3

from action_client.client import MinimalActionClient
import rclpy


def main(args=None):
    rclpy.init(args=args)

    action_client = MinimalActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
