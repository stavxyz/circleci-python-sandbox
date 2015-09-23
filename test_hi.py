
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
        
    def test_is_precisely_correct_version(self):
        
        toxenvname = 'TOX_%s' % os.environ['TOX_ENV_NAME'].upper()
        expected_version = os.environ[toxenvname]
        print('TOX ENV NAME: %s' % toxenvname)
        print('Expected version for tox env: %s' % expected_version) 
        actual = list(sys.version_info[:3])
        expected = [int(x) for x in expected_version.split('.')]
        self.assertEqual(actual, expected)

    def test_what_python(self):
        
        print('which python')
        subprocess.call('which python', stderr=subprocess.STDOUT, shell=True)
        print('type python')
        subprocess.call('type python', stderr=subprocess.STDOUT, shell=True)
        print('whereis python')
        subprocess.call('whereis python', stderr=subprocess.STDOUT, shell=True)
        print('module path')
        print(module_path())
        print('\n\nPYTHON VERSION')
        print('**************')
        print(sys.version)
        print('\n\n')


if __name__ == '__main__':

    unittest.main(verbosity=3)
