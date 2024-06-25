from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py','launch/gazebo.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/my_robot3.urdf','urdf/my_robot.urdf']),
        ('share/' + package_name + '/rviz', ['rviz/config.rviz','rviz/config3.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_robot_controller.my_first_node:main",
            "draw_cricle = my_robot_controller.draw_circle:main",
            "pose_subscriber = my_robot_controller.pose_subscriber:main",
            "turtle_controller = my_robot_controller.turtle_controller:main",
            "display_launch = my_robot_controller.display:main",
            "gazebo_launch = my_robot_controller.gazebo:main",
        ],
    },
)
