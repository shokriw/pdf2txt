import PyPDF2
import re
import arabic_reshaper
from bidi.algorithm import get_display

def extract_and_clean_arabic_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    # Remove non-Arabic characters
    arabic_pattern = re.compile('[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    arabic_words = arabic_pattern.findall(text)
    
    # Join the Arabic words
    cleaned_text = ' '.join(arabic_words)
    
    # Reshape Arabic text
    reshaped_text = arabic_reshaper.reshape(cleaned_text)
    # Correct its direction
    bidi_text = get_display(reshaped_text)
    
    return bidi_text

# Use the file name "pdf.pdf"
pdf_path = 'pdf.pdf'
cleaned_text = extract_and_clean_arabic_text(pdf_path)

# Save the cleaned text to a file named "output.txt"
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(cleaned_text)

print("Arabic text has been extracted, cleaned, and saved to 'output.txt'")