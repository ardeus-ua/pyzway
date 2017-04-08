#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyzway',
    version='0.1',
    description='Python for Z-Way',
    author='Jakob Schlyter',
    author_email='jakob@kirei.se',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    url='https://github.com/jschlyter/pyzway',
    packages=['zway'],
    install_requires=[
        'requests',
        'setuptools',
    ]
)
