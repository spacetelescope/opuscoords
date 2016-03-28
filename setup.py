#!/usr/bin/env python
import recon.release
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, find_packages, Extension


version = recon.release.get_info()
recon.release.write_template(version, 'lib/opuscoords')

setup(
    name = 'opuscoords',
    version = version.pep386,
    author = 'Warren Hack',
    author_email = 'help@stsci.edu',
    description = 'Python Tools for OPUS Coordinate Conversions',
    url = 'https://github.com/spacetelescope/opuscoords',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'nose',
        'numpy',
        'scipy',
        'sphinx',
    ],

    package_dir = {
        '':'lib'
    },
    packages = find_packages('lib'),
    package_data = {
        '': ['SP_LICENSE']
    },
    ext_modules=[
        Extension('opuscoords.GCcoords',
            glob('src/*.c'),
            include_dirs=[np_include()]),
    ],
)
