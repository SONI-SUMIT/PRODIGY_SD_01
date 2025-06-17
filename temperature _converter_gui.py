import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result.set(f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K")

        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result.set(f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K")

        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result.set(f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter Temperature:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack()

unit_var = tk.StringVar(value="Celsius")
tk.Label(root, text="Select Unit:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
tk.OptionMenu(root, unit_var, "Celsius", "Fahrenheit", "Kelvin").pack()


tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temperature).pack(pady=20)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue", bg="#f0f0f0").pack()

root.mainloop()
