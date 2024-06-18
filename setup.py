"""
 * File: setup.py
 * Description: Setup script for pyLogger package
 *           
 * Author: 0x6D76
 * Copyright (c) 2024 0x6D76 (0x6D76@proton.me)
"""

from setuptools import setup, find_packages

setup (
    name = 'pyLogger',
    version = '0.1.0',
    packages = find_packages (),
    install_requires = [],
    entry_points = {
        'console_scripts' : [
            'pyLogger = pyLogger.logger:main',
        ],
    },
    author = '0x6D76',
    author_email = '0x6D76@proton.me',
    description = 'Custom logger package based on Python',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url='https://github.com/0x6D76/pyLogger',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
