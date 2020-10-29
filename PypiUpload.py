from grtoolkit.PYPI import Upload2Pypi, pypiVersion
import time
packageName = "grtoolkit"

#UPDATE PACKAGE ON PYPI
Upload2Pypi()

#UPDATE LOCAL PACKAGE TO LATEST VER ON PYPI
from grtoolkit.Windows import cmd
install_package = f'python -m pip install --upgrade {packageName} --user'
cmd(install_package, install_package)

#DELETE DIST FILES FOR FOLDER STRUCTURE READABILITY
from grtoolkit.Storage import deleteDirectory
from grtoolkit import cwd
parentFolder = cwd()
deleteDirectory(parentFolder + '\\build')
deleteDirectory(parentFolder + '\\dist')
deleteDirectory(parentFolder + f'\\{packageName}.egg-info')
