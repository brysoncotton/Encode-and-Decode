from tkinter import filedialog as fd
import codecs

fin = fd.askopenfilename(title="Open the file you want to decrypt", initialdir='/home/bryson',
                         filetypes=(("text files", "*.txt"), ("all files", "*.*")))

f = open(fin, 'r')
firstLine = f.readline()
fileData = f.read()
f.close()

if firstLine == "Method A\n":
    with open(fin, "r") as f:
        lines = f.readlines()
    with open(fin, "w") as f:
        for line in lines:
            if line.strip("\n") != "Method A":
                f.write(line)
        decrypt = codecs.decode(fileData, "rot13")
        f.close()

        # Actually write the decrypted text to the file
        f = open(fin, 'w')
        fileData = f.write(decrypt)
        f.close()

        import end


else:
    print("Oops, that file has not yet been encrypted, or the encryption tag has been removed, "
          "please try another file\n")
