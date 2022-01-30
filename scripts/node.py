import rospy
from sensor_msgs import LaserScan
from std_msgs import Float32
from std_msgs import UInt8

def __init__(self):
    rospy.init_node('scan_wrapper')
    self.ranges = [None] * 181
    self.pos = 0
    self.p_update = False

def rangeCallback(self, msg):
    self.range = msg.data
    self.r_update = True
    self.pub_s(self.r_update, self.p_update)

def posCallback(self, msg):
    self.pos = msg.data
    self.p_update = True
    self.pub_s(self.r_update, self.p_update)

def pub_s(r, p):
    if r and p:
        print('OK')
            


# topic list : range, pos
if __name__ == '__main__':
    pub = rospy.Publisher("/scan", LaserScan, queue_size= 10)
    r_sub = rospy.Subscriber("/range", Float32, rangeCallback)
    p_sub = rospy.Subscriber("/pos", UInt8, posCallback)
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass