import os
from grtoolkit.Decorators import try_pass


def importPackage(package):
    """Programatically import library"""
    import importlib
    return importlib.import_module(package)


def packagePath(package):
    """Find local path of library"""
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

@try_pass
def dictionary_add_modify(dictionary, **kwargs2AddUpdate):
    """Add or modify kwargs to dictionary"""
    for k,v in kwargs2AddUpdate.items():
        dictionary.update({f"{k}":v})
    return dictionary



if __name__ == "__main__":
    pass
