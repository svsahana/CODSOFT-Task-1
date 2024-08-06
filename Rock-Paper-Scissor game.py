import tkinter as tk
from tkinter import messagebox
import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"


def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Show the result in a messagebox
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")


def create_gui():
    root = tk.Tk()
    root.title("Rock-Paper-Scissors")

    tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Rock", command=lambda: play_game('rock')).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(root, text="Paper", command=lambda: play_game('paper')).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(root, text="Scissors", command=lambda: play_game('scissors')).pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
