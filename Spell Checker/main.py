from textblob import TextBlob

t = 1
while t:
    a = input("Enter the word to be checked:- ")
    print("Original text: "+str(a))

    b = TextBlob(a)
    print("Corrected text: "+str(b.correct()))
    t = int(input("Try Again? 1 : 0 "))