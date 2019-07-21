import pickle, shutil
from grtoolkit.Decorators import try_pass

def savePickle(filename, pickle_object):
    outfile = open(filename, 'wb')
    pickle.dump(pickle_object, outfile)
    outfile.close()
    
def loadPickle(filename):
    infile = open(filename, 'rb')
    pickle_object = pickle.load(infile)
    infile.close
    return pickle_object

@try_pass
def deleteDirectory(path):
    shutil.rmtree(path)

class File:
    def __init__(self, fileName):
        self.fileName = fileName

    def write(self, content):
        """Overwrites to file - deletes what was there before
        If file did not exist it creates a file"""

        f = open(self.fileName, "w")
        f.write(content)
        f.close()

    def append(self, content, newline=True):
        """Appends content to existing file"""

        f = open(self.fileName, "a")
        f.write("\n" + content) if newline else f.write(content)
        f.close()

    def read(self):
        """Returns existing file content"""

        f = open(self.fileName)
        t = f.read()
        f.close
        return t

    def print(self):
        """Prints existing file content"""

        print(self.read())