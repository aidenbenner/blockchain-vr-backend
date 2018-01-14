cmake_minimum_required(VERSION 3.9)
project(blockchain_parser)

set(CMAKE_CXX_STANDARD 17)

add_library(stdc++fs UNKNOWN IMPORTED)
set_property(TARGET stdc++fs PROPERTY IMPORTED_LOCATION "/usr/lib/libstdc++fs.a")
add_executable(blockchain_parser main.cpp transaction.h block.h)
target_link_libraries(${PROJECT_NAME} stdc++fs)