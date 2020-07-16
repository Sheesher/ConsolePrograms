import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge(res_name: str):
    pdf_writer = PdfFileWriter()
    root = tkinter.Tk()
    files = filedialog.askopenfilenames(parent=root, title="Choose the PDFs")
    for file in root.tk.splitlist(files):
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(res_name, 'wb') as o:
        pdf_writer.write(o)

name = input("Enter a name for the merged PDF: ")

merge(name)