import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        # 创建发布者，消息队列大小为10
        self.publisher_ = self.create_publisher(Image, '/camera/rgb/image_raw', 10)
        # 每0.1秒回调一次（约10Hz）
        self.timer = self.create_timer(0.1, self.timer_callback)
        # 使用OpenCV打开默认相机
        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()
        self.get_logger().info('Camera publisher node has been started.')
    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
        # 将OpenCV图像转换为ROS Image消息，编码格式为 bgr8
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing camera image')
        else:
            self.get_logger().warning('Failed to read from camera')
    def destroy_node(self):
        self.cap.release()
        super().destroy_node()
    
def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()