""" Variables that never change """

__version__ = '0.0.1a'
__author__ = 'Seniatical & Daftscientist'
__license__ = 'MIT License'

USER_AGENT = 'PyPtero <https://github.com/Rapi-Dev/PyPtero> [Version {}]'.format(__version__)
USE_SSL = {True: 'https', False: 'http'}
REQUEST_TYPES = ('DELETE', 'GET', 'POST', 'PATCH')