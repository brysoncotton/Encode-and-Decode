from tkinter import *

main_window = Tk()
main_window.title("Encoding and Decoding")
main_window.geometry("318x200")


def encode_click():
    main_window.destroy()
    import GUI_encode_master


def decode_click():
    main_window.destroy()
    import confirm_decrypt


welcomeMessage = Message(main_window, width=1000, text='Hello, do you want to Encode or Decode a file?', anchor=CENTER)
spacer = Message(main_window, width=1000, text='', anchor=CENTER)
encodeButton = Button(main_window, text="Encode", command=encode_click, width=35)
decodeButton = Button(main_window, text="Decode", command=decode_click, width=35)

welcomeMessage.grid(row=0, column=0)
spacer.grid(row=1,column=0)
spacer.grid(row=2,column=0)
encodeButton.grid(row=3, column=0)
decodeButton.grid(row=4, column=0)

main_window.mainloop()
