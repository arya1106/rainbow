#!/usr/bin/env python
from setuptools import setup, Extension
from os.path import join

setup(
    packages=['rainbow'],
    py_modules=['rainbow.__init__'],
    ext_modules=[Extension('rainbow._rainbow', [join('rainbow', '_rainbow.c')])],
)