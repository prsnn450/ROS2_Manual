cmake_minimum_required(VERSION 3.8)
project(kuka_arm_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(trajectory_msgs REQUIRED)
find_package(moveit_ros_planning REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_core REQUIRED)
find_package(graph_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

set(Moveit_includes
  rclcpp
  moveit_ros_planning
  moveit_ros_planning_interface
  moveit_core
  graph_msgs
)

include_directories(include)

# Add executables for the nodes
add_executable(jtc_node src/joint_trajectory_controller.cpp)
ament_target_dependencies(jtc_node rclcpp trajectory_msgs)

add_executable(gripper_node src/gripper_controller.cpp)
ament_target_dependencies(gripper_node rclcpp trajectory_msgs)

add_executable(moveit_drive src/motion_drive_moveit.cpp)
ament_target_dependencies(moveit_drive ${Moveit_includes})

add_executable(moveit_action_drive_server src/robot_action.cpp)
ament_target_dependencies(moveit_drive ${Moveit_includes} geometry_msgs)

# Install targets
install(TARGETS
  jtc_node
  gripper_node
  moveit_drive
  moveit_action_drive_server
  DESTINATION lib/${PROJECT_NAME}
)

# Install other necessary files
install(DIRECTORY src urdf meshes config launch models worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
