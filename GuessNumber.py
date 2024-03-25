import tkinter as tk
import customtkinter as ctk
import random


# Lookup and set saved theme
def set_appear_theme():

    # Grabbing theme from txt file
    with open("theme.txt", 'r') as theme:
        color_theme = theme.read()

    # Theme Color logic
    if color_theme == "pink":
        ctk.set_default_color_theme("pink.json")
    elif color_theme == "purple":
        ctk.set_default_color_theme("purple.json")
    elif color_theme == "red":
        ctk.set_default_color_theme("red.json")
    elif color_theme == "orange":
        ctk.set_default_color_theme("orange.json")
    elif color_theme == "yellow":
        ctk.set_default_color_theme("yellow.json")
    elif color_theme == "light-green":
        ctk.set_default_color_theme("light_green.json")
    elif color_theme == "green":
        ctk.set_default_color_theme("green")
    elif color_theme == "dark-green":
        ctk.set_default_color_theme("dark_green.json")
    elif color_theme == "light-blue":
        ctk.set_default_color_theme("light_blue.json")
    elif color_theme == "blue":
        ctk.set_default_color_theme("blue")
    elif color_theme == "dark-blue":
        ctk.set_default_color_theme("dark-blue")


    # Grabbing appearance from txt file
    with open("appearance.txt", 'r') as theme:
        appearance_theme = theme.read()

    # Set appearance
    ctk.set_appearance_mode(appearance_theme)

set_appear_theme()


class NumberGuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        # Variables
        self.random_number = 0
        self.remaining_chances = 5
        self.guess_var = tk.StringVar()
        self.guess_var.set("Input a number!")
        self.result_var = tk.StringVar()

        # Create widgets
        self.label_instruction = ctk.CTkLabel(root, text="Guess the Number (1-10):")
        self.entry_guess = ctk.CTkEntry(root, textvariable=self.guess_var)
        self.guess_button = ctk.CTkButton(root, text="Guess", command=self.make_guess)
        self.reset_button = ctk.CTkButton(root, text="Reset Game", command=self.reset_game)
        self.result_label = ctk.CTkLabel(root, textvariable=self.result_var)

        # Generate the initial random number
        self.generate_random_number()

        # Grid layout
        self.label_instruction.grid(row=0, column=0, padx=10, pady=10)
        self.entry_guess.grid(row=0, column=1, padx=10, pady=10)
        self.guess_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.reset_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_random_number(self):
        self.random_number = random.randint(1, 10)

    def make_guess(self):
        try:
            user_guess = int(self.guess_var.get())
        except ValueError:
            self.result_var.set("Please enter a valid number.")
            return

        if 1 <= user_guess <= 10:
            self.check_guess(user_guess)
        else:
            self.result_var.set("Please enter a number between 1 and 10.")

    def check_guess(self, user_guess):
        if user_guess == self.random_number:
            self.result_var.set("Congratulations! You guessed the correct number!")
            self.guess_button["state"] = "disabled"
        else:
            self.remaining_chances -= 1
            if self.remaining_chances > 0:
                self.result_var.set(f"Wrong guess! {self.remaining_chances} chances remaining.")
            else:
                self.result_var.set(f"Sorry, you lost. The correct number was {self.random_number}.")
                self.guess_button["state"] = "disabled"

    def reset_game(self):
        self.generate_random_number()
        self.remaining_chances = 5
        self.guess_var.set("")
        self.result_var.set("")
        self.guess_button["state"] = "normal"


if __name__ == "__main__":
    master = ctk.CTk()
    app = NumberGuessingGameApp(master)
    master.mainloop()