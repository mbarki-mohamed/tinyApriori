#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from TinyApriori import __version__

# Current version
VERSION = __version__

setup(
    name='tinyApriori',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # No dependencies required
    ],
    author='Mohamed Mbarki',
    author_email='mbarki.mmed@gmail.com',
    description='A tiny python implementation of the Apriori algorithm for frequent itemset mining',
    url='https://github.com/mbarki-mohamed/tinyApriori',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
)