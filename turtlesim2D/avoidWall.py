import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

currnt_pose = Pose()

def pose_callback(data):
    global currnt_pose
    currnt_pose = data
    
   

def move():
    global currnt_pose
    rospy.init_node("move", anonymous= True)
    velocity_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    
    rate = rospy.Rate(1)
    velocity = Twist()
    while not rospy.is_shutdown():
        global currnt_pose
        
        
        if currnt_pose.x > 9.0 or currnt_pose.x <1.0 or currnt_pose.y >10.0 or currnt_pose.y <1.0  :
            velocity.angular.z = 1.0
            velocity.linear.y = 0.4
            velocity.linear.x = 0.05
        else:
            velocity.linear.x = 0.5
            velocity.angular.z = 0.1
            
        
            
        velocity_pub.publish(velocity)
        
        
        rate.sleep()
    


try: 
    
    move()
except:
    pass
