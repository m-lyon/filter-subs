#!/usr/bin/env python3
'''setup.py, use this to install module'''
from os import path
from setuptools import setup

version = '1.2.0'
this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='subtitle-filter',
    version=version,
    description='Filter SDH entries and more from .srt files',
    author='Matt Lyon',
    author_email='matthewlyon18@gmail.com',
    url='https://github.com/mattlyon93/filter-subs',
    download_url='https://github.com/mattlyon93/filter-subs/archive/v{}.tar.gz'.format(version),
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    license='MIT License',
    packages=['subtitle_filter', 'subtitle_filter/libs'],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Topic :: Text Processing :: Filters',
        'Topic :: Multimedia :: Sound/Audio :: Speech'
    ],
    keywords=['subtitle', 'SDH', 'hard-of-hearing', 'filter', 'movie', 'tv'],
    scripts=['subtitle_filter/bin/filter-subtitles.py']
)
