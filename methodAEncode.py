import codecs
from tkinter import filedialog as fd

fin = fd.askopenfilename(title="Open the file you want to encrypt", initialdir='/home/bryson',
                         filetypes=(("text files", "*.txt"), ("all files", "*.*")))

f = open(fin, 'r')
fileData = f.read()

encrypt = codecs.encode(fileData, "rot13")
f.close()
#Actually write the encrypted text to the file
f = open(fin, 'w')
fileData = f.write("Method A\n" + encrypt)
f.close()

import end
