
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from assnake_core_preprocessing.snake_module_setup import snake_module


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        snake_module.deploy_module()
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        snake_module.deploy_module()
        install.run(self)


setup(
    name='assnake-core-preprocessing',
    version='0.8.0',
    include_package_data=True,
    license='MIT',         
    description = 'Reads preprocessing module for assnake',   
    author = 'Dmitry Fedorov',                  
    author_email = 'fedorov.de@gmail.com',      
    url = 'https://github.com/ASSNAKE/assnake-core-preprocessing',   
    # download_url = 'https://github.com/ASSNAKE/assnake/archive/v0.8.8.tar.gz',    # I explain this later on
    keywords = ['ILLUMINA', 'NGS', 'METAGENOMIC', 'DATA'], 
    packages=find_packages(),
    entry_points = {
        'assnake.plugins': ['assnake-core-preprocessing = assnake_core_preprocessing.snake_module_setup:snake_module']
    },
    install_requires=[
        'assnake'
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)