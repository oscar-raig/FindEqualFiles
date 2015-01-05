import hashlib
class FoundFile:
#    FileName =''
#    hash5='' 
#    directory=[]
    def __init__ (self,FileName,readHash=False):
        self.FileName = FileName
        if ( readHash == True):
            self.hash5 = hashlib.md5(open(FileName, 'rb').read()).hexdigest()
        self.directory=''
     
    def setName(self,newFileName):
        self.FileName = newFileName    
    def getName (self):
        return self.FileName

    def setHash (self, newHash):
        self.hash5 = newHash
    def getHash (self):
        return self.hash5
    def setDirectory(self,directory):
        self.directory = directory
    def getDirectory(self):
        return self.directory
    
    
    
    