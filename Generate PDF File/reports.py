import os
import webbrowser
from fpdf import FPDF


class PDFReport:
    """
    Create a PDF report...
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font('Times', 'B', size=20)
        pdf.cell(w=0, h=60, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font('Times', 'B', size=14)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and amount of the first person
        pdf.set_font('Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and amount of the second person
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0, ln=1)

        # Change current directory
        os.chdir('files')

        pdf.output(self.filename)

        webbrowser.open(self.filename)

