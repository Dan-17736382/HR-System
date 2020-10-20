from tkinter import *
from tkinter import ttk

window = Tk()

class Application:
    def __init__(self, master):
        button = ttk.Button(master, text = "Exit", command = self.exit)
        button.place(x=700, y=550)

    def exit(root):
        window.destroy()


def main(): 
    menu = Application(window)
    window.geometry("800x600")
    window.title("Test Window")
    window.resizable(width=False, height=False)
    window.mainloop()


if __name__ == "__main__": main()
