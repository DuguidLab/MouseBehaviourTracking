#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name="mouse_behaviour_tracking",
    version="0.0.1",
    package_dir={'': 'src'},
    packages=find_packages('./src'),

    install_requires=[
        'docutils>=0.3',
        'Cython',
        'kivy',
    ],

    author="Constantinos Eleftheriou, Alex Harston",
    author_email="Contantinos.Eleftheriou@ed.ac.uk, alex@harston.io",
    description="Mouse Behaviour Tracking - a Kivy project",
    license="MIT",
)
