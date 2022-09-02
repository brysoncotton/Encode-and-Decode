while True:
    choice = input("Do we want to Encrypt or Decrypt?\n")

    choiceCap = choice.capitalize()
    if choiceCap == "Encrypt":

        while True:
            method = input("What method are we going to use?")
            if method.capitalize() == "A":
                import methodAEncode

    if choiceCap == "Decrypt":
                import decodeMaster
    else:
        print("That is not an invalid input, please try again \n")
        