from fpdf import FPDF
import os

class PDF_Printer:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(40, 10, 'Proiect MSIC!')
        self.nume_pdf = "PMSIC.pdf"
        self.latime = 20
        self.inaltime = 20

    def seteaza_nume(self, nume):
        self.nume_pdf = nume

    def scrie_PDF(self, mesaj):
        self.pdf.cell(self.latime, self.inaltime, mesaj)

    def printeaza_PDF(self):
        self.pdf.output(self.nume_pdf, 'F')