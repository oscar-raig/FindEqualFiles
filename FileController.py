
class FileController:
  
    def __init__(self, FileCollection):
        print 'Init Controller'
        self.fileCollection = FileCollection;

    def splitInFolder(self, directory):
    	print 'splitInFolder'
    	self.fileCollection.splitInFolder(directory)