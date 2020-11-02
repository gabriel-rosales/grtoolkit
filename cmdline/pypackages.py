import grtoolkit, subprocess
from os.path import dirname

subprocess.Popen(rf'explorer /select,"{dirname(dirname(grtoolkit.__file__))}"')