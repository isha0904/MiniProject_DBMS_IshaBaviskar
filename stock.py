import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector


def update_blood_stock():
    try:
        # Prompt user for input values
        bank_id = simpledialog.askinteger("Bank ID", "Enter Bank ID:")
        operation = simpledialog.askstring(
            "Operation", "Select operation (Inc / Dec):")
        blood_group = simpledialog.askstring(
            "Blood Group", "Enter Blood Group:")
        units = simpledialog.askinteger("Units", "Enter Units:")

        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Potato@1604',
            database='blooddonationsystem'
        )
        cursor = conn.cursor()

        # Execute the stored procedure to update blood stock
        if operation == "Inc":
            cursor.callproc("UpdateDonatedStock",
                            (bank_id, blood_group, units))
        else:
            cursor.callproc("UpdateAfterReceiver",
                            (bank_id, blood_group, units))
        conn.commit()

        # Display success message
        messagebox.showinfo("Success", "Blood stock updated successfully")

        # Display updated blood stock
        display_blood_stock(cursor, bank_id)

        # Close cursor and connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error:", e)


def display_blood_stock(cursor, bank_id):
    try:
        # Execute query to display updated blood stock
        cursor.execute(
            "SELECT * FROM bloodbankstock WHERE BankID = %s", (bank_id,))
        blood_stock = cursor.fetchall()

        # Create new window for displaying blood stock
        stock_window = tk.Toplevel()
        stock_window.title("Blood Stock")

        # Create and place widgets for displaying blood stock
        for i, row in enumerate(blood_stock):
            for j, value in enumerate(row):
                label = tk.Label(stock_window, text=value,
                                 font=("Helvetica", 12))
                label.grid(row=i, column=j, padx=5, pady=5)

    except mysql.connector.Error as e:
        print("Error:", e)


def open_update_stock():
    update_blood_stock()


# Create Tkinter window
window = tk.Tk()
window.title("Blood Bank Update Stock")

# Set window to fullscreen
window.attributes("-fullscreen", True)

# Set background color
window.configure(bg="#FAEBD7")

# Create and place widgets
title_label = tk.Label(window, text="Update Blood Stock", font=(
    "Helvetica", 36), bg="#FAEBD7", fg="black")
title_label.pack(pady=50)

update_stock_button = tk.Button(window, text="Update Stock", font=(
    "Helvetica", 18), bg="#FF5733", fg="white", command=open_update_stock)
update_stock_button.pack(pady=20)

# Button to exit the application
exit_button = tk.Button(window, text="Exit", font=(
    "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

# Run the Tkinter event loop
window.mainloop()
