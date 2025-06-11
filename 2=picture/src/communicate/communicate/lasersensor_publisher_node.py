import rclpy 
from rclpy.node import Node
from std_msgs.msg import Float32 
import numpy as np

def main(args=None): 
    rclpy.init(args=args) # 初始化
    node = PublisherNode("lasersensor_publisher_node") # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy

class PublisherNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info(f"{name}Created!")
        self.publisher_ = self.create_publisher(Float32,"laserdata_topic",10)
        self.create_timer(1.0, self.timer_callback)
    
    def timer_callback(self):
        msg = Float32()
        msg.data = np.random.rand()
        self.publisher_.publish(msg)
        self.get_logger().info(f'{self.get_name()} publishing: {msg.data}')#日志输出

if __name__ == "__main__":
    main()