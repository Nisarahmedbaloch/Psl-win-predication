import tkinter as tk
from tkinter import ttk
from predictor import predict_winner
from gui_output import show_output
import pandas as pd

# Read the data and extract unique teams and venues
data = pd.read_csv("E:/excelldata/Pslalldata.csv")
teams = sorted(data['TEAM  1'].dropna().unique())
venues = sorted(data['VENUE'].dropna().unique())

def main_window():
    root = tk.Tk()
    root.title("PSL Match Win Predictor")
    root.geometry("500x500")
    root.configure(bg='#00ADB5')

    def submit():
        # Create a dictionary with inputs
        input_dict = {
            'TEAM  1': team1_var.get(),
            'TEAM  2': team2_var.get(),
            'VENUE': venue_var.get(),
            'TOSS_WINNER': toss_var.get(),
            'BAT FIRST': bat_var.get(),
            'TARGET': target_var.get()
        }

        # Strip spaces in input_dict keys to avoid extra spaces
        input_dict = {key.strip(): value for key, value in input_dict.items()}
        print("Input Dictionary:", input_dict)  # Debugging line

        # Make prediction and show output
        prediction = predict_winner(input_dict)
        show_output(prediction)

    tk.Label(root, text="PSL Match Predictor", font=("Arial", 20, 'bold'), bg='#00ADB5', fg='white').pack(pady=10)

    # Dropdown fields for user input
    def make_dropdown(label_text, variable, options):
        tk.Label(root, text=label_text, font=("Arial", 12), bg='#00ADB5', fg='white').pack()
        ttk.Combobox(root, textvariable=variable, values=options, state='readonly').pack(pady=5)

    team1_var = tk.StringVar()
    team2_var = tk.StringVar()
    venue_var = tk.StringVar()
    toss_var = tk.StringVar()
    bat_var = tk.StringVar()
    target_var = tk.IntVar()

    make_dropdown("Select Team 1", team1_var, teams)
    make_dropdown("Select Team 2", team2_var, teams)
    make_dropdown("Venue", venue_var, venues)
    make_dropdown("Toss Winner", toss_var, teams)
    make_dropdown("Bat First", bat_var, teams)

    tk.Label(root, text="Target Score", font=("Arial", 12), bg='#00ADB5', fg='white').pack()
    tk.Entry(root, textvariable=target_var).pack(pady=5)

    tk.Button(root, text="Predict Result", command=submit, font=("Arial", 14), bg='#222831', fg='white').pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_window()
