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


class LotterySimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lottery Simulator")

        # Variables
        self.user_regular_numbers_var = [tk.StringVar() for _ in range(6)]
        self.user_magic_number_var = tk.StringVar()
        self.lottery_regular_numbers = []
        self.lottery_magic_number = 0
        self.result_var = tk.StringVar()

        # Create widgets
        self.user_magic_number_var.set("0")
        for var in self.user_regular_numbers_var:
            var.set("0")

        self.label_user_regular = ctk.CTkLabel(root, text="Enter 6 regular numbers (1-40):")
        self.entry_user_regular = [ctk.CTkEntry(root, textvariable=self.user_regular_numbers_var[i], width=10) for i in range(6)]
        self.label_user_magic = ctk.CTkLabel(root, text="Enter the magic number (1-15):")
        self.entry_user_magic = ctk.CTkEntry(root, textvariable=self.user_magic_number_var, width=10)
        self.generate_button = ctk.CTkButton(root, text="Generate Lottery Numbers", command=self.generate_lottery_numbers)
        self.result_label = ctk.CTkLabel(root, textvariable=self.result_var)

        # Grid layout
        self.label_user_regular.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        for i, entry in enumerate(self.entry_user_regular):
            entry.grid(row=i + 1, column=0, padx=5, pady=5, sticky="nesw")
        self.label_user_magic.grid(row=7, column=0, padx=10, pady=10, columnspan=2)
        self.entry_user_magic.grid(row=8, column=0, padx=5, pady=5, sticky="nesw")
        self.generate_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=10, column=0, columnspan=2, pady=10)

    def generate_lottery_numbers(self):
        try:
            user_regular_numbers = [int(self.user_regular_numbers_var[i].get()) for i in range(6)]
            user_magic_number = int(self.user_magic_number_var.get())
        except ValueError:
            self.result_var.set("Please enter a valid number.")
            return

        # Check if numbers are within valid ranges
        if not all(1 <= num <= 40 for num in user_regular_numbers) or not (1 <= user_magic_number <= 15):
            self.result_var.set("Invalid numbers. Please enter numbers within the specified ranges.")
            return

        # Check for duplicate numbers
        if len(set(user_regular_numbers)) != 6 or len(set(user_regular_numbers + [user_magic_number])) != 7:
            self.result_var.set("Duplicate numbers are not allowed.")
            return

        # Generate lottery numbers
        self.lottery_regular_numbers = random.sample(range(1, 41), 6)
        self.lottery_magic_number = random.randint(1, 15)

        # Check how many numbers are correct
        correct_numbers = set(self.lottery_regular_numbers).intersection(user_regular_numbers)
        correct_magic = self.lottery_magic_number == user_magic_number

        # Display results
        self.result_var.set(
            f"Your Selections:\nRegular Numbers: {user_regular_numbers}\nMagic Number: {user_magic_number}\n\n"
            f"Lottery Numbers:\nRegular Numbers: {self.lottery_regular_numbers}\nMagic Number: {self.lottery_magic_number}\n\n"
            f"Results:\nCorrect Numbers: {len(correct_numbers)}\n"
            f"Correct Magic Number: {'Yes' if correct_magic else 'No'}"
        )


if __name__ == "__main__":
    master = ctk.CTk()
    app = LotterySimulatorApp(master)
    master.mainloop()