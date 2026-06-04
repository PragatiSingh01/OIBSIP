from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter valid values")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI = {bmi:.2f}\nCategory = {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only")

# Main Window
root = Tk()
root.title("BMI Calculator")
root.geometry("350x300")

# Heading
Label(root, text="BMI Calculator",
      font=("Arial", 16, "bold")).pack(pady=10)

# Weight
Label(root, text="Weight (kg)").pack()
weight_entry = Entry(root)
weight_entry.pack()

# Height
Label(root, text="Height (m)").pack()
height_entry = Entry(root)
height_entry.pack()

# Button
Button(root, text="Calculate BMI",
       command=calculate_bmi).pack(pady=10)

# Result
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()