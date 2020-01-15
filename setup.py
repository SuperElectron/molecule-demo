# setup.py
from setuptools import setup, find_packages

setup(
    name='fibonacci',
    version='0.1.0',
    description='Molecule Demo Setup',
    author='Matthew McCann',
    author_email='matmccann@gmail.com',
    url='https://gitlab.com/matmccann/fibonacci',
    packages=find_packages(exclude=('tests'))
)
