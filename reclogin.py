import tkinter as tk
from tkinter import messagebox
import mysql.connector


def receiver_login():
    def login():
        # Retrieve input values
        name = name_entry.get()
        contact = contact_entry.get()

        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                password='Potato@1604',
                user='root',
                database='blooddonationsystem'
            )
            cursor = conn.cursor()

            # Execute SQL query to check if receiver exists
            cursor.execute(
                "SELECT * FROM receiver WHERE r_name=%s AND r_phno=%s", (name, contact))
            receiver = cursor.fetchone()

            if receiver:
                messagebox.showinfo("Success", "Login Successful")
                # Redirect to receiver page with options
                import ReceiverOptions
                ReceiverOptions.callfn()
                # Add your code here to redirect to receiver page

            else:
                messagebox.showerror("Error", "Invalid credentials")

            # Close cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            print("Error:", e)

    # Create Tkinter window
    login_window = tk.Tk()
    login_window.title("Receiver Login")

    # Set window to fullscreen
    login_window.attributes("-fullscreen", True)

    # Set background color
    login_window.configure(bg="#FAEBD7")

    # Create and place widgets
    header_label = tk.Label(login_window, text="Receiver Login", font=(
        "Helvetica", 24), bg="#FAEBD7", fg="black")
    header_label.pack(pady=50)

    form_frame = tk.Frame(login_window, bg="#FAEBD7")
    form_frame.pack()

    name_label = tk.Label(form_frame, text="Name:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    name_label.grid(row=0, column=0, padx=20, pady=10)

    name_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    name_entry.grid(row=0, column=1, padx=20, pady=10)

    contact_label = tk.Label(form_frame, text="Contact:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    contact_label.grid(row=1, column=0, padx=20, pady=10)

    contact_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    contact_entry.grid(row=1, column=1, padx=20, pady=10)

    login_button = tk.Button(login_window, text="Login", font=(
        "Helvetica", 14), bg="#FF5733", fg="white", command=login)
    login_button.pack(pady=20)

    # Button to exit the application
    exit_button = tk.Button(login_window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=login_window.destroy)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

    login_window.mainloop()


def receiver_register():
    def register():
        # Retrieve input values
        name = name_entry.get()
        blood_group = blood_group_var.get()
        street = street_entry.get()
        city = city_entry.get()
        state = state_entry.get()
        contact = contact_entry.get()
        quantity = quantity_entry.get()
        priority = priority_var.get()
        age = age_entry.get()

        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                password='Potato@1604',
                user='root',
                database='blooddonationsystem'
            )
            cursor = conn.cursor()

            # Execute SQL query to insert new receiver
            cursor.execute(
                "INSERT INTO receiver (r_name, r_bloodgroup, r_street, r_city, r_state, r_phno, quantity, priority, r_age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (name, blood_group, street, city, state,
                 contact, quantity, priority, age)
            )
            conn.commit()

            messagebox.showinfo("Success", "Registration Successful")
            # Redirect to login page
            # Add your code here to redirect to login page
            import ReceiverOptions
            ReceiverOptions.callfn()

            # Close cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            print("Error:", e)

    # Create Tkinter window
    register_window = tk.Tk()
    register_window.title("Receiver Registration")

    # Set window to fullscreen
    register_window.attributes("-fullscreen", True)

    # Set background color
    register_window.configure(bg="#FAEBD7")

    # Create and place widgets
    header_label = tk.Label(register_window, text="Receiver Registration", font=(
        "Helvetica", 24), bg="#FAEBD7", fg="black")
    header_label.pack(pady=50)

    form_frame = tk.Frame(register_window, bg="#FAEBD7")
    form_frame.pack()

    name_label = tk.Label(form_frame, text="Name:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    name_label.grid(row=0, column=0, padx=20, pady=10)

    name_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    name_entry.grid(row=0, column=1, padx=20, pady=10)

    blood_group_label = tk.Label(form_frame, text="Blood Group:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    blood_group_label.grid(row=1, column=0, padx=20, pady=10)

    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    blood_group_var = tk.StringVar(register_window)
    blood_group_var.set(blood_groups[0])  # default value
    blood_group_dropdown = tk.OptionMenu(
        form_frame, blood_group_var, *blood_groups)
    blood_group_dropdown.grid(row=1, column=1, padx=20, pady=10)

    street_label = tk.Label(form_frame, text="Street:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    street_label.grid(row=2, column=0, padx=20, pady=10)

    street_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    street_entry.grid(row=2, column=1, padx=20, pady=10)

    city_label = tk.Label(form_frame, text="City:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    city_label.grid(row=3, column=0, padx=20, pady=10)

    city_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    city_entry.grid(row=3, column=1, padx=20, pady=10)
    state_label = tk.Label(form_frame, text="State:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    state_label.grid(row=4, column=0, padx=20, pady=10)

    state_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    state_entry.grid(row=4, column=1, padx=20, pady=10)

    contact_label = tk.Label(form_frame, text="Contact:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    contact_label.grid(row=5, column=0, padx=20, pady=10)

    contact_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    contact_entry.grid(row=5, column=1, padx=20, pady=10)

    quantity_label = tk.Label(form_frame, text="Quantity:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    quantity_label.grid(row=6, column=0, padx=20, pady=10)

    quantity_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    quantity_entry.grid(row=6, column=1, padx=20, pady=10)

    priority_label = tk.Label(form_frame, text="Priority:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    priority_label.grid(row=7, column=0, padx=20, pady=10)

    priorities = ['Urgent', 'Not Urgent']
    priority_var = tk.StringVar(register_window)
    priority_var.set(priorities[0])  # default value
    priority_dropdown = tk.OptionMenu(
        form_frame, priority_var, *priorities)
    priority_dropdown.grid(row=7, column=1, padx=20, pady=10)

    age_label = tk.Label(form_frame, text="Age:", font=(
        "Helvetica", 14), bg="#FAEBD7")
    age_label.grid(row=8, column=0, padx=20, pady=10)

    age_entry = tk.Entry(form_frame, font=("Helvetica", 14))
    age_entry.grid(row=8, column=1, padx=20, pady=10)

    register_button = tk.Button(register_window, text="Register", font=(
        "Helvetica", 14), bg="#FF5733", fg="white", command=register)
    register_button.pack(pady=20)

    # Button to exit the application
    exit_button = tk.Button(register_window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=register_window.destroy)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

    register_window.mainloop()
