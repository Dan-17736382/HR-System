from tkinter import *
from tkinter import ttk
import sqlite3


class Application:
    def __init__(self) :
        # create a tkinter instance
        self.window = Tk()
        
        # create a database connection
        self.connection = sqlite3.connect("log.db")
        self.cursor = self.connection.cursor()

        # setup the database
        self.setup_database()

        # override the behaviour of the x button so that the database connection is always closed
        self.window.protocol('WM_DELETE_WINDOW', self.exit)

        # --- GUI elements ---
        self.window.title("Login")

        # username entry
        username_label = Label(self.window, text="Username")
        username_label.grid(row=0, column=0, pady=5)
        
        self.username_entry = Entry(self.window, textvariable="username")
        self.username_entry.grid(row=0, column=1)
        
        # password entry
        password_label = Label(self.window, text="Password")
        password_label.grid(row=1, column=0, pady=5)
        
        self.password_entry = Entry(self.window, textvariable="password", show='*')
        self.password_entry.grid(row=1, column=1)

        # domain selection
        domain_label = Label(self.window, text="Domain")
        domain_label.grid(row=2, column=0, pady=5)

        self.domain_combobox = ttk.Combobox(self.window, values=["Staff", "Admin", "Guest"])
        self.domain_combobox.grid(row=2, column=1, padx=20)
        
        # submit button
        self.submit_button = Button(self.window, text="Submit", command=lambda: self.exit())
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=5)

    def setup_database(self) :
        # create the Log table if none exists
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Log (
                    full_name text,
                    date_of_birth text
                    )""")

    def exit(self) :
        # close the database connection
        self.connection.commit()
        self.connection.close()

        # destroy the window
        self.window.destroy()


def main() : 
    menu = Application()

    # begin the application
    menu.window.mainloop()


if __name__ == "__main__" : main()
