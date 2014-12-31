import os
import os.path
import glob
from logging import root
from packagefile.FoundFile import FoundFile

class FileCollection:
    ListOfFiles = []
    def __init__(self):
        print 'Init'
    
    def getListOfFiles (self):
        return self.ListOfFiles
    
    def setListOfFiles (self,newListOfFiles):
        self.ListOfFiles = newListOfFiles
    
    def ChooseFileAndAddToList(self,Folder,listOfFiles):
        for fileInDir in listOfFiles:
            if fileInDir.endswith(".txt"):
#                print(os.path.join(root, file))
                fileToAdd = FoundFile(os.path.join(Folder, fileInDir))
                self.ListOfFiles.append(fileToAdd)    
        
    def FindFiles(self):
        directoryToSearch = "/Users/oscarraigcolon/Arrel/git/rebuild-graph/"
        print "Directory To search " ,directoryToSearch

        for root, dirs, files in os.walk(directoryToSearch):
#            print root
            self.ChooseFileAndAddToList( root,files )
    def getNameOfFileFromPath(self,FileWithPath):
        return os.path.basename(FileWithPath)
    
    def FileIsInTheList(self, repeatedFileList,fileToSearch):
        if fileToSearch in repeatedFileList:
            return True
        else:
            return False

    def getFilesWithSameName(self):
        repeatedFileList=dict()
        existingFiles=dict()
        for iterationFile in self.ListOfFiles:
            nameOfFile = self.getNameOfFileFromPath(iterationFile.getName())
            if self.FileIsInTheList(existingFiles,nameOfFile) :
                repeatedFileList[nameOfFile]=nameOfFile
            else :
#                print "File is in not in the list"
                existingFiles[nameOfFile]=nameOfFile
        return repeatedFileList
        
    def PrintFiles(self):
        for fileinList in self.ListOfFiles:
            print fileinList.getName()
    
    def PrintRepeatedFiles(self,listOfRepeatedFiles):
        for fileinList in listOfRepeatedFiles:
            print fileinList
        

if __name__ == '__main__':
    print "Begin searching repeated files"
    
    fileCollection = FileCollection()
    fileCollection.FindFiles()
#   fileCollection.PrintFiles()
    listOfRepeatedFiles = fileCollection.getFilesWithSameName()
    print "List of Repeated Files ====="
    fileCollection.PrintRepeatedFiles( listOfRepeatedFiles )
    
    
    
    print "End of Repeated Files ====="

