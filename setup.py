from setuptools import setup, find_packages
from typing import List


#declaring varibales for setup functions
project_name = "housing-predictor"
version = "0.0.5"
author = "Liptika Dhal"
description = "This is a machine learning project of house price prediction"
#packages = ["housing"]
requirement_file_name = "requirements.txt"

def get_requirements_list()->List[str]:
    """this function is going to return a list of requirements mentioned in requirements.txt"""
    with open(requirement_file_name) as requirement_file:
        return requirement_file.readlines()

setup(
    name = project_name,
    version = version,
    author = author,
    description = description,
    packages = find_packages(),
    install_requires = get_requirements_list()


)