import os


def importPackage(package):
    import importlib

    return importlib.import_module(package)


def packagePath(package):
    my_module = importPackage(package)
    return my_module.__file__


def packageDir(package):
    return os.path.dirname(packagePath(package))


def runPipenv(path, *args, **kwargs):
    execCommand = f"pipenv run python {path}"
    for arg in args:
        execCommand+= f" {arg}"
    for kwarg in kwargs:
        execCommand+= f" {kwarg}"
    os.system(execCommand)