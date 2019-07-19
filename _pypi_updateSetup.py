import requests, json, sys, os, datetime
import grtoolkit, re

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
    currVerSplit = pypiVersion(package).split(".")
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

    setup = grtoolkit.File.grsFile(setupfile)
    setup_txt = setup.read()
    package = package_regex.findall(setup_txt)[0].split('"')[1]     #Find package name from setup file
    currVersion = version_regex.findall(setup_txt)[0]               #Find version currently on setup file

    newsetup = grtoolkit.File.replaceWords(setup_txt,{currVersion:f'version="{genDateVersion(package)}"'})
    setup.write(newsetup)   #Overwrite setup.py


updateSetupVer()