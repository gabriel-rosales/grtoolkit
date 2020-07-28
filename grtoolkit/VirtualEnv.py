# SUMMARY

# pip install virtualenv
# virtualenv <your-env>
# <your-env>\Scripts\activate
# <your-env>\Scripts\pip.exe install google-api-python-client


###################################################################################

#pip install virtualenv
#pip install virtualenvwrapper-win (ONLY virtualenvwrapper IF NOT WINDOWS)

'''
CREATE VIRTUAL ENVIRONMENT (NO NEED TO BE IN DIRECTORY)
mkvirtualenv my-new-project

LIST ALL VENVS IN SYSTEM
workon

ACTIVATE/DEACTIVATE VENV
workon my-new-project
deactivate

DELETE VENV
rmvirtualenv my-new-project

'''

import os 

def readText(fileName):
   f = open(fileName)
   t = f.read()
   f.close
   return t

def cmdSystem(cmdList):
   msg = ''
   for cmd in cmdList:
       if msg == '':
           msg = msg + cmd
       else:
           msg = msg + ' & ' + cmd
   return msg

def venvList():
    return os.popen('workon').read().split()[11:]

def venvCheck(venvName):
    for venv in venvList():
        if venvName == venv:
            return True
    return False

def venvDeleteAll():
    for venv in venvList():
        os.system('rmvirtualenv %s' %venv)

class venv():
    def __init__(self,name):
        self.name = name
        self.py_interpreter = ""

        if not self.Exists():
            self.Create()

    def Create(self):
        os.system('mkvirtualenv %s' %self.name)

    def Delete(self):
        os.system('rmvirtualenv %s' %self.name)

    def Exists(self):
        for venv in venvList():
            if self.name == venv:
                return True
        return False

    def SetInterpreter(self, venvPath):
        self.py_interpreter = venvPath

    def Run(self, scriptPath):
        cmd = list()
        cmd.append('workon %s' %self.name)
        cmd.append('python "%s"' %scriptPath)
        cmd.append('deactivate')
        cmd = cmdSystem(cmd)
        os.system(cmd)

    def Install_Library(self, library):
        cmd = list()
        cmd.append('workon %s' %self.name)
        cmd.append('pip install %s' %library)
        cmd.append('deactivate')
        cmd = cmdSystem(cmd)
        os.system(cmd)

    def Uninstall_Library(self, library):
        cmd = list()
        cmd.append('workon %s' %self.name)
        cmd.append('pip uninstall %s' %library)
        cmd.append('deactivate')
        cmd = cmdSystem(cmd)
        os.system(cmd)

    def RequirementsFileCreate(self, destinationFolder):
        cmd = list()
        cmd.append('workon %s' %self.name)
        cmd.append('pip freeze > "%s\\requirement.txt"' %destinationFolder)
        cmd = cmdSystem(cmd)
        os.system(cmd)

    def RequirementsInstall(self, sourceFile):
        cmd = list()
        cmd.append('workon %s' %self.name)
        cmd.append('pip install -r "%s"' %sourceFile)
        cmd = cmdSystem(cmd)
        os.system(cmd)

    def RequirementsList(self):
        reqList = os.popen('workon %s & pip freeze' %self.name).read().split()
        return reqList

    def RequirementsCompare(self, sourceFile):
        a = self.RequirementsList()
        b = readText(sourceFile).split()
        return a == b

    def RequirementsCompareOverride(self, sourceFile):
        if not self.RequirementsCompare(sourceFile):
            for lib in self.RequirementsList():
                self.Uninstall_Library(lib)
            self.RequirementsInstall(sourceFile)


if __name__ == "__main__":
    # C:\Users\gabrielr\Envs\test\Scripts\python.exe
    import sys
    parentFolder = os.path.dirname(sys.argv[0])
    # pyFile = parentFolder + '\\test.py'
    # req = "%s\\requirement.txt" %parentFolder


    # test = venv("test")
    # if not(test.Exists()):
    #     test.Create()
    # test.RequirementsFileCreate(parentFolder)
    # print(test.RequirementsCompare(parentFolder + '\\' + "requirement.txt"))
    # test.Install_Library("numpy")
    # print(test.RequirementsCompare(parentFolder + '\\' + "requirement.txt"))
    # print(sys.executable)

    # import io
    # from contextlib import redirect_stdout

    # f = io.StringIO()
    # with redirect_stdout(f):
    #     # print("hello1234")
    #     test = venv("test")
    # out = f.getvalue()

    # print(out)

    # print("hello world gabriel")
    # out = sys.stdout.readline()
    # print(out)

    # print("cookies")

    # print(sys.prefix)
    # os.environ['VIRTUAL_ENV']
    # test.Delete()

    # from io import StringIO
    # def capture_out(func):
    #     try:
    #         old_stdout = sys.stdout
    #         result = StringIO()
    #         sys.stdout = result
    #         func()
    #         result_string = result.getvalue()
    #         return result_string
    #     finally:
    #         sys.stdout = old_stdout

    # hi = capture_out(print("hello world"))
    sys.stderr.write("Hi")