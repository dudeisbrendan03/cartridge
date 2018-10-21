#Details
VERSION = (0, 1)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Packaging and deployment tool'
__author__ = 'Brendan Jennings'
__author_email__ = 'jbrendan70@outlook.com'
__homepage__ = 'https://github.com/dudeisbrendan03/cartridge'
__license__ = 'BSD'

#Exceptions
from .core import incorrectUsage

#Classes
from .core import consoleDisplay

#Basic functions