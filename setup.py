from setuptools import find_packages, setup

from typing import List



def get_requirements(file_path:str)->List[str] :
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        return requirements   



setup(
    name = "DiamondPricePrediction",
    version = "0.0.1",
    author = "Birjendra Kumar Shukla",
    author_email = "bshukla2236@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages= find_packages()
) 
