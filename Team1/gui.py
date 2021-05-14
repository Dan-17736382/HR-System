from tkinter import *
from tkinter import ttk
import sqlite3
import webbrowser
from datetime import datetime
import csv
        
class DataPage:
    def __init__(self):
        self.connection = None
        self.window = Tk()
        self.window.title("Employee Data [Login at " + datetime.now().strftime("%H:%M:%S %d/%m/%Y") + "]")

        # List of user IDs
        self.id_label = Label(self.window, text="Employee ID")
        self.id_label.grid(row=0, column=0)
        self.id_listbox = Listbox()
        self.id_listbox.grid(row=1, column=0, pady=5)
        
        # List of user names
        self.name_label = Label(self.window, text="Name")
        self.name_label.grid(row=0, column=1)
        self.name_listbox = Listbox()
        self.name_listbox.grid(row=1, column=1, pady=5)
        
        # List of user emails
        self.email_label = Label(self.window, text="Email")
        self.email_label.grid(row=0, column=2)
        self.email_listbox = Listbox()
        self.email_listbox.grid(row=1, column=2, pady=5)
        
        # List of user departments
        self.dept_label = Label(self.window, text="Department")
        self.dept_label.grid(row=0, column=3)
        self.dept_listbox = Listbox()
        self.dept_listbox.grid(row=1, column=3, pady=5)
        
        # View Details button
        self.view_button = Button(self.window, text="View Details")
        self.view_button.grid(row=2, column=4, padx=10, pady=2)

        # Logout button
        self.logout_button = Button(self.window, text="Logout", command=lambda: self.exit())
        self.logout_button.grid(row=3, column=4, padx=10, pady=2)

        # Populate tables
        with open('MOCK_DATA.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
        
            for data in csv_reader:
                self.id_listbox.insert(END, data[0])
                self.name_listbox.insert(END, data[1])
                self.email_listbox.insert(END, data[2])
                self.dept_listbox.insert(END, data[3])

        # override the behaviour of the x button so that the database connection is always closed
        self.window.protocol('WM_DELETE_WINDOW', self.exit)

        
    def exit(self) :
        # close the database connection
        self.connection.commit()
        self.connection.close()

        # destroy the window
        self.window.destroy()
        
    
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

        # agree to lsepi checkbox
        self.is_lsepi_checked = 0
        self.lsepi_checkbox = ttk.Checkbutton(self.window, text="Do you agree to LSEPI?",variable=self.is_lsepi_checked, onvalue=1, offvalue=0)
        self.lsepi_checkbox.grid(row=3, column=0, columnspan=2, pady=5)
        
        # lsepi link
        link1 = Label(self.window, text="View LSEPI document", fg="blue", cursor="hand2")
        link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Dan-17736382/HR-System/blob/main/Team1/lsepi.pdf"))
        link1.grid(row=4, column=0, columnspan=2, pady=5)

        # submit button
        self.submit_button = Button(self.window, text="Submit", command=lambda: self.login())
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=5)
        

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

    def login(self):
        self.window.destroy()
        data_page = DataPage()
        data_page.connection = self.connection
        data_page.window.mainloop()


def main() : 
    menu = Application()

    # begin the application
    menu.window.mainloop()


if __name__ == "__main__" : main()
