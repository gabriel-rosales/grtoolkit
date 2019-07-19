import os, sys
from grtoolkit.Windows import cmd
from _pypi_updateSetup import updateSetupVer
import shutil
from grtoolkit.Decorators import try_pass

cwd = os.path.dirname(sys.argv[0])

# CREATE DISTRIBUTION
# python3 -m pip install --user --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel

@try_pass
def deldir(path):
    shutil.rmtree(path)

deldir(os.path.dirname(sys.argv[0])+'\\build\\')
deldir(os.path.dirname(sys.argv[0])+'\\dist\\')
deldir(os.path.dirname(sys.argv[0])+'\\__pycache__\\')

updateSetupVer()

cmd(f'cd {cwd}', 
    'python setup.py sdist bdist_wheel',
    'twine upload dist/*')