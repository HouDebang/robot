import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        # 订阅 /camera/rgb/image_raw 话题，队列大小10
        self.subscription = self.create_subscription(
            Image,
            '/camera/rgb/image_raw',
            self.listener_callback,
            10)
        self.bridge = CvBridge()
        self.get_logger().info('Image subscriber node has been started.')
    def listener_callback(self, msg):
        try:
        # 将ROS Image消息转换为OpenCV图像
            cv_image = self.bridge.imgmsg_to_cv2(msg, 
            desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f'Error converting image: {e}')
            return
        # 显示图像
        cv2.imshow("Camera Feed", cv_image)
        cv2.waitKey(1)
def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()