import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    create a pdf file that contain data about the flatmates such as
    their names, their amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="p", unit="pt", format="A4")
        pdf.add_page()

        pdf.image("files/home.png", w=30, h=30)

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=40, txt="Flatmates Bill Slip", border=1, align="C", ln=1)

        pdf.set_font(family="Times", size=15, style="IB")
        pdf.cell(w=100, h=40, txt="Period : ", border=0, align="C")
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align="C", ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name + " : ", border=0, align="C")
        pdf.cell(w=150, h=40, txt="$" + str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, align="C", ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name + " : ", border=0, align="C")
        pdf.cell(w=150, h=40, txt="$" + str(round(flatmate2.pays(bill, flatmate1), 2)), border=0, align="C", ln=1)

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
