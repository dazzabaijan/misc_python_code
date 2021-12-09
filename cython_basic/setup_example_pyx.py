from Cython.Build.Dependencies import cythonize
from distutils.core import setup
from Cython.Build import Cythonize

setup(ext_modules=cythonize('example.pyx'))