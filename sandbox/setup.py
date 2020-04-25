from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("matrix.pyx"), install_requires=['Cython', 'numpy']
)