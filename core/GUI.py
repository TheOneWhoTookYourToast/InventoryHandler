import tkinter as tk
from tkinter import messagebox
import json

class GUI:
    def __init__(self):
        self.accounts_path = "core/accounts.json"
        self.logged_in = False
        self.user = ""
        self.root = tk.Tk()
        self.setup_root()
        self.state = self.log_in
        self.state()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_root(self):
        self.root.title("My GUI")
        self.root.geometry("400x300")
        self.root.minsize(480, 270)

    def clean_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_toolbar()

    def create_toolbar(self):
        if self.logged_in:
            menubar = tk.Menu(self.root)
            filemenu = tk.Menu(menubar, tearoff=0)

            menubar.add_command(label="Home", command=self.home_screen)

            filemenu.add_command(label="New Character", command=self.debug_button)
            filemenu.add_command(label="Load Character", command=self.debug_button)
            filemenu.add_command(label="Save Character", command=self.debug_button)
            menubar.add_cascade(label="Character", menu=filemenu)

            if not self.logged_in:
                menubar.add_command(label="Log In", command=self.log_in)
            else:
                menubar.add_command(label="Log Out", command=self.log_out)

            self.root.config(menu=menubar)

    def log_in(self):
        self.clean_frame()
        login_frame = tk.Frame(self.root)
        login_frame.grid(row=1, column=1, pady=2, sticky="nsew")

        tk.Label(login_frame, text="Username").grid(row=1, column=1, pady=2, sticky="e")
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=1, column=2, pady=2, sticky="ew")

        tk.Label(login_frame, text="Password").grid(row=2, column=1, pady=2, sticky="e")
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=2, column=2, pady=2, sticky="ew")

        tk.Button(login_frame, text="Log In", command=self.validate_login).grid(row=3, column=1, columnspan=2, pady=2, sticky="ew")

        login_frame.grid_columnconfigure(0, weight=1)
        login_frame.grid_columnconfigure(1, weight=0)
        login_frame.grid_columnconfigure(2, weight=1)
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_rowconfigure(1, weight=0)
        login_frame.grid_rowconfigure(2, weight=0)
        login_frame.grid_rowconfigure(3, weight=0)
        login_frame.grid_rowconfigure(4, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        try:
            with open(self.accounts_path, 'r') as f:
                accounts = json.load(f)
        except FileNotFoundError:
            tk.Label(self.root, text="Accounts file not found", fg="red").grid(row=2, column=1, pady=2, sticky="ew")
            return
        
        if username in accounts and accounts[username] == password:
            self.logged_in = True
            self.user = username
            self.home_screen()
        else:
            tk.Label(self.root, text="Invalid username or password", fg="red").grid(row=2, column=1, pady=2, sticky="ew")

    def log_out(self):
        self.user = ""
        self.logged_in = False
        self.log_in()

    def debug_button(self):
        print("Button clicked")

    def new_character(self):
        pass

    def load_character(self):
        pass

    def save_character(self):
        pass

    def home_screen(self):
        self.clean_frame()

        home_frame = tk.Frame(self.root)
        home_frame.grid(row=1, column=1, pady=2, sticky="nsew")

        tk.Button(home_frame, text="New Character", command=self.new_character).pack(pady=2, fill="x")
        tk.Button(home_frame, text="Load Character", command=self.load_character).pack(pady=2, fill="x")
        tk.Button(home_frame, text="Save Character", command=self.save_character).pack(pady=2, fill="x")

        home_frame.grid_columnconfigure(0, weight=1)
        home_frame.grid_columnconfigure(1, weight=0)
        home_frame.grid_columnconfigure(2, weight=1)
        home_frame.grid_rowconfigure(0, weight=1)
        home_frame.grid_rowconfigure(1, weight=0)
        home_frame.grid_rowconfigure(2, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)

    def on_closing(self):
        answer = messagebox.askquestion("Exit", "Have you saved your character?", icon="warning", type="yesno")

        if answer == "yes":
            self.root.destroy()  # Exit
        if answer == "no":
            pass  # Cancel

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
