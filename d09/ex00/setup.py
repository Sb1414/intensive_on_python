from distutils.core import setup, Extension

# определение модуля и его методов
module = Extension('calculator', sources=['calculator.c'])

# конфигурация сборки и установки модуля
setup(
    name='calculator',
    version='1.0',
    description='Simple calculator module',
    ext_modules=[module]
)

# python setup.py install
