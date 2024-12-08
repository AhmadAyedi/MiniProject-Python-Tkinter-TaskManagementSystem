def main_window():
    main_win = tk.Tk()
    main_win.title("Welcome")

    tk.Label(main_win, text="Welcome! Please choose an option:").pack(pady=10)
    tk.Button(main_win, text="Sign Up", command=lambda: [main_win.destroy(), sign_up_window()]).pack(pady=5)
    tk.Button(main_win, text="Login", command=lambda: [main_win.destroy(), login_window()]).pack(pady=5)

    main_win.mainloop()

# Start the program
main_window()





























