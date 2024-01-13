from pdfminer.high_level import extract_pages, extract_text
pdfname=input("Enter pdf name: ")
text = extract_text(pdfname)
print(text.split())
