import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import socket

class TurtleControlNode(Node):
    def __init__(self):
        super().__init__('turtle_control_node')

        # Configuration du serveur TCP pour recevoir les commandes du FiPy
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = '10.89.2.196'  # Adresse IP du FiPy
        self.server_port = 1234  # Port du serveur TCP
        
        self.server_socket.bind((self.server_ip, self.server_port))
        self.server_socket.listen(1)
        self.get_logger().info(f'Serveur TCP en écoute sur {self.server_ip}:{self.server_port}')
        self.conn, _ = self.server_socket.accept()
        self.get_logger().info('Connexion acceptée')

        # Création d'un publisher pour les commandes de mouvement
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Timer pour traiter les commandes du FiPy
        self.create_timer(1.0, self.process_fipy_commands)

    def process_fipy_commands(self):
        try:
            data = self.conn.recv(1024).decode()
            if data:
                self.get_logger().info('Commande reçue du FiPy: ' + data)
                if data.startswith('MOVE'):
                    _, linear_velocity, angular_velocity = data.split()
                    twist_msg = Twist()
                    twist_msg.linear.x = float(linear_velocity)
                    twist_msg.angular.z = float(angular_velocity)
                    self.cmd_vel_publisher.publish(twist_msg)
                    self.get_logger().info(f'Commande publiée: linear.x={twist_msg.linear.x}, angular.z={twist_msg.angular.z}')
        except Exception as e:
            self.get_logger().error(f'Échec de la réception de données: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
