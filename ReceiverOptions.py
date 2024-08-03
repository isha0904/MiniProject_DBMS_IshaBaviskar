import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


def callfn():

    def display_bank_details():
        try:
            conn = mysql.connector.connect(
                host='localhost',
                password='Potato@1604',
                user='root',
                database='blooddonationsystem'
            )
            cursor = conn.cursor()
            # Execute SQL query to fetch bank details
            cursor.execute(
                "SELECT bankID, BankName, StreetLoc, CityLoc, StateLoc, Contact FROM bloodbankdetails")
            bank_details = cursor.fetchall()

            # Create Tkinter window
            bank_window = tk.Toplevel()
            bank_window.title("Blood Bank Details")

            # Create and place widgets
            table = ttk.Treeview(bank_window, columns=(
                "Bank ID", "Bank Name", "Street Location", "City Location", "State Location", "Contact"), show="headings")
            table.heading("Bank ID", text="Bank ID")
            table.heading("Bank Name", text="Bank Name")
            table.heading("Street Location",
                          text="Street Location")
            table.heading("City Location",
                          text="City Location")
            table.heading("State Location",
                          text="State Location")
            table.heading("Contact", text="Contact")

            for row in bank_details:
                table.insert("", "end", values=row)

            table.pack(expand=True, fill="both")

            # Close cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            print("Error:", e)

    def find_nearest_bank():

        def fetch_nearest_banks():
            city = city_entry.get()
            try:
                # Connect to MySQL database
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Potato@1604',
                    database='blooddonationsystem'
                )
                cursor = conn.cursor()

            # Execute SQL query to fetch nearest blood banks based on city
                query = ("SELECT b.BankName, b.StreetLoc, b.CityLoc, b.Contact, s.Apos, s.Aneg, s.Bpos, s.Bneg, s.ABpos, s.ABneg, s.Opos, s.Oneg FROM bloodbankdetails AS b JOIN bloodbankstock AS s ON b.BankID = s.BankID WHERE b.CityLoc = %s")
                cursor.execute(query, (city,))
                nearest_banks = cursor.fetchall()

                # Display nearest banks in a new window
                nearest_banks_window = tk.Toplevel()
                nearest_banks_window.title(
                    "Nearest Blood Banks")

                # Create and place widgets
                table = ttk.Treeview(nearest_banks_window, columns=(
                    "Bank Name", "Street Location", "City Location", "Contact", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"), show="headings")
                table.heading("Bank Name", text="Bank Name")
                table.heading("Street Location",
                              text="Street Location")
                table.heading("City Location", text="City Location")
                table.heading("Contact", text="Contact")
                table.heading("A+", text="A+")
                table.heading("A-", text="A-")
                table.heading("B+", text="B+")
                table.heading("B-", text="B-")
                table.heading("AB+", text="AB+")
                table.heading("AB-", text="AB-")
                table.heading("O+", text="O+")
                table.heading("O-", text="O-")

                for row in nearest_banks:
                    table.insert("", "end", values=row)

                table.pack(expand=True, fill="both")

                # Close cursor and connection
                cursor.close()
                conn.close()

            except mysql.connector.Error as e:
                print("Error:", e)

        # Create Tkinter window
        find_nearest_window = tk.Toplevel()
        find_nearest_window.title("Find Nearest Blood Bank")

        # Set background color
        find_nearest_window.configure(bg="#FAEBD7")

        # Create and place widgets
        city_label = tk.Label(find_nearest_window, text="Enter City:", font=(
            "Helvetica", 14), bg="#FAEBD7")
        city_label.grid(row=0, column=0, padx=20, pady=10)

        city_entry = tk.Entry(
            find_nearest_window, font=("Helvetica", 14))
        city_entry.grid(row=0, column=1, padx=20, pady=10)

        find_button = tk.Button(find_nearest_window, text="Find Nearest Blood Bank", font=(
            "Helvetica", 14), bg="#FF5733", fg="white", command=lambda: fetch_nearest_banks())
        find_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    def exit_app():
        window.destroy()

    # Create Tkinter window
    window = tk.Tk()
    window.title("Blood Donation")

    # Set window to fullscreen
    window.attributes("-fullscreen", True)

    # Set background color
    window.configure(bg="#FAEBD7")

    # Create and place widgets
    header_frame = tk.Frame(window, bg="#FAEBD7")
    header_frame.pack(pady=50)

    container_frame = tk.Frame(window, bg="#FAEBD7")
    container_frame.pack()

    display_button = tk.Button(container_frame, text="Display All Blood Banks", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=display_bank_details)
    display_button.grid(row=0, column=0, padx=20, pady=10)

    nearest_button = tk.Button(container_frame, text="Find Nearest Blood Bank", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=find_nearest_bank)
    nearest_button.grid(row=0, column=1, padx=20, pady=10)
    # Create and place widgets

    # Button to exit the application
    exit_button = tk.Button(window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
    exit_button.place(relx=1.0, rely=0,
                      anchor="ne", x=-20, y=20)
    window.mainloop()
