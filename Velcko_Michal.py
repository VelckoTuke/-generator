import random
import tkinter as tk
from tkinter import ttk


def generate_numbers():
    try:
        N = int(entry_N.get())
    except ValueError:
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, "Chyba: N musí byť celé číslo.\n")
        return

    D = slider_D.get()

    result_box.delete(1.0, tk.END)

    numbers = [random.random() for _ in range(N)]

    result_box.insert(tk.END, f"Vygenerované čísla (0–1):\n")
    for num in numbers:
        result_box.insert(tk.END, f"{num}\n")

    result_box.insert(tk.END, "\nPercentá:\n")
    for num in numbers:
        percent = num * 100
        result_box.insert(tk.END, f"{percent}%\n")

    result_box.insert(tk.END, f"\nZaokrúhlené na {D} miest:\n")
    for num in numbers:
        percent = num * 100
        rounded = round(percent, D)
        result_box.insert(tk.END, f"{rounded}%\n")




window = tk.Tk()
window.title("Generátor čísel 0–1 → percentá")

frame = ttk.Frame(window, padding=10)
frame.pack()

# N
ttk.Label(frame, text="N (počet čísel):").grid(row=0, column=0, sticky="w")
entry_N = ttk.Entry(frame, width=10)
entry_N.grid(row=0, column=1)
entry_N.insert(0, "10")

# Slider D
ttk.Label(frame, text="D (desatinné miesta):").grid(row=1, column=0, sticky="w")
slider_D = tk.Scale(frame, from_=0, to=10, orient=tk.HORIZONTAL)
slider_D.set(2)
slider_D.grid(row=1, column=1, sticky="we")

# Tlačitko
btn = ttk.Button(frame, text="Generovať", command=generate_numbers)
btn.grid(row=2, column=0, columnspan=2, pady=10)

# Výstupné okno
result_box = tk.Text(window, height=20, width=50)
result_box.pack()

window.mainloop()
