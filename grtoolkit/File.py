import sys, re, os, math, functools, time, PyPDF2
from grtoolkit.Storage import File

def replaceWords(textOrFile, dictionary):
    if os.path.exists(textOrFile):
        base_text = File(textOrFile).read()
    for key, val in dictionary.items():
        base_text = textOrFile.replace(key,val)
    return base_text

def foldersInFolder(folder, query=""):  # Returns list of files of specified file type
    folder_list = []
    for _, subfolders, _ in os.walk(folder):  # folders, subfolders, filenames
        for sub in subfolders:
            if query in sub:  # if file_search is not empty
                folder_list.append(sub)
    return folder_list


def filesInFolder(folder, fileType):  # Returns list of files of specified file type
    fileType = delDotPrefix(fileType)
    file_regex = re.compile(
        r".*\." + fileType, re.IGNORECASE
    )  # Regular Expression; dot star means find everything
    file_list = []
    for _, _, filenames in os.walk(folder):  # folders, subfolders, filenames
        for singlefile in filenames:
            file_search = file_regex.findall(singlefile)
            if file_search:  # if file_search is not empty
                file_list.append(singlefile)
    return file_list


def directoryLastValue(directory):
    return directory.rsplit("\\", 1)[-1]


def checkExtension(filePath, ext):
    '''Compare file extension; returns True/False'''
    return filePath[filePath.rfind(".", 0) : len(filePath)] == correctDotPrefix(ext)


def correctExtension(filePath, ext):
    '''Add file extension if it is incorrect'''
    return (
        filePath if checkExtension(filePath, ext) else filePath + correctDotPrefix(ext)
    )

def correctDotPrefix(string):
    '''Add dot prefix to file extension if missing'''
    return string if string.find(".") == 0 else "." + string


def delDotPrefix(string):
    '''Delete dot prefix to file extension if present'''
    return string[1:] if string.find(".") == 0 else string

def ext(path, dot=True):
    if dot:
        return path[path.rfind(".", 0) : len(path)]
    else:
        return path[path.rfind(".", 0) + 1 : len(path)]

def name(path):
    return path[: path.rfind(".", 0)]

if __name__ == "__main__":
    pass