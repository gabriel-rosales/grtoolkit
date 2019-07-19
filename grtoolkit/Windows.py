import sys, os

def deleteThumb():
    os.remove(os.path.dirname(sys.argv[0]) + '\\thummb.db')


def cmd(*args):
    '''Input: string, string, string, ...
    Can run multiple commands to the windows terminal'''

    def cmdSystem(cmdList):
       msg = ''
       for cmd in cmdList:
           if msg == '':
               msg = msg + cmd
           else:
               msg = msg + ' & ' + cmd
       return msg

    cmdlist = list()
    for instruction in args:
        cmdlist.append(instruction)
    cmdlist = cmdSystem(cmdlist)
    os.system(cmdlist)
