import os


def importPackage(package):
    import importlib

    return importlib.import_module(package)


def packagePath(package):
    my_module = importPackage(package)
    return my_module.__file__


def packageDir(package):
    return os.path.dirname(packagePath(package))
