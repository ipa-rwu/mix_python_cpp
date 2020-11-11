cmake_minimum_required(VERSION 3.5)
project(mix_python_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)

# Install the python module for this package
ament_python_install_package(action_client)


add_executable(action_server_member_functions src/minimal_action_server/member_functions.cpp)
ament_target_dependencies(action_server_member_functions
  "rclcpp"
  "rclcpp_action"
  "example_interfaces")

add_executable(action_server_not_composable src/minimal_action_server/not_composable.cpp)
ament_target_dependencies(action_server_not_composable
  "rclcpp"
  "rclcpp_action"
  "example_interfaces")

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(TARGETS
  action_server_not_composable
  action_server_member_functions
  DESTINATION lib/${PROJECT_NAME})

# Install python scripts
install(
  PROGRAMS scripts/client_execution.py
DESTINATION lib/${PROJECT_NAME}
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
