import tkinter as tk
import hashlib
import webbrowser
import subprocess
from selenium import webdriver

root = tk.Tk()
root.title("SecroSearch")

label = tk.Label(root, text="Welcome to Secrosearch")
label.pack()

# Add a Frame for the login UI
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

# Add a Button to submit the login credentials
login_button = tk.Button(login_frame, text="Login", command=lambda: LoginSignupApp(root, username_entry, password_entry).login())
login_button.pack()

# Add a Frame for the sign up UI
signup_frame = tk.Frame(root)
signup_frame.pack()

tk.Label(signup_frame, text="Username:").pack()
signup_username_entry = tk.Entry(signup_frame)
signup_username_entry.pack()

tk.Label(signup_frame, text="Password:").pack()
signup_password_entry = tk.Entry(signup_frame, show="*")
signup_password_entry.pack()

# Add a Button to submit the sign up credentials
signup_button = tk.Button(signup_frame, text="Sign Up", command=lambda: SignUp(root, signup_username_entry, signup_password_entry).signup())
signup_button.pack()

class LoginSignupApp:
    def __init__(self, root, username_entry, password_entry):
        self.root = root
        self.username_entry = username_entry
        self.password_entry = password_entry

    def login(self):
        # Add your code here to authenticate the user
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in users and users[username] == hashed_password:
            print("Login successful!")
            # Clear the login UI
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            # Add a search bar
            search_frame = tk.Frame(self.root)
            search_frame.pack()
            search_entry = tk.Entry(search_frame)
            search_entry.pack()
            # Add a Button to submit the search
            search_button = tk.Button(search_frame, text="Search", command=lambda: self.search(search_entry.get()))
            search_button.pack()
            # Add a Button to clear the search history
            clear_history_button = tk.Button(search_frame, text="Clear History", command=self.clear_history)
            clear_history_button.pack()
            clear_history_button.config(state="disabled")
        else:
            print("Invalid username or password")

    def search(self, query):
        # Open a private Google search
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        browser = webdriver.Chrome(options=options)
        browser.get('https://www.google.com/search?q=' + query)
        time.sleep(60)


    def clear_history(self):
        # Clear the search history
        pass

class SignUp:
    def __init__(self, root, signup_username_entry, signup_password_entry):
        self.root = root
        self.signup_username_entry = signup_username_entry
        self.signup_password_entry = signup_password_entry

    def signup(self):
        # Add your code here to create a new user
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_password
        print(f"User {username} created!")
        # Clear the sign up UI
        self.signup_username_entry.delete(0, tk.END)
        self.signup_password_entry.delete(0, tk.END)

# Example database
users = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest()
}

root.mainloop()

# Clear the login UI
username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)

# Clear the sign up UI
signup_username_entry.delete(0, tk.END)
signup_password_entry.delete(0, tk.END)

def login(self):
    # Get the username and password from the entry fields
    username = self.username_entry.get()
    password = self.password_entry.get()
    
    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if the entered username and password match any existing user in the database
    if username in users and users[username] == hashed_password:
        print("Login successful!")
        # Clear the login UI
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        # Add a search bar
        search_frame = tk.Frame(self.root)
        search_frame.pack()
        search_entry = tk.Entry(search_frame)
        search_entry.pack()
        # Add a Button to submit the search
        search_button = tk.Button(search_frame, text="Search", command=lambda: self.search(search_entry.get()))
        search_button.pack()
        # Add a Button to clear the search history
        clear_history_button = tk.Button(search_frame, text="Clear History", command=self.clear_history)
        clear_history_button.pack()
        clear_history_button.config(state="disabled")
    else:
        print("Invalid username or password")
       
    class LoginSignupApp:
     def __init__(self, root, username_entry, password_entry, max_failed_attempts=5):
        self.root = root
        self.username_entry = username_entry
        self.password_entry = password_entry
        self.max_failed_attempts = max_failed_attempts
        self.failed_attempts = 0

    def login(self):
        # Get the username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hash the password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the entered username and password match any existing user in the database
        if username in users and users[username] == hashed_password:
            print("Login successful!")
            # Clear the login UI
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            # Add a search bar
            search_frame = tk.Frame(self.root)
            search_frame.pack()
            search_entry = tk.Entry(search_frame)
            search_entry.pack()
            # Add a Button to submit the search
            search_button = tk.Button(search_frame, text="Search", command=lambda: self.search(search_entry.get()))
            search_button.pack()
            # Add a Button to clear the search history
            clear_history_button = tk.Button(search_frame, text="Clear History", command=self.clear_history)
            clear_history_button.pack()
            clear_history_button.config(state="disabled")
            # Reset the failed attempt counter
            self.failed_attempts = 0
        else:
            print("Invalid username or password")
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_failed_attempts:
                print(f"Maximum number of failed attempts ({self.max_failed_attempts}) reached. Exiting program.")
                exit()