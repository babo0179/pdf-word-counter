import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def word_count(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    pdf_path = input("PDF ফাইলের path দিন: ")
    
    if not os.path.exists(pdf_path):
        print("ফাইল পাওয়া যায়নি।")
    else:
        text = extract_text_from_pdf(pdf_path)
        count = word_count(text)
        print(f"\nমোট শব্দ (word): {count}")
