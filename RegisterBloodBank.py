# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector


# def register():
#     bank_name = bank_name_entry.get()
#     street_loc = street_loc_entry.get()
#     city_loc = city_loc_entry.get()
#     state_loc = state_loc_entry.get()
#     contact = contact_entry.get()

#     # Connect to MySQL database
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='Potato@1604',
#         database='blooddonationsystem'
#     )
#     cursor = conn.cursor()

#     # Insert bank details into bloodbankdetails table
#     query = "INSERT INTO bloodbankdetails (BankName, StreetLoc, CityLoc, StateLoc, Contact) VALUES (%s, %s, %s, %s, %s)"
#     data = (bank_name, street_loc, city_loc, state_loc, contact)
#     cursor.execute(query, data)
#     conn.commit()

#     messagebox.showinfo("Success", "Registration successful")
#     import bloodbank
#     bloodbank.show_blood_bank_interface()
#     # Close cursor and connection
#     cursor.close()
#     conn.close()

#     pass


# def exit_app():
#     window.destroy()


# window = tk.Tk()
# window.title("Blood Bank Login/Register")
# window.attributes("-fullscreen", True)
# # Set background color
# window.configure(bg="#FAEBD7")

# # Create and place widgets for registration
# registration_frame = tk.Frame(window, bg="#FAEBD7")
# registration_frame.pack(pady=20)

# tk.Label(registration_frame, text="Register", font=("Helvetica", 24),
#          bg="#FAEBD7").grid(row=0, column=0, columnspan=2, pady=10)

# tk.Label(registration_frame, text="Bank Name:", font=("Helvetica", 16), bg="#FAEBD7").grid(
#     row=1, column=0, sticky="e", padx=5)
# bank_name_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
# bank_name_entry.grid(row=1, column=1, sticky="w",
#                      padx=5)

# tk.Label(registration_frame, text="Street Location:", font=("Helvetica", 16),
#          bg="#FAEBD7").grid(row=2, column=0, sticky="e", padx=5)
# street_loc_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
# street_loc_entry.grid(row=2, column=1, sticky="w", padx=5)

# tk.Label(registration_frame, text="City Location:", font=("Helvetica", 16), bg="#FAEBD7").grid(
#     row=3, column=0, sticky="e", padx=5)
# city_loc_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
# city_loc_entry.grid(row=3, column=1, sticky="w", padx=5)

# tk.Label(registration_frame, text="State Location:", font=("Helvetica", 16),
#          bg="#FAEBD7").grid(row=4, column=0, sticky="e", padx=5)
# state_loc_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
# state_loc_entry.grid(row=4, column=1, sticky="w", padx=5)

# tk.Label(registration_frame, text="Contact:", font=("Helvetica", 16), bg="#FAEBD7").grid(
#     row=5, column=0, sticky="e", padx=5)
# contact_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
# contact_entry.grid(row=5, column=1, sticky="w", padx=5)

# register_button = tk.Button(
#     registration_frame, text="Register", font=("Helvetica", 16), bg="#FF5733", fg="white", command=register)
# register_button.grid(row=6, column=0, columnspan=2, pady=10)


# # Button to exit the application
# exit_button = tk.Button(window, text="Exit", font=(
#     "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
# exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)


# window.mainloop()

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bloodbank


def register(bank_name_entry, street_loc_entry, city_loc_entry, state_loc_entry, contact_entry):
    bank_name = bank_name_entry.get()
    street_loc = street_loc_entry.get()
    city_loc = city_loc_entry.get()
    state_loc = state_loc_entry.get()
    contact = contact_entry.get()

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Potato@1604',
        database='blooddonationsystem'
    )
    cursor = conn.cursor()

    # Insert bank details into bloodbankdetails table
    query = "INSERT INTO bloodbankdetails (BankName, StreetLoc, CityLoc, StateLoc, Contact) VALUES (%s, %s, %s, %s, %s)"
    data = (bank_name, street_loc, city_loc, state_loc, contact)
    cursor.execute(query, data)
    conn.commit()

    messagebox.showinfo("Success", "Registration successful")

    # Close cursor and connection
    cursor.close()
    conn.close()

    # After successful registration, redirect to blood bank interface
    import bloodbank
    bloodbank.show_blood_bank_interface()


def exit_app():
    window.destroy()


window = tk.Tk()
window.title("Blood Bank Login/Register")
window.attributes("-fullscreen", True)
# Set background color
window.configure(bg="#FAEBD7")

# Create and place widgets for registration
registration_frame = tk.Frame(window, bg="#FAEBD7")
registration_frame.pack(pady=20)

tk.Label(registration_frame, text="Register", font=("Helvetica", 24),
         bg="#FAEBD7").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(registration_frame, text="Bank Name:", font=("Helvetica", 16), bg="#FAEBD7").grid(
    row=1, column=0, sticky="e", padx=5)
bank_name_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
bank_name_entry.grid(row=1, column=1, sticky="w",
                     padx=5)

tk.Label(registration_frame, text="Street Location:", font=("Helvetica", 16),
         bg="#FAEBD7").grid(row=2, column=0, sticky="e", padx=5)
street_loc_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
street_loc_entry.grid(row=2, column=1, sticky="w", padx=5)

tk.Label(registration_frame, text="City Location:", font=("Helvetica", 16), bg="#FAEBD7").grid(
    row=3, column=0, sticky="e", padx=5)
city_loc_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
city_loc_entry.grid(row=3, column=1, sticky="w", padx=5)

tk.Label(registration_frame, text="State Location:", font=("Helvetica", 16),
         bg="#FAEBD7").grid(row=4, column=0, sticky="e", padx=5)
state_loc_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
state_loc_entry.grid(row=4, column=1, sticky="w", padx=5)

tk.Label(registration_frame, text="Contact:", font=("Helvetica", 16), bg="#FAEBD7").grid(
    row=5, column=0, sticky="e", padx=5)
contact_entry = tk.Entry(registration_frame, font=("Helvetica", 16))
contact_entry.grid(row=5, column=1, sticky="w", padx=5)

register_button = tk.Button(
    registration_frame, text="Register", font=("Helvetica", 16), bg="#FF5733", fg="white", command=lambda: register(bank_name_entry, street_loc_entry, city_loc_entry, state_loc_entry, contact_entry))
register_button.grid(row=6, column=0, columnspan=2, pady=10)

# Button to exit the application
exit_button = tk.Button(window, text="Exit", font=(
    "Helvetica", 14), bg="#FAEBD7", fg="black", command=exit_app)
exit_button.place(relx=1.0, rely=0, anchor="ne", x=-20, y=20)

window.mainloop()
