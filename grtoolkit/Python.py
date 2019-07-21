import os

def packagePath(package):
    import importlib
    my_module = importlib.import_module(package)
    return my_module.__file__

def packageDir(package):
    return os.path.dirname(packagePath(package))