import pyttsx3 # Speech synthesis
import PyPDF2 # For parsing PDF documents
from sys import stderr # For displaying errors
from pathlib import Path # For verifying the file

# Reading the input
book_file = input('Enter the name of the file: ')
while True:
    page_number = input('Enter the page number: ')

    # Making sure an integer is read
    try:
        page_number = int(page_number)
        break
    except:
        print('Error: Invalid page-number!', file=stderr) # Not an integer
        continue

# Check if the file exists
if Path(f'./{book_file}').is_file():
    # Using the with-as syntax eliminates the need to close the file object manually and is safer
    with open(book_file, 'rb') as book:
        # Initialize the PDF file object
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(f'Number of pages: {pages}')
        
        # Set page_number to the first page in the case of invalid input
        if page_number > pages:
            print(f'Error: {page_number} exceeds the number of available pages.', file=stderr)
            page_number = 1
        
        # Initialize the TTS object
        speaker = pyttsx3.init()

        # Start reading the file from the specified page number
        # Note that the page numbers are 0-based i. e. Always 1 less than the desired value
        for num in range(page_number - 1, pages):
            # Extract and pronounce the text for each page
            text = pdfReader.getPage(num).extractText()
            speaker.say(text)
            speaker.runAndWait()
else:
    print('Error: File inaccessible!', file=stderr) # Couldn't read the file