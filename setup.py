#!/usr/bin/env python3
import os.path
from setuptools import setup, find_packages
from glob import glob

setup(
    name='pathfinder_editor',
    author='craftsmanadam',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points='''
            [console_scripts]
            pathfinder_editor=editor.pathfinder_editor:pathfinder_editor
    '''
)
