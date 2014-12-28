import unittest
from packagefile.FoundFile import FoundFile
from packagefile.FileCollection import FileCollection

class TestFoundFile(unittest.TestCase):
    
    def test_FoundFileConstructor(self):
        self.assertRaises(IOError,FoundFile,'fileNotFound')
#        FileFromFoundFile = foundFile.getName()
#        self.assertEqual('fileNotFound', FileFromFoundFile)

class Test_FileCollection(unittest.TestCase):
    def test_FileCollection_Constructor(self):
        localFileCollection = FileCollection()
        localListOfFiles = localFileCollection.getListOfFiles()
        self.assertEqual(0, len(localListOfFiles), "New Object has a empty list")

if __name__ == '__main__':
    unittest.main()
        