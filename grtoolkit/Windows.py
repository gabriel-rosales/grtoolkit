import sys, os

def deleteThumb():
    os.remove(os.path.dirname(sys.argv[0]) + '\\thummb.db')

def cmdSystem(cmdList):
   msg = ''
   for cmd in cmdList:
       if msg == '':
           msg = msg + cmd
       else:
           msg = msg + ' & ' + cmd
   return msg