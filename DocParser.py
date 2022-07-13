import io
import os.path

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def nameInput():
    name = str(input())
    return name + ".pdf"


def readDoc(name):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    path = "C:\\Users\\ПК\\Desktop\\Диплом\\" + name
    print(path)
    check_file = os.path.exists(path)
    if check_file:
        with open(path, 'rb') as fh:
            for page in PDFPage.get_pages(fh,
                                          caching=True,
                                          check_extractable=True):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
    else:
        print("No such file")
        exit(-1)

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


def convertData(text):
    # создаем текстовый файл
    # запись в текстовый файл
    file1 = open("C:\\Users\\ПК\\Desktop\\Диплом\\FileWriter.txt", "w+")
    file1.write(text)
    file1.close()
    return "C:\\Users\\ПК\\Desktop\\Диплом\\FileWriter.txt"
