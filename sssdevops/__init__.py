"""
Main init file for the sssdevops package
"""

from .sssdevops import *    #import all functions from ./sssdevops.py 
from .listtools import *    #import all functions from ./listtools.py 


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
