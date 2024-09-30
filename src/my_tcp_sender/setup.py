# from setuptools import setup

# package_name = 'my_tcp_sender'

# setup(
#     name=package_name,
#     version='0.0.1',
#     packages=[package_name],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='samar',
#     maintainer_email='samar@example.com',
#     description='A ROS 2 package to send messages via TCP',
#     license='License Type',
#     entry_points={
#         'console_scripts': [
#             'tcp_sender_node = my_tcp_sender.tcp_sender_node:main',
#             'temp_control_node = my_tcp_sender.temp_control_node:main',
#             'turtle_control_node = my_tcp_sender.turtle_control_node:main',
#         ],
#     },
# )
from setuptools import setup

package_name = 'my_tcp_sender'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samar',
    maintainer_email='samar@example.com',
    description='A package for TCP communication between FiPy and ROS2 nodes',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           # 'temp_control_node = my_tcp_sender.temp_control_node:main',
            'tcp_sender_node = my_tcp_sender.tcp_sender_node:main',
        ],
    },
)

