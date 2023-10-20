from fpdf import FPDF

# Create a class that inherits from FPDF to customize the PDF generation
class Shirtificate(FPDF):
    def header(self):
        # Set font and size for the header
        self.set_font("Arial", "B", 12)
        # Center the text horizontally
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=True)

    def add_shirt(self, name):
        # Set font and size for the name
        self.set_font("Arial", "", 32)
        self.set_text_color(255, 255, 255)
        # Center the name horizontally
        # Add the CS50 shirt image (adjust the path as needed)
        self.image("shirtificate.png", x=30, w=150)
        pdf.set_xy(10, 50)
        shirt_logo = name +' took CS50'
        self.cell(0, 15, shirt_logo, align="C", ln=True)



# Prompt the user for their name
name = input("Enter your name: ")

# Create a PDF object
pdf = Shirtificate()

# Add a page to the PDF (A4 size)
pdf.add_page(format="A4")

# Add the shirt and name to the PDF
pdf.add_shirt(name)

# Output the PDF to a file named "shirtificate.pdf"
pdf_file = "shirtificate.pdf"
pdf.output(pdf_file)
