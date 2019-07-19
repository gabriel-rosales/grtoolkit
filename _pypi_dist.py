import os, sys
cwd = os.path.dirname(sys.argv[0])
from grtoolkit.Windows import cmdSystem

# CREATE DISTRIBUTION
# python3 -m pip install --user --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel

cmd = list()
cmd.append(f'cd {cwd}')
cmd.append('setup.py sdist bdist_wheel')
# cmd.append('twine upload dist/*')
cmd = cmdSystem(cmd)
os.system(cmd)