from pypdf import PdfMerger
import os
from pathlib import Path



def PDFMerge(date):
    merger = PdfMerger()

    for pdf in sorted(os.listdir("PDF")):
        file_extension = Path(pdf).suffix

        if file_extension != '.xlsx':
            pdf = "PDF/"+pdf
            merger.append(pdf)
    merger.write("PDF/"+date+".pdf")
    merger.close()
