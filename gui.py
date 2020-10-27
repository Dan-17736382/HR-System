from tkinter import *
from tkinter import ttk
import sqlite3

class Application:
    def __init__(self):
        # create a TK instance
        self.window = Tk()

        # establish a database connection
        self.connection = sqlite3.connect("user_database.db")
        self.cursor = self.connection.cursor()

        # override the behaviour of the close button so that we make sure
        # to close the database connection on program exit
        self.window.protocol('WM_DELETE_WINDOW', self.exit)

    def exit(self):
        # make sure to close the database connection on program exit
        self.connection.commit()
        self.connection.close()

        self.window.destroy()


def main():
    # create an instance of the Application class
    application = Application()

    # set initial window size to 800x600 and centre the window
    initial_width = 800
    initial_height = 600
    x = (application.window.winfo_screenwidth() / 2) - (initial_width / 2)
    y = (application.window.winfo_screenheight() / 2) - (initial_height / 2)
    application.window.geometry('%dx%d+%d+%d' % (initial_width, initial_height, x, y))

    # set the window's title
    application.window.title("Test Window")

    # start the application
    application.window.mainloop()


if __name__ == "__main__": main()
