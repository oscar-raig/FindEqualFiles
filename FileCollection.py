import os
import os.path
import glob
from logging import root
from packagefile.FoundFile import FoundFile
from packagefile.RepeatedFile import RepeatedFile
from Finder.Containers_and_folders import folder


class FileCollection:
  
    def __init__(self):
        print 'Init'
        self.ListOfFiles = []
    
    def getListOfFiles (self):
        return self.ListOfFiles
    
    def setListOfFiles (self,newListOfFiles):
        self.ListOfFiles = newListOfFiles
    
    def addFileFoundToRepeatedList(self,repeatedList,newFileFound):
        fileToAdd = FoundFile(newFileFound.getName())
        fileToAdd.setDirectory(newFileFound.getDirectory())
        repeatedList.append(fileToAdd)
    
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
    
    def FileIsInTheList(self, List,fileToSearch):
        for iterationFile in List:
            if iterationFile.getName() == fileToSearch :
                return True
           
        return False
    
    def GetFileFromList(self,list,fileToSearch):
        for iterationFile in list:
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
                
                if not self.FileIsInTheList(repeatedFileList, nameOfFile):
                    FilefirstTime = self.GetFileFromList(existingFiles, nameOfFile)
                    self.addFileFoundToRepeatedList(repeatedFileList,FilefirstTime)
                
                self.addFileFoundToRepeatedList(repeatedFileList,iterationFile)
                existingFiles.append(iterationFile)
            else :
#                print "File is in not in the list"
#                existingFiles[nameOfFile]=nameOfFile
                existingFiles.append(iterationFile)
                
        finalRepeatedFileList=[]
        for iterationRepeatedFile in repeatedFileList:
            print 'FileName for repeated file' ,iterationRepeatedFile.getName()
            print 'DirEctory for repeated file',iterationRepeatedFile.getDirectory()
            if self.FileIsInTheList(finalRepeatedFileList, iterationRepeatedFile.getName()):
                existingFile = self.GetFileFromList(finalRepeatedFileList, 
                                                    iterationRepeatedFile.getName())
                existingFile.addDirectoryToList(iterationRepeatedFile.getDirectory())
            else:
                fileRepeated = RepeatedFile(iterationRepeatedFile.getName())
                fileRepeated.addDirectoryToList(iterationRepeatedFile.getDirectory())
                finalRepeatedFileList.append(fileRepeated)
            
            
        
        return finalRepeatedFileList
        
    def PrintFiles(self):
        print "Printing Files"
        counterOfRepatedFiles = 0
        for fileinList in self.ListOfFiles:
            print "File No ",counterOfRepatedFiles
            counterOfRepatedFiles = counterOfRepatedFiles + 1
            print 'File Name' , fileinList.getName()
            directory = fileinList.getDirectory()
            print 'Directory ' , directory
    
    def PrintRepeatedFiles(self,listOfRepeatedFiles):
        counterOfRepatedFiles = 0
        for fileinList in listOfRepeatedFiles:
            print "File No",counterOfRepatedFiles
            counterOfRepatedFiles = counterOfRepatedFiles + 1
            print fileinList.getName()
            listDirectory = fileinList.getDirectoryList()
            for directory in listDirectory:
                print directory
        
    def splitInFolder( self, directoryToSearch):
        print "splitInFolder: Directory To search " ,directoryToSearch

        for root, dirs, files in os.walk(directoryToSearch):
            print "root",root
            print "dirs",dirs
            print "files",files
            self.moveToFolder( root, files, directoryToSearch )

    def moveToFolder( self, root,files,directoryToSearch):
         print "moveToFolder: Directory To search " ,directoryToSearch     



