"""
Main init file for the sssdevops package
"""

from .list_tools import *    #import all functions from ./list_tools.py 
from .more_list_tools import *    #import all functions from ./more_list_tools.py 


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
