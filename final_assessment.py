
# I acknowledge the use of Microsoft Copilot (https://copilot.microsoft.com/) to create the code in this file

import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("300x250")

# Generate the secret number
secret_number = random.randint(1, 10)

# Function to check the guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret_number:
            result_label.config(text="🎉 You guessed it! Well done!")
            guess_button.config(state="disabled")  # Disable guess button
            play_again_button.pack(pady=5)         # Show play again button
        else:
            result_label.config(text="❌ Nope! Try again!")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
    
    entry.delete(0, tk.END)

# Function to reset the game
def play_again():
    global secret_number
    secret_number = random.randint(1, 10)
    result_label.config(text="")
    entry.delete(0, tk.END)
    guess_button.config(state="normal")
    play_again_button.pack_forget()  # Hide play again button

# GUI elements
instruction_label = tk.Label(window, text="Guess a number between 1 and 10:")
instruction_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

guess_button = tk.Button(window, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

play_again_button = tk.Button(window, text="Play Again", command=play_again)
# Don't show it until needed

# Run the GUI loop
window.mainloop()
