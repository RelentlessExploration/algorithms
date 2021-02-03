import importlib_resources as _resources
try:
    from configparser import ConfigParser as _ConfigParser
except ImportError:  # Python 2
    from ConfigParser import ConfigParser as _ConfigParser

__version__ = "1.2.0"
_cfg = _ConfigParser()
