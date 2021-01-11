
# Create a workspace

    mkdir ros2_first_test_ws
    cd ros2_first_test_ws
    mkdir src
    cd src

# Create a package    

    ros2 pkg create udemy_ros_intro_pkg_1 --build-type ament_python --dependencies rclpy
    
# Build the package

Only build the package from the workspace directory; otherwise the `colcon` directories `install` and `build` will be placed in the `src` folder:

    cd ros2_first_test_ws
    colcon build --packages-select udemy_ros_intro_pkg_1

Put the file `my_first_node.py` into `src/udemy_ros_intro_pkg_1/udemy_ros_intro_pkg_1` and build again. Then source `setup.bash` via

    source ros2_first_test_ws/install/setup.bash

# Run the node

The node name (executable) `py_node` is specified in the file `setup.py`:

    ros2 run udemy_ros_intro_pkg_1 py_node
