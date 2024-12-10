#!/usr/bin/env python3
import rospy # Library import
from std_msgs.msg import String # message

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) # define publisher
    rospy.init_node('talker', anonymous=True) # initialize the node
    rate = rospy.Rate(1)  # 1 Hz # define talking rate
    while not rospy.is_shutdown(): # setup an infinite loop
        hello_str = "Hello ROS! %s" % rospy.get_time()
        rospy.loginfo(hello_str) # Equivalent to print() function of python
        pub.publish(hello_str) # publish
        rate.sleep() # use the rate

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
