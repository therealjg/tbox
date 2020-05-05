#!/usr/bin/python

from setuptools import setup
setup(
    name="tbox",
    version="1.0",
    py_modules=['start'],
    install_requires=[
        'Click',
	'dnspython',
    ],
    entry_points='''
        [console_scripts]
        tbox=main:main
    ''',
)
