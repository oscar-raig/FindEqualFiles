import unittest

from FileController import FileController

class TestFilecontroller(unittest.TestCase):

	 def test_FileController_Constructor(self):
        	localFileCollection = FileController(None)
        	self.assertFalse(None, localFileCollection)


        
if __name__ == '__main__':
    unittest.main()        	