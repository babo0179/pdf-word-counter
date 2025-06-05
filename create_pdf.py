from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", size=16)
        self.cell(0, 10, "Hello (Mostakim Ali) BTC!", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

pdf = PDF()
pdf.add_page()

pdf.output("test.pdf")
