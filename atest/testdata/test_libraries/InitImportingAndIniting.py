from __future__ import print_function

from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


class Importing(object):

    def __init__(self):
        BuiltIn().import_library('String')

    def kw_from_lib_with_importing_init(self):
        print('Keyword from library with importing __init__.')


class Initting(object):

    def __init__(self):
        # This initializes the accesses library.
        self.lib = BuiltIn().get_library_instance('InitImportingAndIniting.Initted')

    def kw_from_lib_with_initting_init(self):
        logger.info('Keyword from library with initting __init__.')
        self.lib.kw_from_lib_initted_by_init()


class Initted(object):

    def __init__(self, id):
        self.id = id

    def kw_from_lib_initted_by_init(self):
        print('Keyword from library initted by __init__ (id: %s).' % self.id)
