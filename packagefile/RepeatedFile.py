class RepeatedFile:
    def __init__(self,FileName):
        self.nameOfFile=FileName
        self.directories = dict()
    def getDirectoryList(self):
        return self.directories
    def addDirectoryToList(self,directory):
        self.directories[directory]=directory
    def getName(self):
        return self.nameOfFile