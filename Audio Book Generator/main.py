from gtts import gTTS
import PyPDF2

pdf_File = open('name.pdf', 'rb') 

pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages
textList = []

for i in range(count):
   try:
    page = pdf_Reader.getPage(i)    
    textList.append(page.extractText())
   except:
       pass

textString = " ".join(textList)
print(textString)
language = 'en'

myAudio = gTTS(text=textString, lang=language, slow=False)
myAudio.save("Audio.mp3")
