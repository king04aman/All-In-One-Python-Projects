from stegano import lsbset
from stegano.lsbset import generators

# Hide the message in the image
flag="This is sample text msg!"
lets=lsbset.hide("./test.png",flag,generators.eratosthenes())
lets.save("steg.png")

# Show the message from the image
f=open("steg.png","rb")
lsbset.reveal(f,generators.eratosthenes())
