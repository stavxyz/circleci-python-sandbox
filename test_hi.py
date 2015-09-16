
import unittest


class TestThings(unittest.TestCase):

    def test_the_answer(self):
    
        self.assertIs(42, 42)
        
        
if __name__ == '__main__':

    unittest.main()
