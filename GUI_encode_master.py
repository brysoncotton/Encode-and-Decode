from tkinter import *

encodeWindow = Tk()
encodeWindow.title("Encoding")
encodeWindow.geometry("318x200")


def method_a():
    encodeWindow.destroy()
    import confrim_method_a


EncryptMessage = Message(encodeWindow, width=1000, text='What Method do you want to use to encrypt?', anchor=CENTER)
method_A_Button = Button(encodeWindow, text="Method A", command=method_a,)

EncryptMessage.grid(row=0, column=0)
method_A_Button.grid(row=1, column=0)

encodeWindow.mainloop()
