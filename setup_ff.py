from distutils.core import setup, Extension
#from setuptools import setup, Extension
import numpy
import platform

include_dirs_numpy = [numpy.get_include()]
include_dirs_lapacke = ['../lapacke/include']
include_dirs = ['c/harmonic_h', 'c/anharmonic_h']
include_dirs += include_dirs_numpy + include_dirs_lapacke
extra_link_args = ['-lgomp',]

if platform.system() == 'Darwin':
    include_dirs += ['/opt/local/include']
    extra_link_args += ['/opt/local/lib/libopenblas.a']
else:
    extra_link_args += ['-llapacke', '-llapack', '-lblas']

extension_forcefit = Extension(
    'anharmonic._forcefit',
    include_dirs=include_dirs,
    extra_compile_args=['-fopenmp'],
    extra_link_args=extra_link_args,
    sources=['c/_forcefit.c',
             'c/harmonic/lapack_wrapper.c'])

setup(name='force-fit',
      version='0.8.0',
      description='This is the force-fit module.',
      author='Atsushi Togo',
      author_email='atz.togo@gmail.com',
      url='http://phonopy.sourceforge.net/',
      packages=['anharmonic',
                'anharmonic.force_fit'],
      scripts=['scripts/force-fit',],
      ext_modules=[extension_forcefit])
