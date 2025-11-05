#I acknowledge the use of Microsoft Copilot (https://copilot.microsoft.com/) to create the code in this file

import random

# The computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Ask the player to guess
guess = int(input("Take a guess: "))

# Check if the guess is correct
if guess == secret_number:
    print("🎉 You guessed it! Well done!")
else:
    print(f"❌ Nope! The number was {secret_number}. Better luck next time!")
