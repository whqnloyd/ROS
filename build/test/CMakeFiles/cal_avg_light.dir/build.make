# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/husarion/ROS/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/husarion/ROS/build

# Include any dependencies generated for this target.
include test/CMakeFiles/cal_avg_light.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/cal_avg_light.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/cal_avg_light.dir/flags.make

test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o: test/CMakeFiles/cal_avg_light.dir/flags.make
test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o: /home/husarion/ROS/src/test/src/cal_avg_light.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/husarion/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o"
	cd /home/husarion/ROS/build/test && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o -c /home/husarion/ROS/src/test/src/cal_avg_light.cpp

test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.i"
	cd /home/husarion/ROS/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/husarion/ROS/src/test/src/cal_avg_light.cpp > CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.i

test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.s"
	cd /home/husarion/ROS/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/husarion/ROS/src/test/src/cal_avg_light.cpp -o CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.s

test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.requires:

.PHONY : test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.requires

test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.provides: test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.requires
	$(MAKE) -f test/CMakeFiles/cal_avg_light.dir/build.make test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.provides.build
.PHONY : test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.provides

test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.provides.build: test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o


# Object files for target cal_avg_light
cal_avg_light_OBJECTS = \
"CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o"

# External object files for target cal_avg_light
cal_avg_light_EXTERNAL_OBJECTS =

/home/husarion/ROS/devel/lib/test/cal_avg_light: test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o
/home/husarion/ROS/devel/lib/test/cal_avg_light: test/CMakeFiles/cal_avg_light.dir/build.make
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/libroscpp.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_signals.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/librosconsole.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/liblog4cxx.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_regex.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/librostime.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /opt/ros/kinetic/lib/libcpp_common.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_system.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_thread.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_chrono.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_date_time.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libboost_atomic.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libpthread.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: /usr/lib/arm-linux-gnueabihf/libconsole_bridge.so
/home/husarion/ROS/devel/lib/test/cal_avg_light: test/CMakeFiles/cal_avg_light.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/husarion/ROS/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/husarion/ROS/devel/lib/test/cal_avg_light"
	cd /home/husarion/ROS/build/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cal_avg_light.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/cal_avg_light.dir/build: /home/husarion/ROS/devel/lib/test/cal_avg_light

.PHONY : test/CMakeFiles/cal_avg_light.dir/build

test/CMakeFiles/cal_avg_light.dir/requires: test/CMakeFiles/cal_avg_light.dir/src/cal_avg_light.cpp.o.requires

.PHONY : test/CMakeFiles/cal_avg_light.dir/requires

test/CMakeFiles/cal_avg_light.dir/clean:
	cd /home/husarion/ROS/build/test && $(CMAKE_COMMAND) -P CMakeFiles/cal_avg_light.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/cal_avg_light.dir/clean

test/CMakeFiles/cal_avg_light.dir/depend:
	cd /home/husarion/ROS/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/husarion/ROS/src /home/husarion/ROS/src/test /home/husarion/ROS/build /home/husarion/ROS/build/test /home/husarion/ROS/build/test/CMakeFiles/cal_avg_light.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/cal_avg_light.dir/depend

