### TODO: Generate a script that will create a bat file the will launch a selected python script within a virtual environment

# BAT FORMAT

# @echo off
# REM <venv activation file location> && python <python script>
# "C:\Users\gabrielr\Envs\HelloWorld\Scripts\activate.bat" && python "\\garrtechdc1\RedirectedFolders\gabrielr\Desktop\Current Job\REPO\alexandria\Python\VirtualEnvs\v_env_helloworld.py"

from grtoolkit.GUI import chooseFile
from grtoolkit.Storage import File
import os

venvPythonExe = chooseFile(os.getcwd(), title="Choose python virtual environment EXE...")

def venvBAT(venvPythonExe, script2launch):
    BAT=f"""@echo off
            REM <venv activation file location> && python <python script>
            {venvPythonExe} && python {script2launch}"""
    
    
