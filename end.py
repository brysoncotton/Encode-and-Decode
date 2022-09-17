from tkinter import *
import time

main_window = Tk()
main_window.title("")
main_window.geometry("318x200")


def yes():
    main_window.destroy()
    import main


def no():
    time.sleep(1)
    quit()


again = Message(main_window, width=1000, text='               The file has been encrypted,\n'
                                              'do you want to encrypt or decrypt another file?', anchor=CENTER)
yes_button = Button(main_window, text="Yes", command=yes, width=35)
no_button = Button(main_window, text="No\n(Closes the App)", command=no, width=35)

again.grid(row=0, column=0)
yes_button.grid(row=1, column=0)
no_button.grid(row=2, column=0)
main_window.mainloop()
