import os
import launch
import launch_ros
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, Command

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='my_robot_controller').find('my_robot_controller')
    default_model_path = os.path.join(pkg_share, 'urdf/my_robot.urdf')

    # Declare the robot_state_publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}],
        output='screen'
    )

    # Declare the joint_state_publisher_gui node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # Declare the spawn_entity node
    spawn_entity_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'my_robot', '-topic', 'robot_description'],
        output='screen'
    )

    # Launch description with all actions and nodes
    return LaunchDescription([
        DeclareLaunchArgument(
            name='model',
            default_value=default_model_path,
            description='Absolute path to robot urdf file'
        ),
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        spawn_entity_node
    ])

def main():
    ld = generate_launch_description()
    launch_service = launch.LaunchService()
    launch_service.include_launch_description(ld)
    return launch_service.run()

if __name__ == '__main__':
    main()
