from setuptools import setup
from Cython.Build import cythonize

setup(
    name='matrix',
    version='1.0',
    ext_modules=cythonize("multiply.pyx"),
)

# python setup.py build_ext --inplace
# python test_mul_perf.py