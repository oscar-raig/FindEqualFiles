import os
import os.path
import glob
from logging import root
from packagefile.FoundFile import FoundFile
from Finder.Containers_and_folders import folder
from objc._objc import NULL

class FileCollection:
  
    def __init__(self):
        print 'Init'
        self.ListOfFiles = []
    
    def getListOfFiles (self):
        return self.ListOfFiles
    
    def setListOfFiles (self,newListOfFiles):
        self.ListOfFiles = newListOfFiles
    
    def addFileFoundToRepeatedList(self,repeatedList,newFileFound,theOtherDirectory):
        Found = False
        nameOfNewFileFound = newFileFound.getName()
        for iteratedFileFound in repeatedList:
            if ( nameOfNewFileFound == iteratedFileFound.getName()):
                Found = True
                iteratedFileFound.setDirectory(newFileFound.getDirectory())
        if not Found :
            newFileFound.setDirectory(theOtherDirectory)
            repeatedList.append(newFileFound)
    
    def ChooseFileAndAddToList(self,Folder,listOfFiles,extension):
        for fileInDir in listOfFiles:
            if fileInDir.endswith(extension):
#                print(os.path.join(root, file))
 #               fileToAdd = FoundFile(os.path.join(Folder, fileInDir))
                fileToAdd = FoundFile(fileInDir)
                print "Adding file", fileInDir
                print "Adding directory", Folder
                fileToAdd.setDirectory(Folder)
                self.ListOfFiles.append(fileToAdd)    
        
    def FindFiles(self,directoryToSearch,extension):
        print "Directory To search " ,directoryToSearch

        for root, dirs, files in os.walk(directoryToSearch):
#            print "root",root
#            print "dirs",dirs
#            print "files",files
            self.ChooseFileAndAddToList( root,files,extension )
    def getNameOfFileFromPath(self,FileWithPath):
        return os.path.basename(FileWithPath)
    
    def FileIsInTheList(self, repeatedFileList,fileToSearch):
        for iterationFile in repeatedFileList:
            if iterationFile.getName() == fileToSearch :
                return True
           
        return False
    
    def GetFileFromList(self, repeatedFileList,fileToSearch):
        for iterationFile in repeatedFileList:
            if iterationFile.getName() == fileToSearch :
                return iterationFile
          
        return NULL

    def getFilesWithSameName(self):
        repeatedFileList=[]
        existingFiles=[]
        for iterationFile in self.ListOfFiles:
            nameOfFile = self.getNameOfFileFromPath(iterationFile.getName())
            if self.FileIsInTheList(existingFiles,nameOfFile) :
#                repeatedFileList.append(iterationFile)
                existingFileWeNeed = self.GetFileFromList(existingFiles,nameOfFile)
                self.addFileFoundToRepeatedList(repeatedFileList,iterationFile,existingFileWeNeed.getDirectory())
                existingFiles.append(iterationFile)
            else :
#                print "File is in not in the list"
#                existingFiles[nameOfFile]=nameOfFile
                 existingFiles.append(iterationFile)
        return repeatedFileList
        
    def PrintFiles(self):
        print "Printing Files"
        counterOfRepatedFiles = 0
        for fileinList in self.ListOfFiles:
            print "File No",counterOfRepatedFiles
            counterOfRepatedFiles = counterOfRepatedFiles + 1
            print fileinList.getName()
            listofdirectories = fileinList.getDirectory()
            for directoryIterated in listofdirectories:
                print directoryIterated
    
    def PrintRepeatedFiles(self,listOfRepeatedFiles):
        counterOfRepatedFiles = 0
        for fileinList in listOfRepeatedFiles:
            print "File No",counterOfRepatedFiles
            counterOfRepatedFiles = counterOfRepatedFiles + 1
            print fileinList.getName()
            listDirectory = fileinList.getDirectory()
            for directory in listDirectory:
                print directory
        

if __name__ == '__main__':
    import sys, getopt
    directory = ''
    extension = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hde",["directory=","extension="])
    except getopt.GetoptError:
        print 'FileCollection.py --d directory --e *.png'
        sys.exit(2)
    for opt, arg in opts:
            if opt == '-h':
                print 'FileCollection.py --d directory --e *.png'
                sys.exit()
            elif opt in ("-d", "--directory"):
                    directory = arg
            elif opt in ("-e", "--extension"):
                    extension = arg
            
    print 'Directory is "', directory
   
    print "Begin searching repeated files"
    
    fileCollection = FileCollection()
    fileCollection.FindFiles(directory,extension)
#    fileCollection.PrintFiles()
#    sys.exit()
    
    listOfRepeatedFiles = fileCollection.getFilesWithSameName()
    print "List of Repeated Files ====="
    fileCollection.PrintRepeatedFiles( listOfRepeatedFiles )
    
    
    
    print "End of Repeated Files ====="

