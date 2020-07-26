import grtoolkit as gr 
import os, shutil

parentFolder = os.getcwd()

print("Generate Quotes from Goodreads website.\n")
author = input("Author to search:\n")
book = input("Book name as per Goodreads:\n")
pickleFile = f"{author}.pickle"
saveFile = f"Quotes.txt"

# IF PICKLE FILE EXISTS THEN LOAD, OTHERWISE GENERATE FROM GOODREADS WEBSITE
if os.path.isfile(pickleFile):
    db = gr.Quotes.loadDB(pickleFile)
else:
    db = gr.Quotes.generateDB(author, saveFile=pickleFile)

# FILTER DATABASE BY 
qts = gr.Quotes.filterQuotesByBook(db,book)
# EXPORT QUOTES TO NOTEPAD FILE
gr.Quotes.export(qts,f"{parentFolder}\\{saveFile}",enc=1)

# COPY QUOTES TEMPLATE FILE
shutil.copy2(os.environ['QUOTE_PPT_TEMPLATE'],f"{parentFolder}\\QUOTE_PPT_TEMPLATE.pptm")


