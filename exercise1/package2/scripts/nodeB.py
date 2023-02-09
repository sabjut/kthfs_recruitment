#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class NodeB:

    def __init__(self, q=0.15):
        rospy.init_node('nodeB', anonymous=False)
        rospy.Subscriber("/jut", Int32, self.callback)
        self.pub = rospy.Publisher('/kthfs/result', Int32, queue_size=10)
        self.q = q
        rospy.loginfo("nodeB initialized with q=%f" % q)

    def callback(self, data):
        new_data = data.data / self.q
        rospy.loginfo("received %d, sending %d" % (data.data, new_data))
        self.pub.publish(new_data)

if __name__ == '__main__':
    try:
        node = NodeB()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass