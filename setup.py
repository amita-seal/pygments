#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pygments
~~~~~~~~

Pygments is a syntax highlighting package written in Python.

It is a generic syntax highlighter suitable for use in code hosting, forums,
wikis or other applications that need to prettify source code.  Highlights
are:

* a wide range of over 300 languages and other text formats is supported
* special attention is paid to details, increasing quality by a fair amount
* support for new languages and formats are added easily
* a number of output formats, presently HTML, LaTeX, RTF, SVG, all image \
    formats that PIL supports and ANSI sequences
* it is usable as a command-line tool and as a library

:copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
"""

from setuptools import setup, find_packages

setup(
    name = 'Pygments',
    version = '2.5.2',
    url = 'http://pygments.org/',
    license = 'BSD License',
    author = 'Georg Brandl',
    author_email = 'georg@python.org',
    description = 'Pygments is a syntax highlighting package written in Python.',
    long_description = __doc__,
    keywords = 'syntax highlighting',
    packages = find_packages(exclude=['tests']),
    entry_points = {
        'console_scripts': ['pygmentize = pygments.cmdline:main'],
    },
    platforms = 'any',
    zip_safe = False,
    include_package_data = True,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Development Status :: 6 - Mature',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
)
