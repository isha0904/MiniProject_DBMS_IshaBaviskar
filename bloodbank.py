import tkinter as tk
from tkinter import messagebox
import mysql.connector


def view_requests():
    # Add code to view receiver requests
    import viewreceiver
    viewreceiver.open_blood_reqs()
    pass


def update_stock():
    # Add code to update stock
    import stock
    stock.open_update_stock()
    pass


def loginnn():
    def login():
        bank_name = bank_name_entry.get()
        contact = contact_entry.get()

        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Potato@1604',
                database='blooddonationsystem'
            )
            cursor = conn.cursor()

            # Check if the bank details exist in the database
            query = "SELECT * FROM bloodbankdetails WHERE BankName = %s AND Contact = %s"
            data = (bank_name, contact)
            cursor.execute(query, data)
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", "Login successful")
                # Add code to redirect to the welcome page
                show_blood_bank_interface()
            else:
                messagebox.showerror("Error", "Invalid credentials")

            # Close cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def exit_app():
        window.destroy()

    # Create Tkinter window
    window = tk.Tk()
    window.title("Blood Bank Login")

    window.attributes("-fullscreen", True)

    # Set background color
    window.configure(bg="#FAEBD7")

    # Create and place widgets for login
    login_frame = tk.Frame(window, bg="#FAEBD7")
    login_frame.pack(pady=20)

    tk.Label(login_frame, text="Blood Bank Login", font=("Helvetica", 24),
             bg="#FAEBD7").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(window, text="Bank Name", font=("Helvetica", 16),
             bg="#FF5733", fg="white").pack()
    bank_name_entry = tk.Entry(window, font=("Helvetica", 16))
    bank_name_entry.pack()
    tk.Label(window, text="Contact No", font=(
        "Helvetica", 16), bg="#FF5733", fg="white").pack()
    contact_entry = tk.Entry(window, font=("Helvetica", 16))
    contact_entry.pack()

    # Button to trigger login function
    login_button = tk.Button(window, text="Login", font=(
        "Helvetica", 16), bg="#C70039", fg="white", command=login)
    login_button.pack(pady=20)

    # Button to exit the application
    exit_button = tk.Button(window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)
    window.mainloop()


def show_blood_bank_interface():

    # Create new Tkinter window for blood bank interface
    blood_bank_window = tk.Toplevel()
    blood_bank_window.title("Blood Bank Interface")

    # Set window to fullscreen
    blood_bank_window.attributes("-fullscreen", True)

    # Set background color
    blood_bank_window.configure(bg="#FAEBD7")

    tk.Label(blood_bank_window, text="Blood Bank Interface", font=("Helvetica", 24),
             bg="#FAEBD7").pack(pady=10)

    view_requests_button = tk.Button(
        blood_bank_window, text="View Receiver Requests", bg="#FF5733", fg="white", command=view_requests)
    view_requests_button.pack(pady=10)

    update_stock_button = tk.Button(
        blood_bank_window, text="Update Stock", bg="#FF5733", fg="white", command=update_stock)
    update_stock_button.pack(pady=10)

    exit_button = tk.Button(blood_bank_window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=blood_bank_window.destroy)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)


# Run the Tkinter event loop
# window.mainloop()
