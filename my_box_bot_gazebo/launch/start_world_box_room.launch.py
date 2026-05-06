#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from ament_index_python.packages import (
    get_package_share_directory,
    get_package_prefix,
)
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory("gazebo_ros")
    pkg_box_bot_gazebo = get_package_share_directory("my_box_bot_gazebo")

    # Description package install directory
    description_package_name = "my_box_bot_description"
    install_dir = get_package_prefix(description_package_name)

    # Path to models inside my_box_bot_gazebo
    gazebo_models_path = os.path.join(pkg_box_bot_gazebo, "models")

    # Set GAZEBO_MODEL_PATH
    if "GAZEBO_MODEL_PATH" in os.environ:
        os.environ["GAZEBO_MODEL_PATH"] = (
            os.environ["GAZEBO_MODEL_PATH"]
            + ":"
            + install_dir
            + "/share"
            + ":"
            + gazebo_models_path
        )
    else:
        os.environ["GAZEBO_MODEL_PATH"] = (
            install_dir + "/share" + ":" + gazebo_models_path
        )

    # Set GAZEBO_PLUGIN_PATH
    if "GAZEBO_PLUGIN_PATH" in os.environ:
        os.environ["GAZEBO_PLUGIN_PATH"] = (
            os.environ["GAZEBO_PLUGIN_PATH"] + ":" + install_dir + "/lib"
        )
    else:
        os.environ["GAZEBO_PLUGIN_PATH"] = install_dir + "/lib"

    print("GAZEBO MODELS PATH==" + str(os.environ["GAZEBO_MODEL_PATH"]))
    print("GAZEBO PLUGINS PATH==" + str(os.environ["GAZEBO_PLUGIN_PATH"]))

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, "launch", "gazebo.launch.py"),
        )
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "world",
                default_value=[
                    os.path.join(pkg_box_bot_gazebo, "worlds", "room.world"),
                    "",
                ],
                description="SDF world file",
            ),
            gazebo,
        ]
    )
