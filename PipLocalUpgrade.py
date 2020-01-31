packageName = "grtoolkit"
#UPDATE LOCATE PACKAGE TO LATEST VER ON PYPI
from grtoolkit.Windows import cmd
install_package = f'python -m pip install --upgrade {packageName} --user'
cmd(install_package,
    install_package)
    