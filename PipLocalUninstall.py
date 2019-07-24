packageName = "grtoolkit"
#UPDATE LOCATE PACKAGE TO LATEST VER ON PYPI
from grtoolkit.Windows import cmd
uninstall_package = f'pip uninstall {packageName}'
cmd(uninstall_package)