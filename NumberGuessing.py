import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.low = 1
        self.high = 100
        self.tries = 0
        self.secret_number = random.randint(self.low, self.high)

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.master, text="Think of a number between 1 and 100 and I will try to guess it.")
        self.label.pack(pady=10)

        self.guess_label = tk.Label(self.master, text="")
        self.guess_label.pack(pady=10)

        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=10)

        self.too_high_button = tk.Button(self.input_frame, text="Too High", command=self.too_high)
        self.too_high_button.grid(row=0, column=0, padx=10)

        self.correct_button = tk.Button(self.input_frame, text="Correct", command=self.correct_guess)
        self.correct_button.grid(row=0, column=1, padx=10)

        self.too_low_button = tk.Button(self.input_frame, text="Too Low", command=self.too_low)
        self.too_low_button.grid(row=0, column=2, padx=10)

        self.make_guess()  # Start the game with the first guess

    def too_high(self):
        self.high = self.guess - 1
        self.make_guess()

    def too_low(self):
        self.low = self.guess + 1
        self.make_guess()

    def correct_guess(self):
        messagebox.showinfo("Congratulations!", f"I guessed it in {self.tries} tries!")
        self.reset_game()

    def make_guess(self):
        self.guess = (self.low + self.high) // 2
        self.tries += 1
        self.guess_label.config(text=f"My guess is: {self.guess}")

    def reset_game(self):
        self.low = 1
        self.high = 100
        self.tries = 0
        self.secret_number = random.randint(self.low, self.high)
        self.guess_label.config(text="")
        self.make_guess()  # Start a new game with the first guess

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
