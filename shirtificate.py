from fpdf import FPDF

def main():

    name = get_name()

    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 50)
    pdf.cell(h=-1, text="CS50 Shirtificate", center=True)
    pdf.image("shirtificate.png", x=5, y=40, w=200, h=240)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('helvetica', 'B', 30)
    pdf.cell(h=200, text=f"{name} took CS50", center=True)
    pdf.output("shirtificate.pdf")










def get_name():
    return input("Name: ")



if __name__ == "__main__":
    main()
