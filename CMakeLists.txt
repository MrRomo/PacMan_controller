cmake_minimum_required(VERSION 2.8.3)
project(pacman-controller)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  roslib
  rospy
  pacman
)

catkin_package(
  CATKIN_DEPENDS roscpp roslib rospy pacman
)

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

set(pacman_controller_SRCS
  src/pacman_controller_cpp.cpp
)

set(pacman_controller_HDRS
  #Add here header C++ files, if any
  #include/pacman_controller/header.h
)

set(pacman_controller2_SRCS
  src/pacman_controller2_cpp.cpp
)

set(pacman_controller2_HDRS
  #Add here header C++ files, if any
  #include/pacman_controller/header.h
)

add_executable(pacman_controller_cpp ${pacman_controller_SRCS} ${pacman_controller_HDRS})
target_link_libraries(pacman_controller_cpp ${catkin_LIBRARIES})
add_dependencies(pacman_controller_cpp ${catkin_EXPORTED_TARGETS})

add_executable(pacman_controller2_cpp ${pacman_controller2_SRCS} ${pacman_controller2_HDRS})
target_link_libraries(pacman_controller2_cpp ${catkin_LIBRARIES})
add_dependencies(pacman_controller2_cpp ${catkin_EXPORTED_TARGETS})
