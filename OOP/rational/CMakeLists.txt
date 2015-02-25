#declare the project
#CXX means c++
project(rational CXX)

#require make version 2.8 minimum
cmake_minimum_required(VERSION 2.8)

#enable compilation with c++11
#turn on all warnings and make them errors
set(CMAKE_CXX_FLAGS "-Wall -Werror -std=c++11")

#executable to be built from source files
add_executable(rational main.cpp rational.cpp)
