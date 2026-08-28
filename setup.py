from setuptools import setup, Extension
import numpy

NAME = 'cellstates'
VERSION = '0.1'
DESCR = 'Module for finding gene expression states in scRNAseq data'
REQUIRES = ['numpy', 'pandas', 'matplotlib']

AUTHOR = 'Pascal Grobecker'
EMAIL = 'pascal.grobecker@unibas.ch'

PACKAGES = ['cellstates']


try:
    from Cython.Build import cythonize
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "Cython is required to build cellstates. Install it with "
        "`pip install Cython` (or `conda install cython`) and try again."
    ) from exc

EXTENSIONS = [Extension("cellstates.cluster",
                        ["cellstates/cluster.pyx"],
                        include_dirs=[numpy.get_include(), '.'],
                        extra_compile_args=['-fopenmp'],
                        extra_link_args=['-fopenmp'],
                        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]),
              Extension("cellstates.chelpers",
                        ["cellstates/chelpers.pyx"],
                        include_dirs=[numpy.get_include(), '.'],
                        extra_compile_args=['-fopenmp'],
                        extra_link_args=['-fopenmp'],
                        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]
                        )
              ]

EXTENSIONS = cythonize(EXTENSIONS,
                       compiler_directives={'language_level': 3})

if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        description=DESCR,
        author=AUTHOR,
        author_email=EMAIL,
        install_requires=REQUIRES,
        packages=PACKAGES,
        ext_modules=EXTENSIONS
    )
