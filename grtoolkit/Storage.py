import pickle, shutil, os, re
from grtoolkit.Decorators import try_pass
from grtoolkit.File import directoryLastValue

# class Pickle:
#     def __init__(self, fileName):
#         self.fileName = fileName

#     def save(self):
#         outfile = open(filename, 'wb')
#         pickle.dump(pickle_object, outfile)
#         outfile.close()

#     def load(self):
#         infile = open(filename, 'rb')
#         pickle_object = pickle.load(infile)
#         infile.close
#         return pickle_object

    

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
    def __init__(self, fileName, enc=0):
        self.fileName = fileName
        self.enc_dict = {0:None, 1:"utf8", 2:"utf-16le"}
        try:
            self.encode = self.enc_options(enc)
        except:
            self.encode = enc

    def enc_options(self, interger):
        return self.enc_dict[interger]

    def write(self, content):
        """Overwrites to file - deletes what was there before
        If file did not exist it creates a file"""

        if self.encode != None:
            content = content.encode(self.encode)
            f = open(self.fileName, "wb")
        else:
            f = open(self.fileName, "w")
        f.write(content)
        f.close()

    def append(self, content, newline=True):
        """Appends content to existing file"""
        nextLine = "\n"
        if self.encode != None:
            nextLine = nextLine.encode(self.encode)
            content = content.encode(self.encode)
            f = open(self.fileName, "ab")
        else:
            f = open(self.fileName, "a")
        f.write(nextLine + content) if newline else f.write(content)
        f.close()

    def read(self):
        """Returns existing file content"""

        f = None
        t = None

        if self.encode != None:
            f = open(self.fileName, "rb")
            t = f.read()
            t = t.decode(self.encode)
            f.close()
        else:
            f = open(self.fileName)
            t = f.read()
            f.close()
        return t

    def print(self):
        """Prints existing file content"""

        print(self.read())

def search(rootFolder, viewPrint=False, rootInclude=False, depth=None, abs=True, lastValue=False):
    '''USAGE: 
folders, files = search(path, depth=None, abs=False)

PURPOSE
Application tool for os.walk

ARGUMENTS:
    viewPrint - print to console parent folder, subfolder, and files that search() is encountering
    rootInclude - include root search folder in the output folder search results
    depth - how many levels of folders should the program output, default is no limit
    abs - output absolute or relative paths. Default is absolute path.
    lastValue - true/false. return file name or absolute address'''

    files_recursive = list()
    folders_recursive = list()
    rootBaseDepth = rootFolder.count("\\")
    rootFolderLength = len(rootFolder)
    removeStartSlashes = lambda x: x[1:] if x[:1] =='\\' else x

    if rootInclude:
        folders_recursive = [f"{rootFolder}"] if abs else [f"{directoryLastValue(rootFolder)}"]

    for root, subfolders, files in os.walk(rootFolder):

        #CHECK/COMPARE DEPTHS
        depth_current = root.count("\\") - rootBaseDepth + 1
        if depth:
            if depth < depth_current:
                break #breaks out of for loop

        if viewPrint:
            print("Parent Directory:"); print(root)
            print("Subfolders:"); print(subfolders)
            print("Files"); print(files); print("\n")

        if abs: #absolute paths
            files_recursive = files_recursive + list(map(lambda x:f"{root}\\{x}",files))
            folders_recursive = folders_recursive + list(map(lambda x:f"{root}\\{x}",subfolders))
        else:   #relative paths
            files_recursive = files_recursive + list(map(lambda x:removeStartSlashes(root[rootFolderLength:] + '\\' + x) ,files))
            folders_recursive = folders_recursive + list(map(lambda x: removeStartSlashes(root[rootFolderLength:] + '\\' + x) ,subfolders))

        if lastValue:
            files_recursive = list(map(lambda x:directoryLastValue(x),files_recursive))
            folders_recursive = list(map(lambda x:directoryLastValue(x),folders_recursive))

    return folders_recursive, files_recursive

def regexList(unfilteredList, regex):
    '''Returns list filtered by regex'''
    item_regex = re.compile(regex, re.IGNORECASE)  # Regular Expression; dot star means find everything
    filteredList = list()
    for item in unfilteredList:
        filtering = item_regex.findall(item)
        if filtering:
            filteredList.append(item)
    return filteredList