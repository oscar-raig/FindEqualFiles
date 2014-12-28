import os
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
                self.ListofFiles.append(fileToAdd)    
        
    def FindFiles(self):

        for root, dirs, files in os.walk("/Users/oscarraigcolon/Arrel/git/rebuild-graph/"):
#            print root
            self.ChooseFileAndAddToList( root,files )

           
    
    def PrintFiles(self):
        for fileinList in self.ListofFiles:
            print fileinList.getName()

if __name__ == '__main__':
    print "Goodbye, World!"
    
    fileCollection = FileCollection()
    fileCollection.FindFiles()
    fileCollection.PrintFiles()
    
    print "We have finished"

