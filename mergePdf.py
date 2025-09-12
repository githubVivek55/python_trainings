# merge multiple pdf
from PyPDF2 import PdfMerger
import os

def merge_pdf(path):
    files = os.listdir(path)
    for index, file in enumerate(files):
        merger = PdfMerger()
        if file.endswith(".pdf"):
            merger.append(os.path.join(path,file))
        merger.write(os.path.join(path,"screener_cheat_sheet.pdf"))
        merger.close()
if __name__ == "__main__":
    merge_pdf("data")