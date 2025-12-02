import random
import tkinter as tk


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

    # Hlavička tabuľky
    header = f"{'Číslo (0–1)':<20}{'Percentá':<20}{f'Zaokrúhlené ({D})':<20}\n"
    result_box.insert(tk.END, header)
    result_box.insert(tk.END, "-" * 60 + "\n")

    # Riadky tabuľky
    for num in numbers:
        percent = num * 100
        rounded = round(percent, D)

        line = (
            f"{num:<20}"               # číslo 0–1
            f"{percent:<20}"           # v percentách
            f"{rounded:<20}"           # zaokrúhlené
            + "\n"
        )
        result_box.insert(tk.END, line)


# UI
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

# Tlačidlo
btn = ttk.Button(frame, text="Generovať", command=generate_numbers)
btn.grid(row=2, column=0, columnspan=2, pady=10)

# Výstupné okno
result_box = tk.Text(window, height=20, width=60, font=("Courier New", 10))
result_box.pack()

window.mainloop()

