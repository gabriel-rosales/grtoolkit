import os, shutil
NX_SEED = os.environ["NX_SEED"]
shutil.copy(NX_SEED,f"{os.getcwd()}\\{os.path.basename(NX_SEED)}")
