
# Create a workspace

    mkdir ros2_first_test_ws
    cd ros2_first_test_ws
    mkdir src
    cd src

# Create a package    

    ros2 pkg create udemy_ros_intro_pkg_1 --build-type ament_python --dependencies rclpy
    
# Build the package

    cd ros2_first_test_ws
    colcon build --packages-select udemy_ros_intro_pkg_1

Put the file `my_first_node.py` into `src/udemy_ros_intro_pkg_1/udemy_ros_intro_pkg_1` and build again. Then source the `setup.bash` via

    source ros2_first_test_ws/install/setup.bash

# Run the node

    ros2 run udemy_ros_intro_pkg_1 py_node

