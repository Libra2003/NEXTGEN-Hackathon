# importing required modules 
from PyPDF2 import PdfReader 

# creating a pdf reader object 
reader = PdfReader('1.pdf') 

# creating an empty list to store the text from each page 
text_list = []

# looping over all the pages in the pdf file 
for page in reader.pages:
    # extracting text from page 
    text = page.extract_text() 
    # appending the text to the list 
    text_list.append(text)

# printing the text from each page 
for text in text_list:
    print(text)
