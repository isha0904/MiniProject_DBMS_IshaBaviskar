import tkinter as tk


def open_receiver_page():
    window = tk.Tk()
    window.title("Receiver Page")

    def open_login():
        # print("Login button clicked")
        import reclogin
        reclogin.receiver_login()

    def open_registration():
        # print("Register button clicked")
        import reclogin
        reclogin.receiver_register()

    def go_back():
        window.destroy()  # Destroy the window

    # Set window to fullscreen
    window.attributes("-fullscreen", True)

    # Set background color
    window.configure(bg="#FAEBD7")

    # Create and place widgets
    title_label = tk.Label(window, text="Welcome to Blood Donation", font=(
        "Helvetica", 36), bg="#FAEBD7", fg="black")
    title_label.pack(pady=50)

    options_frame = tk.Frame(window, bg="#FAEBD7")
    options_frame.pack()

    login_button = tk.Button(options_frame, text="Login", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=open_login)
    login_button.grid(row=0, column=0, padx=20)

    register_button = tk.Button(options_frame, text="Register", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=open_registration)
    register_button.grid(row=0, column=1, padx=20)

    # Button to exit the application
    exit_button = tk.Button(window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

    # Run the Tkinter event loop
    window.mainloop()


open_receiver_page()
