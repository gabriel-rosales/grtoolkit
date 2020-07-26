import os, sys
from grtoolkit.Decorators import try_pass
from grtoolkit.Windows import cmd
from grtoolkit.Storage import deleteDirectory

import requests, json, datetime
import grtoolkit, re

cwd = os.path.dirname(sys.argv[0])

def pypiJSON(package, version="0.0.0 Optinal"):
    '''Returns pypi JSON file using pypi API'''
    if version == "0.0.0 Optinal":
        r = requests.get(f'https://pypi.org/pypi/{package}/json')
    else:
        r = requests.get(f'https://pypi.org/pypi/{package}/{version}/json')
    return r.json()

def pypiVersion(package):
    '''Returns latest pypi version code from specified package name'''
    return pypiJSON(package)['info']['version']

def genDateVersion(package):
    '''Returns a new date version code after comparing with latest Pypi package version online
    Follows the format Year.Month.ReleaseNumber'''
    try:
        currVerSplit = pypiVersion(package).split(".")
    except:
        currVerSplit = "0.0.0".split(".")
        
    DATE = datetime.datetime.now()

    def prefix0str(interger):
        if len(str(interger)) == 1:
            return f"0{str(interger)}"
        else:
            return str(interger)

    # COMPARE IF THE YEAR AND MONTH MATCHES
    if DATE.strftime(f"%y.%m") == f"{currVerSplit[0]}.{prefix0str(currVerSplit[1])}":
        newVersion = DATE.strftime(f"%y.%m.{int(currVerSplit[2])+1}")
    else:
        newVersion = DATE.strftime(f"%y.%m.0")
    return newVersion

def updateSetupVer(setupfile=os.path.dirname(sys.argv[0])+"\\setup.py"):
    '''Updates setup.py in the specified directory to the next Date Version'''
    package_regex = re.compile('name=".*"')     
    version_regex = re.compile('version=".*"')

    setup = grtoolkit.Storage.File(setupfile)
    setup_txt = setup.read()
    package = package_regex.findall(setup_txt)[0].split('"')[1]     #Find package name from setup file
    currVersion = version_regex.findall(setup_txt)[0]               #Find version currently on setup file

    newsetup = grtoolkit.File.replaceWords(setup_txt,{currVersion:f'version="{genDateVersion(package)}"'})
    setup.write(newsetup)   #Overwrite setup.py

def Upload2Pypi():
    '''Recreates distribution & build, updates version on setup.py, pushes upload to Pypi
    Must be used in the same folder as setup.py'''
    if os.path.exists(cwd + "\\setup.py"):
        deleteDirectory(os.path.dirname(sys.argv[0])+'\\build\\')
        deleteDirectory(os.path.dirname(sys.argv[0])+'\\dist\\')
        deleteDirectory(os.path.dirname(sys.argv[0])+'\\__pycache__\\')

        updateSetupVer()

        if "PYPI_USER" in os.environ and "PYPI_PASS" in os.environ:
            cmd(f'cd {cwd}', 
                'python setup.py sdist bdist_wheel',
                f'twine upload dist/* -u {os.environ["PYPI_USER"]} -p {os.environ["PYPI_PASS"]}')
        else:
            cmd(f'cd {cwd}', 
                'python setup.py sdist bdist_wheel',
                f'twine upload dist/*')
    else:
        print(f"setup.py not found in {cwd}")

if __name__ == "__main__":
    Upload2Pypi()
