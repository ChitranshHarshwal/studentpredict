from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        '''
        -e . should not be read
        '''

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup (
name='studentPredict',
version = '0.0.1',
author='Chitti',
author_email='charshwal@yahoo.com', 
packages = find_packages(),
install_requires=get_requirements('requirements.txt')

)