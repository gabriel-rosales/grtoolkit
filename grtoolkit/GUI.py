import tkinter as tk
from tkinter import filedialog

def chooseFile(parent, title = "Select file"):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(initialdir=parent, title=title)