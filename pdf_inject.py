python
from pypdf import PdfReader, PdfWriter
import os

# Prompt user for file names
input_pdf = input("Enter the input PDF filename: ").strip()
output_pdf = input("Enter the output PDF filename: ").strip()

# Validate input file exists
if not os.path.isfile(input_pdf):
    print(f"[-] Error: File '{input_pdf}' does not exist.")
    exit(1)

try:
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)

    # Add JavaScript
    writer.add_js('app.alert("Hello World");')

    # Write modified PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"[+] Successfully created: {output_pdf}")

except Exception as e:
    print(f"[-] Error processing PDF: {e}")
