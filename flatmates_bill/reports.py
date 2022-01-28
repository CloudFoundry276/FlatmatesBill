import os
import webbrowser

from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names,
    their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("images/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period Label and Value
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=40, txt='Period: ', border=0)
        pdf.cell(w=180, h=40, txt=bill.period, border=0, ln=1)

        # Insert Name and Due Amount of First Flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=180, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert Name and Due Amount of Second Flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=180, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Change directory to pdffiles, generate & open the pdf
        os.chdir("pdffiles")
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class FileSharer:

    def __init__(self, filepath, api_key='AEI2SO4bRkenQ9FYanPwMz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_fileline = client.upload(filepath=self.filepath)
        return new_fileline.url
