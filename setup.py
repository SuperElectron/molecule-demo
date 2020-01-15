# setup.py
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='molecule-demo',
    version='0.1.0',
    description='Molecule Demo Setup',
    author='Matthew McCann',
    author_email='matmccann@gmail.com',
    url='https://github.com/SuperElectron/molecule-demo',
    install_requires=requirements,
    packages=find_packages()
)
