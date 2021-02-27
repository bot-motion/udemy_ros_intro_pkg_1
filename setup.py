from setuptools import setup

package_name = 'udemy_ros_intro_pkg_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='matthias',
    maintainer_email='botmotion@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # executable = package.file_name:main
            "py_node=udemy_ros_intro_pkg_1.my_first_node:main",
            "robot_news_station=udemy_ros_intro_pkg_1.robot_news_station:main",
            "smartphone=udemy_ros_intro_pkg_1.smartphone:main",
            "hw_status_publisher=udemy_ros_intro_pkg_1.hw_status_publisher:main"
        ],
    },
)
