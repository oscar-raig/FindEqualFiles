import hashlib
class FoundFile:
    FileName =''
    hash5='' 
    def __init__ (self,FileName):
        self.FileName = FileName
        hash5 = hashlib.md5(open(FileName, 'rb').read()).hexdigest()
     
    def setName(self,newFileName):
        self.FileName = newFileName    
    def getName (self):
        return self.FileName

    def setHash (self, newHash):
        self.hash5 = newHash
    def getHash (self):
        return self.hash5
    
    
    