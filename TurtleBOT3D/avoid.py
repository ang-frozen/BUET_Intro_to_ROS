#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance:
    def __init__(self):
        rospy.init_node('obstacle_avoidance', anonymous=True)

        # Publisher to control the TurtleBot
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Subscriber to LaserScan data
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        self.move_cmd = Twist()
        rospy.spin()

    def laser_callback(self, data):
        # Check distances in front of the robot
        front = min(min(data.ranges[0:30]), min(data.ranges[330:359]))
        left = min(data.ranges[30:90])
        right = min(data.ranges[270:330])

        rospy.loginfo(f"Front: {front}, Left: {left}, Right: {right}")

        # Threshold for obstacle detection
        threshold = 0.5

        # Obstacle avoidance logic
        if front < threshold:
            # Obstacle ahead, stop and turn
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = 0.5 if left > right else -0.5
        else:
            # Path clear, move forward
            self.move_cmd.linear.x = 0.2
            self.move_cmd.angular.z = 0.0

        self.cmd_pub.publish(self.move_cmd)

if __name__ == '__main__':
    try:
        ObstacleAvoidance()
    except rospy.ROSInterruptException:
        pass
