import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

# Function to open donor.jsp


def open_donor_page():
    def open_login_page():
        # Function to handle login

        def login():
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

                # Execute SQL query
                cursor.execute(
                    "SELECT * FROM donor WHERE d_name=%s AND d_phno=%s", (name, contact))
                count = cursor.fetchone()

                if count:
                    messagebox.showinfo("Success", "Login Successful")
                    # Redirect to donor2.jsp
                    import tkinter as tk
                    from tkinter import ttk

                    def display_bank_details():
                        # Add code to handle redirection to bank_serv

                        try:
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

                        # Function to exit the application
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

                        bank_button = tk.Button(container_frame, text="See Blood Bank details", font=(
                            "Helvetica", 18), bg="#FF5733", fg="white", command=display_bank_details)
                        bank_button.grid(row=0, column=0, padx=20, pady=10)

                        # Button to exit the application
                        exit_button = tk.Button(window, text="Exit", font=(
                            "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
                        exit_button.place(relx=1.0, rely=0,
                                          anchor="ne", x=-20, y=20)
                        window.mainloop()

                    pass

                    def nearest_bank():
                        # start

                        def fetch_nearest_banks(city):
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
                                query = "SELECT BankName, Contact, StreetLoc FROM bloodbankdetails WHERE CityLoc = %s"
                                cursor.execute(query, (city,))
                                nearest_banks = cursor.fetchall()

                                # Display nearest banks in a new window
                                nearest_banks_window = tk.Toplevel()
                                nearest_banks_window.title(
                                    "Nearest Blood Banks")

                                # Create and place widgets
                                table = ttk.Treeview(nearest_banks_window, columns=(
                                    "Bank Name", "Contact", "Street Location"), show="headings")
                                table.heading("Bank Name", text="Bank Name")
                                table.heading("Contact", text="Contact")
                                table.heading("Street Location",
                                              text="Street Location")

                                for row in nearest_banks:
                                    table.insert("", "end", values=row)

                                table.pack(expand=True, fill="both")

                                # Close cursor and connection
                                cursor.close()
                                conn.close()

                            except mysql.connector.Error as e:
                                print("Error:", e)

                        def open_nearest_bank():
                            city = city_entry.get()  # Retrieve city from entry widget
                            fetch_nearest_banks(city)

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

                        city_label = tk.Label(container_frame, text="Enter City:", font=(
                            "Helvetica", 14), bg="#FAEBD7")
                        city_label.grid(row=0, column=0, padx=20, pady=10)

                        city_entry = tk.Entry(
                            container_frame, font=("Helvetica", 14))
                        city_entry.grid(row=0, column=1, padx=20, pady=10)

                        bank_button = tk.Button(container_frame, text="See Blood Bank details", font=(
                            "Helvetica", 18), bg="#FF5733", fg="white", command=open_nearest_bank)
                        bank_button.grid(
                            row=1, column=0, columnspan=2, padx=20, pady=10)

                        # Button to exit the application
                        exit_button = tk.Button(window, text="Exit", font=(
                            "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
                        exit_button.place(relx=1.0, rely=0,
                                          anchor="ne", x=-20, y=20)

                        window.mainloop()

                    # end
                    # Add code to handle redirection to nearestBank.jsp
                    pass

                    def open_nearest_drive_list_serv():
                        # Add code to handle redirection to nearest_drive_list_serv

                        def display_drive_details():
                            try:
                                # Connect to MySQL database
                                conn = mysql.connector.connect(
                                    host='localhost',
                                    user='root',
                                    password='Potato@1604',
                                    database='blooddonationsystem'
                                )
                                cursor = conn.cursor()

                                # Execute SQL query to fetch donation drive details
                                query = "SELECT bb.BankName, d.drive_city, d.drive_location, d.DateOfCamp FROM blooddonationdrive AS d JOIN bloodbankdetails AS bb ON d.Bank_Id = bb.BankId"
                                cursor.execute(query)
                                drive_details = cursor.fetchall()

                                # Display donation drive details in a new window
                                drive_details_window = tk.Toplevel()
                                drive_details_window.title(
                                    "Donation Drive Details")

                                # Create and place widgets
                                table = ttk.Treeview(drive_details_window, columns=(
                                    "Bank Name", "City", "Location", "Date Of Camp"), show="headings")
                                table.heading("Bank Name", text="Bank Name")
                                table.heading("City", text="City")
                                table.heading("Location", text="Location")
                                table.heading("Date Of Camp",
                                              text="Date Of Camp")

                                for row in drive_details:
                                    table.insert("", "end", values=row)

                                table.pack(expand=True, fill="both")

                                # Close cursor and connection
                                cursor.close()
                                conn.close()

                            except mysql.connector.Error as e:
                                print("Error:", e)

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

                        drive_button = tk.Button(container_frame, text="See Donation Drive details", font=(
                            "Helvetica", 18), bg="#FF5733", fg="white", command=display_drive_details)
                        drive_button.grid(row=0, column=0, padx=20, pady=10)

                        # Button to exit the application
                        exit_button = tk.Button(window, text="Exit", font=(
                            "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
                        exit_button.place(relx=1.0, rely=0,
                                          anchor="ne", x=-20, y=20)

                        window.mainloop()

                        # end
                        pass

                    # Function to exit the application
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

                    logo_label = tk.Label(header_frame, text="Blood Donation", font=(
                        "Helvetica", 36), bg="#FAEBD7", fg="black")
                    logo_label.pack(pady=20)

                    title_label = tk.Label(header_frame, text="Choose Where to Donate", font=(
                        "Helvetica", 24), bg="#FAEBD7", fg="black")
                    title_label.pack(pady=20)

                    container_frame = tk.Frame(window, bg="#FAEBD7")
                    container_frame.pack()

                    bank_button = tk.Button(container_frame, text="All Blood Bank Details", font=(
                        "Helvetica", 18), bg="#FF5733", fg="white", command=display_bank_details)
                    bank_button.grid(row=0, column=0, padx=20, pady=10)

                    nearest_bank_button = tk.Button(container_frame, text="Nearest Blood Bank Details", font=(
                        "Helvetica", 18), bg="#FF5733", fg="white", command=nearest_bank)
                    nearest_bank_button.grid(row=0, column=1, padx=20, pady=10)

                    drive_button = tk.Button(container_frame, text="Blood Donation Drive", font=(
                        "Helvetica", 18), bg="#FF5733", fg="white", command=open_nearest_drive_list_serv)
                    drive_button.grid(row=0, column=2, padx=20, pady=10)

                    # Button to exit the application
                    exit_button = tk.Button(window, text="Exit", font=(
                        "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
                    exit_button.place(relx=1.0, rely=0,
                                      anchor="ne", x=-20, y=20)

                    window.mainloop()

                    # Add code for redirection or display donor2.jsp content here
                else:
                    messagebox.showerror("Error", "Failed to login")

                cursor.close()
                conn.close()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database Error: {e}")

        # Create Tkinter window
        window = tk.Tk()
        window.title("Login")

        # Set window to fullscreen
        window.attributes("-fullscreen", True)

        # Set background color
        window.configure(bg="#FAEBD7")

        # Create and place widgets with blood donation related colors
        tk.Label(window, text="Login here :)", font=("Helvetica", 24),
                 bg="#FF5733", fg="white").pack(pady=20)
        tk.Label(window, text="Name", font=("Helvetica", 16),
                 bg="#FF5733", fg="white").pack()
        name_entry = tk.Entry(window, font=("Helvetica", 16))
        name_entry.pack()
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
            "Helvetica", 16), bg="#FF5733", fg="white", command=exit)
        exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

        # Run the Tkinter event loop
        window.mainloop()

        pass

    # Function to open Register.jsp
    def open_register_page():

        import tkinter as ttk

        def insert_donor_info():
            name = name_entry.get()
            age = age_entry.get()
            blood_group = blood_group_entry.get()
            state = state_entry.get()
            city = city_entry.get()
            phone = phone_entry.get()

            # Insert donor info into the database
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    password='Potato@1604',
                    user='root',
                    database='blooddonationsystem'
                )
                cursor = conn.cursor()
                query = "INSERT INTO donor (d_name, d_age, d_bloodgroup, d_city, d_state, d_phno) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (name, age, blood_group, city, state, phone)
                cursor.execute(query, data)
                conn.commit()
                messagebox.showinfo(
                    "Success", "Donor information submitted successfully")

                import tkinter as tk
                from tkinter import ttk

                def display_bank_details():
                    # Add code to handle redirection to bank_serv

                    try:
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

                    # Function to exit the application
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

                    bank_button = tk.Button(container_frame, text="See Blood Bank details", font=(
                        "Helvetica", 18), bg="#FF5733", fg="white", command=display_bank_details)
                    bank_button.grid(row=0, column=0, padx=20, pady=10)

                    # Button to exit the application
                    exit_button = tk.Button(window, text="Exit", font=(
                        "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
                    exit_button.place(relx=1.0, rely=0,
                                      anchor="ne", x=-20, y=20)
                    window.mainloop()

                pass

                def nearest_bank():
                    # start

                    def fetch_nearest_banks(city):
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
                            query = "SELECT BankName, Contact, StreetLoc FROM bloodbankdetails WHERE CityLoc = %s"
                            cursor.execute(query, (city,))
                            nearest_banks = cursor.fetchall()

                            # Display nearest banks in a new window
                            nearest_banks_window = tk.Toplevel()
                            nearest_banks_window.title(
                                "Nearest Blood Banks")

                            # Create and place widgets
                            table = ttk.Treeview(nearest_banks_window, columns=(
                                "Bank Name", "Contact", "Street Location"), show="headings")
                            table.heading("Bank Name", text="Bank Name")
                            table.heading("Contact", text="Contact")
                            table.heading("Street Location",
                                          text="Street Location")

                            for row in nearest_banks:
                                table.insert("", "end", values=row)

                            table.pack(expand=True, fill="both")

                            # Close cursor and connection
                            cursor.close()
                            conn.close()

                        except mysql.connector.Error as e:
                            print("Error:", e)

                    def open_nearest_bank():
                        city = city_entry.get()  # Retrieve city from entry widget
                        fetch_nearest_banks(city)

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

                    city_label = tk.Label(container_frame, text="Enter City:", font=(
                        "Helvetica", 14), bg="#FAEBD7")
                    city_label.grid(row=0, column=0, padx=20, pady=10)

                    city_entry = tk.Entry(
                        container_frame, font=("Helvetica", 14))
                    city_entry.grid(row=0, column=1, padx=20, pady=10)

                    bank_button = tk.Button(container_frame, text="See Blood Bank details", font=(
                        "Helvetica", 18), bg="#FF5733", fg="white", command=open_nearest_bank)
                    bank_button.grid(
                        row=1, column=0, columnspan=2, padx=20, pady=10)

                    # Button to exit the application
                    exit_button = tk.Button(window, text="Exit", font=(
                        "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
                    exit_button.place(relx=1.0, rely=0,
                                      anchor="ne", x=-20, y=20)

                    window.mainloop()

                    # end
                    # Add code to handle redirection to nearestBank.jsp
                pass

                def open_nearest_drive_list_serv():
                    # Add code to handle redirection to nearest_drive_list_serv

                    def display_drive_details():
                        try:
                            # Connect to MySQL database
                            conn = mysql.connector.connect(
                                host='localhost',
                                user='root',
                                password='Potato@1604',
                                database='blooddonationsystem'
                            )
                            cursor = conn.cursor()

                            # Execute SQL query to fetch donation drive details
                            query = "SELECT bb.BankName, d.drive_city, d.drive_location, d.DateOfCamp FROM blooddonationdrive AS d JOIN bloodbankdetails AS bb ON d.Bank_Id = bb.BankId"
                            cursor.execute(query)
                            drive_details = cursor.fetchall()

                            # Display donation drive details in a new window
                            drive_details_window = tk.Toplevel()
                            drive_details_window.title(
                                "Donation Drive Details")

                            # Create and place widgets
                            table = ttk.Treeview(drive_details_window, columns=(
                                "Bank Name", "City", "Location", "Date Of Camp"), show="headings")
                            table.heading("Bank Name", text="Bank Name")
                            table.heading("City", text="City")
                            table.heading("Location", text="Location")
                            table.heading("Date Of Camp",
                                          text="Date Of Camp")

                            for row in drive_details:
                                table.insert("", "end", values=row)

                            table.pack(expand=True, fill="both")

                            # Close cursor and connection
                            cursor.close()
                            conn.close()

                        except mysql.connector.Error as e:
                            print("Error:", e)

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

                    drive_button = tk.Button(container_frame, text="See Donation Drive details", font=(
                        "Helvetica", 18), bg="#FF5733", fg="white", command=display_drive_details)
                    drive_button.grid(row=0, column=0, padx=20, pady=10)

                    # Button to exit the application
                    exit_button = tk.Button(window, text="Exit", font=(
                        "Helvetica", 14), bg="#FAEBD7", fg="black", command=window.destroy)
                    exit_button.place(relx=1.0, rely=0,
                                      anchor="ne", x=-20, y=20)

                    window.mainloop()

                    # end
                    pass

                    # Function to exit the application
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

                logo_label = tk.Label(header_frame, text="Blood Donation", font=(
                    "Helvetica", 36), bg="#FAEBD7", fg="black")
                logo_label.pack(pady=20)

                title_label = tk.Label(header_frame, text="Choose Where to Donate", font=(
                    "Helvetica", 24), bg="#FAEBD7", fg="black")
                title_label.pack(pady=20)

                container_frame = tk.Frame(window, bg="#FAEBD7")
                container_frame.pack()

                bank_button = tk.Button(container_frame, text="All Blood Bank Details", font=(
                    "Helvetica", 18), bg="#FF5733", fg="white", command=display_bank_details)
                bank_button.grid(row=0, column=0, padx=20, pady=10)

                nearest_bank_button = tk.Button(container_frame, text="Nearest Blood Bank Details", font=(
                    "Helvetica", 18), bg="#FF5733", fg="white", command=nearest_bank)
                nearest_bank_button.grid(row=0, column=1, padx=20, pady=10)

                drive_button = tk.Button(container_frame, text="Blood Donation Drive", font=(
                    "Helvetica", 18), bg="#FF5733", fg="white", command=open_nearest_drive_list_serv)
                drive_button.grid(row=0, column=2, padx=20, pady=10)

                # Button to exit the application
                exit_button = tk.Button(window, text="Exit", font=(
                    "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
                exit_button.place(relx=1.0, rely=0,
                                  anchor="ne", x=-20, y=20)

                window.mainloop()

                cursor.close()
                conn.close()

            except mysql.connector.Error as e:
                messagebox.showerror(
                    "Error", f"Failed to submit donation information: {e}")

        def exit_app():
            window.destroy()

        # Create Tkinter window
        window = tk.Tk()

        window.title("Blood Donation")
        window.attributes("-fullscreen", True)
        window.configure(bg="#FAEBD7")

        # Create and place widgets
        frame = ttk.Frame(window)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        name_label = ttk.Label(frame, text="Name:", font=("Helvetica", 16),
                               bg="#FAEBD7")
        name_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        name_entry = ttk.Entry(frame)
        name_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        age_label = ttk.Label(frame, text="Age:", font=("Helvetica", 16),
                              bg="#FAEBD7")
        age_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        age_entry = ttk.Entry(frame)
        age_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        blood_group_label = ttk.Label(frame, text="Blood Group:", font=("Helvetica", 16),
                                      bg="#FAEBD7")
        blood_group_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        blood_group_entry = ttk.Entry(frame)
        blood_group_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        state_label = ttk.Label(frame, text="State:", font=("Helvetica", 16),
                                bg="#FAEBD7")
        state_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        state_entry = ttk.Entry(frame)
        state_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        city_label = ttk.Label(frame, text="City:", font=("Helvetica", 16),
                               bg="#FAEBD7")
        city_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        city_entry = ttk.Entry(frame)
        city_entry.grid(row=4, column=1, sticky=tk.W, pady=5)

        phone_label = ttk.Label(frame, text="Phone No:", font=("Helvetica", 16),
                                bg="#FAEBD7")
        phone_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        phone_entry = ttk.Entry(frame)
        phone_entry.grid(row=5, column=1, sticky=tk.W, pady=5)

        submit_button = ttk.Button(
            frame, text="Submit", command=insert_donor_info, font=("Helvetica", 16),
            bg="#FAEBD7")
        submit_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Exit button
        exit_button = ttk.Button(window, text="Exit", command=exit_app, font=("Helvetica", 16),
                                 bg="#FAEBD7")
        exit_button.place(relx=1.0, rely=0, anchor="ne", x=-10, y=10)

        window.mainloop()

    # donor page ka exit
    # Function to exit the application

    def exit_app():
        window.destroy()

    # Create Tkinter window
    window = tk.Tk()
    window.title("Become a Blood Donor")

    # Set window to fullscreen
    window.attributes("-fullscreen", True)

    # Set background color
    window.configure(bg="#FAEBD7")

    # Create and place widgets
    title_label = tk.Label(window, text="Become a Blood Donor", font=(
        "Helvetica", 36), bg="#FAEBD7", fg="black")
    title_label.pack(pady=50)

    options_frame = tk.Frame(window, bg="#FAEBD7")
    options_frame.pack()

    login_button = tk.Button(options_frame, text="Login", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=open_login_page)
    login_button.grid(row=0, column=0, padx=20)

    register_button = tk.Button(options_frame, text="Register", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=open_register_page)
    register_button.grid(row=0, column=1, padx=20)

    # Button to exit the application
    exit_button = tk.Button(window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

    # Run the Tkinter event loop
    window.mainloop()
    pass

# Function to open receiver2.jsp


def open_receiver_page():
    # Add code to open receiver2.jsp or handle redirection
    import receiver
    receiver.open_receiver_page()
    pass

# Function to open Bank.jsp


def open_blood_bank_page():
    # Add code to open Bank.jsp or handle redirection
    # import bloodbank

    def open_login_window():

        import bloodbank
        bloodbank.loginnn()

    def open_register_window():

        import RegisterBloodBank
        RegisterBloodBank.register()

    window = tk.Tk()
    window.title("Blood Bank")

    # Set window to fullscreen
    window.attributes("-fullscreen", True)

    # Set background color
    window.configure(bg="#FAEBD7")

    # Create and place widgets
    title_label = tk.Label(window, text="Work as a Blood Bank", font=(
        "Helvetica", 36), bg="#FAEBD7", fg="black")
    title_label.pack(pady=50)

    options_frame = tk.Frame(window, bg="#FAEBD7")
    options_frame.pack()

    login_button = tk.Button(options_frame, text="Log In", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=open_login_window)
    login_button.grid(row=0, column=0, padx=20)

    register_button = tk.Button(options_frame, text="Register", font=(
        "Helvetica", 18), bg="#FF5733", fg="white", command=open_register_window)
    register_button.grid(row=0, column=1, padx=20)

    def exit_app():
        window.destroy()

    # Button to exit the application
    exit_button = tk.Button(window, text="Exit", font=(
        "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
    exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

    # Run the Tkinter event loop
    window.mainloop()

    pass

# Function to exit the application


def exit_app():
    window.destroy()


# Create Tkinter window
window = tk.Tk()
window.title("Blood Donation")

# Set window to fullscreen
window.attributes("-fullscreen", True)

# Set background color
window.configure(bg="#FAEBD7")

# Load and resize the logo image
logo_img = Image.open(
    "WhatsApp_Image_2024-04-14_at_11.08.08_84e12278-removebg.png")
logo_img = logo_img.resize((200, 200), resample=Image.Resampling.LANCZOS)
logo_img = ImageTk.PhotoImage(logo_img)

# Create and place widgets
logo_label = tk.Label(window, image=logo_img, bg="#FAEBD7")
logo_label.pack(pady=20)

title_label = tk.Label(window, text="Welcome to Blood Donation", font=(
    "Helvetica", 36), bg="#FAEBD7", fg="black")
title_label.pack()

options_frame = tk.Frame(window, bg="#FAEBD7")
options_frame.pack(pady=50)

donor_button = tk.Button(options_frame, text="Donor", font=(
    "Helvetica", 18), bg="#FF5733", fg="white", command=open_donor_page)
donor_button.grid(row=0, column=0, padx=20)

receiver_button = tk.Button(options_frame, text="Receiver", font=(
    "Helvetica", 18), bg="#FF5733", fg="white", command=open_receiver_page)
receiver_button.grid(row=0, column=1, padx=20)

bank_button = tk.Button(options_frame, text="Blood Bank", font=(
    "Helvetica", 18), bg="#FF5733", fg="white", command=open_blood_bank_page)
bank_button.grid(row=0, column=2, padx=20)

# Button to exit the application
exit_button = tk.Button(window, text="Exit", font=(
    "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

# Run the Tkinter event loop
window.mainloop()
