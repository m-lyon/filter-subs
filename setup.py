#!/usr/bin/env python3
'''setup.py, use this to install module'''
from setuptools import setup

setup(
    name='subtitle-filter',
    version='1.0.0',
    description='Filter SDH entries and more from .srt files',
    author='Matt Lyon',
    author_email='matthewlyon18@gmail.com',
    python_requires='>=3.6',
    license='MIT License',
    packages=['subtitle_filter', 'subtitle_filter/lib'],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    scripts=['subtitle_filter/bin/filter-subtitles.py']
)
