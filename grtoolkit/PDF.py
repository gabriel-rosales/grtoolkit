import os, PyPDF2
from grtoolkit.File import filesInWorkFolder

def join_PDFs(*args):
    """Join all PDFs at folder location or in list of absolute file locations"""

    if os.path.exists(args[0]):
        PDFs = filesInWorkFolder(args[0], ".pdf")
    elif isinstance(args[0], list):
        PDFs = args[0]
    else:
        return "Folder location or file list not properly input."

    writer = PyPDF2.PdfFileWriter()  # NEW FILE
    for PDF in PDFs:
        try:
            pdfFile = open(args[0] + "\\" + PDF, "rb")
            reader = PyPDF2.PdfFileReader(pdfFile)
            for pageNum in range(reader.numPages):
                page = reader.getPage(pageNum)
                writer.addPage(page)
        except:
            pass
    outputFile = open(args[0] + "\\" + "Joined_PDF.pdf", "wb")
    writer.write(outputFile)
    outputFile.close()
    pdfFile.close()