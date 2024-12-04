import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and BMI table
def create_db():
    conn = sqlite3.connect('bmi_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            height REAL,
            weight REAL,
            bmi REAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get input values
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        # Calculate BMI
        bmi = weight / (height / 100) ** 2

        # Display BMI result
        label_bmi_result.config(text=f"BMI: {bmi:.2f}")

        # Insert the record into the database
        conn = sqlite3.connect('bmi_tracker.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bmi_records (height, weight, bmi) VALUES (?, ?, ?)', 
                       (height, weight, bmi))
        conn.commit()
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "BMI record added successfully!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid height and weight values.")

# Function to view the BMI history
def view_history():
    # Clear previous history
    listbox_history.delete(0, tk.END)

    # Retrieve and display records from the database
    conn = sqlite3.connect('bmi_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT height, weight, bmi, date FROM bmi_records ORDER BY date DESC')
    records = cursor.fetchall()
    conn.close()

    for record in records:
        listbox_history.insert(tk.END, f"Height: {record[0]} cm | Weight: {record[1]} kg | BMI: {record[2]:.2f} | Date: {record[3]}")

# Setting up the GUI
root = tk.Tk()
root.title("BMI Tracker")

# Create the database
create_db()

# Labels and Entry Widgets
label_height = tk.Label(root, text="Height (in cm):")
label_height.grid(row=0, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=5)

label_weight = tk.Label(root, text="Weight (in kg):")
label_weight.grid(row=1, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=5)

label_bmi_result = tk.Label(root, text="BMI: -", font=("Helvetica", 14))
label_bmi_result.grid(row=2, columnspan=2, pady=10)

# Buttons
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.grid(row=3, columnspan=2, pady=10)

button_view_history = tk.Button(root, text="View BMI History", command=view_history)
button_view_history.grid(row=4, columnspan=2, pady=10)

# BMI History Listbox
listbox_history = tk.Listbox(root, width=50, height=10)
listbox_history.grid(row=5, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
