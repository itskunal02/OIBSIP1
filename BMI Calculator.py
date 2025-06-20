import tkinter as tk

def calculate_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get()) / 100
    bmi = weight / (height ** 2)
    result.set(f"BMI: {bmi:.2f}")

app = tk.Tk()
app.title("BMI Calculator")

tk.Label(app, text="Height (cm)").pack()
entry_height = tk.Entry(app)
entry_height.pack()

tk.Label(app, text="Weight (kg)").pack()
entry_weight = tk.Entry(app)
entry_weight.pack()

result = tk.StringVar()
tk.Label(app, textvariable=result).pack()

tk.Button(app, text="Calculate", command=calculate_bmi).pack()
app.mainloop()
