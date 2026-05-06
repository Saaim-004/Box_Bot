cmake_minimum_required(VERSION 3.8)
project(my_box_bot_gazebo)

# Enable extra compiler warnings for GCC and Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(my_box_bot_description REQUIRED)

# Testing dependencies
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# Install launch, worlds, and models directories
install(
  DIRECTORY
    launch
    worlds
    models
  DESTINATION
    share/${PROJECT_NAME}/
)

# Install executable scripts
install(PROGRAMS
  scripts/move_laser.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
