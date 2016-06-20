# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='git_cc',
    # version=version,
    description='Provides a bridge between git and ClearCase',
    long_description=readme,
    # author='P.C.J. Swinkels',
    # author_email='swinkels.pieter@yahoo.com',
    # url='home page of the project',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'gitcc=git_cc.gitcc:main',
        ],
    },
)
