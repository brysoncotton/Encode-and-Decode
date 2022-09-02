import time
import codecs


fin = input("Please specify the exact path of the file you want to encrypt\n")

f = open(fin, 'r')
fileData = f.read()

choice = input("Are you sure you want to Encrypt? Y/N\n")
choiceCap = choice.capitalize()
if choiceCap == "Y":
    encrypt = codecs.encode(fileData, "rot13")
    f.close()
    #Actually write the encrypted text to the file
    f = open(fin, 'w')
    fileData = f.write("Method A\n" + encrypt)
    f.close()

while True:
    choice = input("Alright your file is now encrypted. Would you like to encrypt or decrypt another file?\n")
    choiceCap = choice.capitalize()

    if choiceCap == 'Y':
        import main

    if choiceCap == 'N':
        print("OK, closing the App now\n")
        time.sleep(3)
        quit()
