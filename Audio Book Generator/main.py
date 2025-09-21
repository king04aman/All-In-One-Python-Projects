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
    except Exception as e:
        print(f"Skipping page {i}: {e}")
       

textString = " ".join(textList)
print(f"Extracted {len(textString)} characters from {count} pages.")
language = 'en'

myAudio = gTTS(text=textString, lang=language, slow=False)
myAudio.save("Audio.mp3")

print("[ok] Audio book saved as Audio.mp3")
