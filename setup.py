from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''this function will return the list of requirements'''
    reqirments=[]
    with open(file_path) as file_object:
        reqirments=file_object.readlines()
        reqirments=[req.replace("\n", "") for req in reqirments]
    if HYPEN_E_DOT in reqirments:
        reqirments.remove(HYPEN_E_DOT)
        
    return reqirments
setup(
    name='ml_project',
    version=0.01,
    author='Biksham',
    author_email = "bixam.tarala@gmail.com",
    packages=find_packages(),   
    install_requires=get_requirements('requirements.txt')
)