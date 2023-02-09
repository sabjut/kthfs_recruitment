#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class NodeA:

    def __init__(self, k=1, n=4):
        rospy.init_node('nodeA', anonymous=False)
        self.pub = rospy.Publisher('/jut', Int32, queue_size=10)
        self.k = k
        self.n = n
        rospy.loginfo("nodeA initialized with k=%d, n=%d" % (k,n))

    def babble(self):
        rate = rospy.Rate(20) # 20 Hz
        while not rospy.is_shutdown():
            self.pub.publish(self.k)
            rospy.loginfo("publishing %d" % (self.k))
            self.k += self.n
            rate.sleep()

if __name__ == '__main__':
    try:
        n = NodeA()
        n.babble()
    except rospy.ROSInterruptException:
        pass