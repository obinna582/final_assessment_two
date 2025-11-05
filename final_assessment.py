
# I acknowledge the use of Microsoft Copilot (https://copilot.microsoft.com/) to create the code in this file

import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("300x200")

# Generate the secret number
secret_number = random.randint(1, 10)

# Function to check the guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret_number:
            result_label.config(text="🎉 You guessed it! Well done!")
        else:
            result_label.config(text=f"❌ Nope! It was {secret_number}. Try again!")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
    
    # Clear the entry box after each guess
    entry.delete(0, tk.END)

# GUI elements
instruction_label = tk.Label(window, text="Guess a number between 1 and 10:")
instruction_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

guess_button = tk.Button(window, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the GUI loop
window.mainloop()
