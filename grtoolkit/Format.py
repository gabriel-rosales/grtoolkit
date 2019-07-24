import sys, os


def black(pyScript=sys.argv[0]):
    """Reformat python script which calls this function to look like PEP8
    Requires black library (pip install black)"""
    os.system('black "%s"' % pyScript)
