while True:
    fin = input("Please specify the exact path of the file you want to decrypt\n")

    f = open(fin, 'r')
    firstLine = f.readline()
    fileData = f.read()
    f.close()
    choice = input("Are you sure you want to Decrypt? Y/N\n")
    choiceCap = choice.capitalize()
    if choiceCap == "Y":
        if firstLine == "Method A\n":
            import methodADecode
        else:
            print("Oops, that file has not yet been encrypted, or the encryption tag has been removed, "
                  "please try another file\n")
