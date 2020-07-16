import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt(filename=filedialog.askopenfile().name):
    pdf_reader = PdfFileReader(filename)
    pdf_writer = PdfFileWriter()
    password = input("Enter a secure password: ")

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, use_128bit=True)

    with open(filename + ".encrypted.pdf", 'wb') as o:
        pdf_writer.write(o)
    
encrypt()