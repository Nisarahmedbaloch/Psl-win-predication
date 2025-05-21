# gui_output.py
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_output(prediction):
    output_win = tk.Toplevel()
    output_win.title("Prediction Result")
    output_win.geometry("500x400")
    output_win.configure(bg='#222831')

    tk.Label(output_win, text="Prediction Results", font=("Arial", 18, 'bold'), bg='#222831', fg='white').pack(pady=10)

    for team, prob in prediction.items():
        text = f"{team}: {round(prob * 100, 2)} %"
        tk.Label(output_win, text=text, font=("Arial", 14), bg='#393E46', fg='#00ADB5', pady=5, padx=10).pack(pady=5)

    fig, ax = plt.subplots()
    ax.bar(prediction.keys(), [p * 100 for p in prediction.values()], color=['#00ADB5', '#F8B400'])
    ax.set_ylabel("Winning Probability (%)")
    ax.set_ylim(0, 100)
    fig.patch.set_facecolor('#EEEEEE')
    canvas = FigureCanvasTkAgg(fig, master=output_win)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    output_win.mainloop()
