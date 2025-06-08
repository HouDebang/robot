import rclpy
from rclpy.node import Node 
class MinimalNode(Node):
    def __init__(self):
        # 初始化节点，节点名称为'minimal_node'
        super().__init__('minimal_node')
        # 打印日志信息，表明节点已启动
        self.get_logger().info("Minimal node has started.")

def main(args=None):#入口函数
    # 初始化ROS2 客户端库
    rclpy.init(args=args)
    # 创建节点实例
    node = MinimalNode()
    try:
        #回调函数，进入循环，保持节点运行
        rclpy.spin(node)
    finally:
        # 销毁节点并关闭ROS2 客户端库
        node.destroy_node()
        rclpy.shutdown()
if __name__ == '__main__':
    main()