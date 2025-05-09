# ======================================================================================================================
#
# IMPORTS
#
# ======================================================================================================================

import os
from typing import List

from setuptools import find_packages, setup

# ======================================================================================================================


def get_path_to_this_files_parent_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def get_path_to_requirements_txt_relative_to_this_file() -> str:
    return os.path.join(get_path_to_this_files_parent_dir(), "requirements.txt")


def load_required_packages_from_requirements_txt() -> List[str]:
    with open(get_path_to_requirements_txt_relative_to_this_file(), "r") as file:
        return [ln.strip() for ln in file.readlines()]


setup(
    # =====
    # Setup
    # =====
    name="batcherapp",
    # =================================
    # Actual packages, data and scripts
    # =================================
    packages=find_packages(),
    package_dir={"src": "src"},
    install_requires=load_required_packages_from_requirements_txt(),
)
