import pyttsx3
from PyPDF2 import PdfFileReader
read= open('sample.pdf','rb')
pdfreader=PdfFileReader(read)
information = pdfreader.getDocumentInfo()
number_of_pages = pdfreader.getNumPages()
print(number_of_pages)
for i in range(number_of_pages):
        page=pdfreader.getPage(i)
        text=page.extractText()
        print(text)
        main=pyttsx3.init()
        main.say('hai am imran\'s audio book')
        main.say(text)
        main.runAndWait()
