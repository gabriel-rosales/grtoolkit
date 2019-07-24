import grtoolkit, subprocess

print(grtoolkit.cwd())

subprocess.Popen(rf'explorer /select,"{grtoolkit.cwd()}"')