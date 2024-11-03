import tkinter as tk
from tkinter import messagebox
import os

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    
    if not username or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    user_file = f"{username}.txt"
    if os.path.exists(user_file):
        messagebox.showerror("Error", "User already exists!")
        return

    # Create the user file and save the username and password
    with open(user_file, 'w') as file:
        file.write(f"{username}\n{password}\n")

    messagebox.showinfo("Success", "Account created successfully!")
    sign_up_window.destroy()  # Close the sign-up window
    login_window()  # Open the login window immediately after sign-up


def login_user():
    username = username_entry.get()
    password = password_entry.get()
    
    user_file = f"{username}.txt"
    if not os.path.exists(user_file):
        messagebox.showerror("Error", "User does not exist!")
        return

    with open(user_file, 'r') as file:
        stored_username = file.readline().strip()
        stored_password = file.readline().strip()

    if username == stored_username and password == stored_password:
        messagebox.showinfo("Success", "Login successful!")
        login_window.destroy()
        open_task_manager(username)
    else:
        messagebox.showerror("Error", "Incorrect username or password!")

def add_task(username):
    task = task_entry.get()
    if task:
        with open(f"{username}.txt", 'a') as file:
            file.write(task + "\n")
        task_entry.delete(0, tk.END)
        load_tasks(username)

def load_tasks(username):
    task_listbox.delete(0, tk.END)
    with open(f"{username}.txt", 'r') as file:
        tasks = file.readlines()[2:]
    for task in tasks:
        task_listbox.insert(tk.END, task.strip())

def delete_task(username):
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)

        with open(f"{username}.txt", 'r') as file:
            lines = file.readlines()
        with open(f"{username}.txt", 'w') as file:
            file.write(lines[0])
            file.write(lines[1])
            for line in lines[2:]:
                if line.strip() != task_text:
                    file.write(line)

def modify_task(username):
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        task_entry.delete(0, tk.END)       # Clear the task entry field
        task_entry.insert(0, task_text)    # Insert the selected task for modification

        # Update the task once the user clicks "Save Modifications"
        def save_modification():
            new_task_text = task_entry.get()
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, new_task_text)

            # Update the file with modified task
            with open(f"{username}.txt", 'r') as file:
                lines = file.readlines()
            with open(f"{username}.txt", 'w') as file:
                file.write(lines[0])  # Write username
                file.write(lines[1])  # Write password
                for line in lines[2:]:
                    if line.strip() == task_text:
                        file.write(new_task_text + "\n")
                    else:
                        file.write(line)

            task_entry.delete(0, tk.END)  # Clear the task entry after modification
            modify_button.config(text="Modify Task", command=lambda: modify_task(username))

        # Change button to save modifications
        modify_button.config(text="Save Modifications", command=save_modification)

def open_task_manager(username):
    global task_entry, task_listbox, modify_button

    task_window = tk.Tk()
    task_window.title(f"Task Manager - {username}")

    tk.Label(task_window, text="Task:").grid(row=0, column=0)
    task_entry = tk.Entry(task_window, width=40)
    task_entry.grid(row=0, column=1)

    tk.Button(task_window, text="Add Task", command=lambda: add_task(username)).grid(row=0, column=2)
    modify_button = tk.Button(task_window, text="Modify Task", command=lambda: modify_task(username))
    modify_button.grid(row=2, column=2)
    tk.Button(task_window, text="Delete Task", command=lambda: delete_task(username)).grid(row=3, column=2)

    task_listbox = tk.Listbox(task_window, width=50, height=15)
    task_listbox.grid(row=1, column=0, columnspan=2)
    load_tasks(username)

    task_window.mainloop()

def sign_up_window():
    global username_entry, password_entry, sign_up_window

    sign_up_window = tk.Tk()
    sign_up_window.title("Sign Up")

    tk.Label(sign_up_window, text="Username:").grid(row=0, column=0)
    username_entry = tk.Entry(sign_up_window)
    username_entry.grid(row=0, column=1)

    tk.Label(sign_up_window, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(sign_up_window, show="*")
    password_entry.grid(row=1, column=1)

    tk.Button(sign_up_window, text="Sign Up", command=sign_up).grid(row=2, columnspan=2)

    sign_up_window.mainloop()

def login_window():
    global username_entry, password_entry, login_window

    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    tk.Button(login_window, text="Login", command=login_user).grid(row=2, columnspan=2)

    login_window.mainloop()

def main_window():
    main_win = tk.Tk()
    main_win.title("Welcome")

    tk.Label(main_win, text="Welcome! Please choose an option:").pack(pady=10)
    tk.Button(main_win, text="Sign Up", command=lambda: [main_win.destroy(), sign_up_window()]).pack(pady=5)
    tk.Button(main_win, text="Login", command=lambda: [main_win.destroy(), login_window()]).pack(pady=5)

    main_win.mainloop()

# Start the program
main_window()
