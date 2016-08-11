from distutils.core import setup, Extension
#from setuptools import setup, Extension
import platform
import numpy

include_dirs_numpy = [numpy.get_include()]
include_dirs_lapacke = ['../lapacke/include']
include_dirs = ['c/harmonic_h', 'c/anharmonic_h']
include_dirs += include_dirs_numpy + include_dirs_lapacke

extra_link_args = ['-lgomp',]

if platform.system() == 'Darwin':
    include_dirs += ['/opt/local/include',]
    extra_link_args += ['/opt/local/lib/libopenblas.a']
else:
    extra_link_args += ['-llapacke', '-llapack', '-lblas']

extension_phono4py = Extension(
    'anharmonic._phono4py',
    include_dirs=include_dirs,
    extra_compile_args=['-fopenmp'],
    extra_link_args=extra_link_args,
    sources=['c/_phono4py.c',
             'c/harmonic/dynmat.c',
             'c/harmonic/lapack_wrapper.c',
             'c/harmonic/phonoc_array.c',
             'c/harmonic/phonoc_utils.c',
             'c/anharmonic/phonon3/fc3.c',
             'c/anharmonic/phonon4/fc4.c',
             'c/anharmonic/phonon4/real_to_reciprocal.c',
             'c/anharmonic/phonon4/frequency_shift.c'])

setup(name='phono4py',
      version='0.8.0',
      description='This is the phono4py module.',
      author='Atsushi Togo',
      author_email='atz.togo@gmail.com',
      url='http://phonopy.sourceforge.net/',
      packages=['anharmonic',
                'anharmonic.phonon4'],
      scripts=['scripts/phono4py',],
      ext_modules=[extension_phono4py])
