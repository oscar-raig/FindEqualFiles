
from FileCollection import FileCollection

from FileController import FileController

if __name__ == '__main__':
    import sys, getopt
    directory = ''
    extension = ''
    function = 1
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hdes",["directory=","extension="])
    except getopt.GetoptError:
        print 'Error: FileCollection.py -d directory -e *.png'
        sys.exit(2)
    print "options",opts    
    for opt, arg in opts:
            print 'Option' + opt
            if opt == '-h':
                print 'Help: FileCollection.py --d directory --e *.png'
                sys.exit()
            elif opt in ("-d", "--directory"):
                    directory = arg
            elif opt in ("-e", "--extension"):
                    extension = arg
            elif opt in ("-s", "--split"):
                print 'arg', arg, opt
                directory = arg  
                function = 2      
            
    print 'Directory is "', directory
   
    print "Begin searching repeated files"
    
    if function == 1 :
        fileCollection = FileCollection()
        fileCollection.FindFiles(directory,extension)
        #    fileCollection.PrintFiles()
        #    sys.exit()
    
        listOfRepeatedFiles = fileCollection.getFilesWithSameName()
        print "List of Repeated Files ====="
        fileCollection.PrintRepeatedFiles( listOfRepeatedFiles )
        print "End of Repeated Files ====="
    elif function == 2 :
        fileController = FileController(FileCollection())
        fileController.splitInFolder(directory)    
