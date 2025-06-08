from setuptools import find_packages, setup

package_name = 'lasersensor_pkg'

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
    maintainer='ws',
    maintainer_email='ws@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker=lasersensor_pkg.lasersensor_publisher_node:main',
            'listener=lasersensor_pkg.lasersensor_subscriber_node:main'
        ],
    },
)
