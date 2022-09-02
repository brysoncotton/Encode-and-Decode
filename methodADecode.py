import time
import codecs
import decodeMaster

fin = decodeMaster.fin
fileData = decodeMaster.fileData

with open(fin, "r") as f:
    lines = f.readlines()
with open(fin, "w") as f:
    for line in lines:
        if line.strip("\n") != "Method A":
            f.write(line)
    decrypt = codecs.decode(fileData, "rot13")

    f.close()
    #Actually write the decrypted text to the file
    f = open(fin, 'w')
    fileData = f.write(decrypt)
    f.close()

while True:
    choice = input("Alright your file is now decrypted. Would you like to encrypt or decrypt another file?\n")
    choiceCap = choice.capitalize()
    if choiceCap == 'Y':
        import main

    if choiceCap == 'N':
        print("OK, closing the App now\n")
        time.sleep(3)
        quit()

    else:
        print("That is not a valid input, please try again\n")
