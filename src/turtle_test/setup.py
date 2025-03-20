from setuptools import find_packages, setup

package_name = 'turtle_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Srijan Prasanna',
    maintainer_email='pn.srijan@gmail.com',
    description='Playing around with ROS2 using turtlesim',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = turtle_test.my_node:main',
            'circle = turtle_test.draw_circle:main'
        ],
    },
)
