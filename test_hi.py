
from __future__ import print_function

import os
import subprocess
import sys
import unittest

try:
    unicode
except NameError:
    unicode = str
    
def touni(s, enc='utf8', err='strict'):
    if isinstance(s, bytes):
        return s.decode(enc, err)
    else:
        return unicode(s or ("" if s is None else s))


def we_are_frozen():
    # All of the modules are built-in to the interpreter
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(touni(sys.executable, enc=encoding))
    return os.path.dirname(touni(__file__, enc=encoding))


class TestThings(unittest.TestCase):

    def test_the_answer(self):
    
        self.assertEqual(42, 42)

    def test_what_python(self):
        
        print('which python')
        subprocess.call('which python', stderr=subprocess.STDOUT, shell=True)
        print('type python')
        subprocess.call('type python', stderr=subprocess.STDOUT, shell=True)
        print('whereis python')
        subprocess.call('whereis python', stderr=subprocess.STDOUT, shell=True)
        print('module path')
        print(module_path())


if __name__ == '__main__':

    unittest.main(verbosity=3)
