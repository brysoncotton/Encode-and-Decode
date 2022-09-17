from tkinter import *


def confirm():
    confirmWindow.destroy()
    import decodeMaster


confirmWindow = Tk()
confirmWindow.title("Confirm?")
confirmWindow.geometry("215x100")

yes_button = Button(confirmWindow, text="Confirm\nDecryption?", command=confirm, height=5, width=10, bg='#0FFF50')
no_button = Button(confirmWindow, text="Terminate\nDecryption", command=confirm, height=5, width=10, bg='#DC143C')
yes_button.grid(row=0, column=0)
no_button.grid(row=0, column=1)
confirmWindow.mainloop()