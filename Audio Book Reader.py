import pyttsx3
import PyPDF2
book = open('Introduction_to_algorithms-3rd Edition.pdf','rb') #Just change the name of the pdf 
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7,pages): #Replace 7 from the page of the book from where you want to read.
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()