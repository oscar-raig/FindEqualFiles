import unittest
from packagefile.FoundFile import FoundFile
from packagefile.FileCollection import FileCollection

class TestFoundFile(unittest.TestCase):
    
    def test_FoundFileConstructor(self):
        self.assertRaises(IOError,FoundFile,'fileNotFound',True)
#        FileFromFoundFile = foundFile.getName()
#        self.assertEqual('fileNotFound', FileFromFoundFile)

class Test_FileCollection(unittest.TestCase):
    
    def test_FileCollection_Constructor(self):
        localFileCollection = FileCollection()
        localListOfFiles = localFileCollection.getListOfFiles()
        self.assertEqual(0, len(localListOfFiles), "New Object has a empty list")
        
    def test_SetListOfFiles(self):
        listOfFiles = []
        firstFile = FoundFile("path1/paht1")
        listOfFiles.append(firstFile)
        secondFile = FoundFile("path2/paht2")
        listOfFiles.append(secondFile)
        fileCollectionForTest = FileCollection()
        fileCollectionForTest.setListOfFiles(listOfFiles)
        self.assertEquals(2,len( fileCollectionForTest.getListOfFiles()),"Two files")
        
    def test_GetNameFromPath(self):     
        self.assertEquals(FileCollection().getNameOfFileFromPath("test/test.txt"),"test.txt")

    def test_FileIsInTheList(self):
        listOfReapatedFiles =[]
        fileFound = FoundFile("file1")
        listOfReapatedFiles.append(fileFound)
        theFileIsInTheListShouldbeTrue = FileCollection().FileIsInTheList(listOfReapatedFiles,"file1")
        self.assertTrue(theFileIsInTheListShouldbeTrue,"This file shold be" )
        
    def test_TwoFilesWithSameNameX2AndOneWithDifferentOneShouldReturnAlistWithTwo(self):
        listOfFiles =[]
        File1 = FoundFile("file1")
        File1.setDirectory("directory1")
        listOfFiles.append(File1)
        
        File2 = FoundFile("file1")
        File2.setDirectory("directory2")
        listOfFiles.append(File2)
        
        File3 = FoundFile("file2")
        File3.setDirectory("directory3")
        listOfFiles.append(File3)
        File4 = FoundFile("file2")
        listOfFiles.append(File4)
        File5 = FoundFile("file3")
        listOfFiles.append(File5)

       
        
        localFileCollection = FileCollection()
        localFileCollection.setListOfFiles(listOfFiles)
        localFileCollection.PrintFiles()
        listOfFilesWithSameName = localFileCollection.getFilesWithSameName()
           
        self.assertEqual(2,len( listOfFilesWithSameName ),"5 files in the list, 2 repeated" )
         
        numberIteration = 0
        for itemFileWithSameName in listOfFilesWithSameName:
            if numberIteration == 0:
                self.assertTrue(itemFileWithSameName.getName() == "file1")
                listOfDirectories = itemFileWithSameName.getDirectoryList()
                self.assertEqual(2,len( listOfDirectories ),"file1 has two directories" )
            elif numberIteration == 1:
                self.assertTrue(itemFileWithSameName.getName() == "file2")
            numberIteration = numberIteration + 1

        
        
if __name__ == '__main__':
    unittest.main()
        