import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import mysql.connector


def fetch_blood_reqs():
    try:
        # Prompt user for BankID
        bank_id = simpledialog.askinteger("Bank ID", "Enter Bank ID:")

        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Potato@1604',
            database='blooddonationsystem'
        )
        cursor = conn.cursor()

        # Execute SQL query to fetch blood requests based on BankId
        query = "SELECT * FROM bloodreq WHERE BankId = %s"
        cursor.execute(query, (bank_id,))
        blood_reqs = cursor.fetchall()

        # Display blood requests in a new window
        blood_reqs_window = tk.Toplevel()
        blood_reqs_window.title("Blood Requests")

        # Create and place widgets
        table = ttk.Treeview(blood_reqs_window, columns=(
            "BankId", "ReceiverName", "Blood Group", "PhoneNo", "Quantity", "Priority"), show="headings")
        table.heading("BankId", text="BankId")
        table.heading("ReceiverName", text="ReceiverName")
        table.heading("Blood Group", text="Blood Group")

        table.heading("PhoneNo", text="PhoneNo")
        table.heading("Quantity", text="Quantity")
        table.heading("Priority", text="Priority")

        for row in blood_reqs:
            table.insert("", "end", values=row)

        table.pack(expand=True, fill="both")

        # Close cursor and connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error:", e)


def open_blood_reqs():
    fetch_blood_reqs()


# Create Tkinter window
window = tk.Tk()
window.title("Blood Bank Blood Requests")

# Set window to fullscreen
window.attributes("-fullscreen", True)

# Set background color
window.configure(bg="#FAEBD7")

# Create and place widgets
title_label = tk.Label(window, text="Blood Requests", font=(
    "Helvetica", 36), bg="#FAEBD7", fg="black")
title_label.pack(pady=50)

view_requests_button = tk.Button(window, text="View Blood Requests", font=(
    "Helvetica", 18), bg="#FF5733", fg="white", command=open_blood_reqs)
view_requests_button.pack(pady=20)

# Button to exit the application
exit_button = tk.Button(window, text="Exit", font=(
    "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

# Run the Tkinter event loop
window.mainloop()
