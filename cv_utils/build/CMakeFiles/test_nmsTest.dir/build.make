# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

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

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mdesnoyer/src/reefbot/ros/cv_utils

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mdesnoyer/src/reefbot/ros/cv_utils/build

# Utility rule file for test_nmsTest.

# Include the progress variables for this target.
include CMakeFiles/test_nmsTest.dir/progress.make

CMakeFiles/test_nmsTest: ../bin/nmsTest
	cd /home/mdesnoyer/src/reefbot/ros/cv_utils && /opt/ros/fuerte/share/rosunit/bin/rosunit --name=nmsTest --time-limit=60.0 /home/mdesnoyer/src/reefbot/ros/cv_utils/bin/nmsTest

test_nmsTest: CMakeFiles/test_nmsTest
test_nmsTest: CMakeFiles/test_nmsTest.dir/build.make
.PHONY : test_nmsTest

# Rule to build all files generated by this target.
CMakeFiles/test_nmsTest.dir/build: test_nmsTest
.PHONY : CMakeFiles/test_nmsTest.dir/build

CMakeFiles/test_nmsTest.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_nmsTest.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_nmsTest.dir/clean

CMakeFiles/test_nmsTest.dir/depend:
	cd /home/mdesnoyer/src/reefbot/ros/cv_utils/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mdesnoyer/src/reefbot/ros/cv_utils /home/mdesnoyer/src/reefbot/ros/cv_utils /home/mdesnoyer/src/reefbot/ros/cv_utils/build /home/mdesnoyer/src/reefbot/ros/cv_utils/build /home/mdesnoyer/src/reefbot/ros/cv_utils/build/CMakeFiles/test_nmsTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_nmsTest.dir/depend

