
from __future__ import print_function

import subprocess
import sys
import unittest


def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(unicode(sys.executable, encoding))
    return os.path.dirname(unicode(__file__, encoding))


class TestThings(unittest.TestCase):

    def test_the_answer(self):
    
        self.assertIs(42, 42)

    def test_what_python(self):
        
        print('which python')
        subprocess.call('which python', stderr=subprocess.STDOUT, shell=True)
        print('type python')
        subprocess.call('type python', stderr=subprocess.STDOUT, shell=True)
        print('whereis python')
        subprocess.call('whereis python', stderr=subprocess.STDOUT, shell=True)


if __name__ == '__main__':

    unittest.main(verbosity=3)
