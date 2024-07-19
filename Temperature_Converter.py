import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_fahrenheit_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_celsius_result.config(text=f"{celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Celsius to Fahrenheit
label_celsius = tk.Label(root, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10)

entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

button_convert_to_fahrenheit = tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
button_convert_to_fahrenheit.grid(row=0, column=2, padx=10, pady=10)

label_fahrenheit_result = tk.Label(root, text="Result: °F")
label_fahrenheit_result.grid(row=1, column=1, padx=10, pady=10)

# Fahrenheit to Celsius
label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(row=2, column=0, padx=10, pady=10)

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=2, column=1, padx=10, pady=10)

button_convert_to_celsius = tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_convert_to_celsius.grid(row=2, column=2, padx=10, pady=10)

label_celsius_result = tk.Label(root, text="Result: °C")
label_celsius_result.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
