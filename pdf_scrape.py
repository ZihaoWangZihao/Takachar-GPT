import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()

    return text

# Path to PDF file
pdf_path = "/Users/zihaowang/PycharmProjects/Takachar-GPT/Narrative_Logs/Narrative_Test_Log_1.pdf"

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)
