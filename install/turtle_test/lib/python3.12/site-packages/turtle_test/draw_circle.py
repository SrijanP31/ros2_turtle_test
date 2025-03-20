import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 

class Circle(Node):
    
    def __init__(self):
        super().__init__("circle")
        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.timer_val = 0.5
        self.timer = self.create_timer(self.timer_val,self.circle_draw)
        self.velocity = Twist()
        self.radius = 1

        self.velocity.angular.x = 0.0
        self.velocity.angular.y = 0.0
        self.velocity.linear.y = 0.0
        self.velocity.linear.z = 0.0

    def circle_draw(self):

        self.velocity.angular.z = 2*3.1415/self.timer_val
        self.velocity.linear.x = (2*3.1415*self.radius)/self.timer_val
        self.radius += 0.1

        self.pub.publish(self.velocity)
        

def main(args=None):
    rclpy.init(args=args)
    circle = Circle()
    rclpy.spin(circle)

if __name__ == "__main__":
    main()