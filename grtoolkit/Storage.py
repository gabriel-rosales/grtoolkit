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