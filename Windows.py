import sys, os

def deleteThumb():
    os.remove(os.path.dirname(sys.argv[0]) + '\\thummb.db')