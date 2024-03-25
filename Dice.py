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


class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        # Variables
        self.num_dice_var = tk.StringVar()
        self.num_sides_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Create widgets
        self.num_dice_var.set("0")
        self.num_sides_var.set("0")
        self.label_num_dice = ctk.CTkLabel(root, text="Number of Dice:")
        self.entry_num_dice = ctk.CTkEntry(root, textvariable=self.num_dice_var)
        self.label_num_sides = ctk.CTkLabel(root, text="Number of Sides:")
        self.entry_num_sides = ctk.CTkEntry(root, textvariable=self.num_sides_var)
        self.roll_button = ctk.CTkButton(root, text="Roll Dice", command=self.roll_dice)
        self.result_frame = ctk.CTkScrollableFrame(root, width=200, height=50)
        self.result_label = ctk.CTkLabel(self.result_frame, textvariable=self.result_var)

        # Grid layout
        self.label_num_dice.grid(row=0, column=0, padx=10, pady=10)
        self.entry_num_dice.grid(row=0, column=1, padx=10, pady=10)
        self.label_num_sides.grid(row=1, column=0, padx=10, pady=10)
        self.entry_num_sides.grid(row=1, column=1, padx=10, pady=10)
        self.roll_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_frame.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=0, column=0, columnspan=2, pady=10)

    def roll_dice(self):
        try:
            num_dice = int(self.num_dice_var.get())
            num_sides = int(self.num_sides_var.get())
        except ValueError:
            self.result_var.set("Please enter a valid number.")
            return

        # Check if the number of dice and sides are valid
        if num_dice <= 0 or num_sides <= 0:
            self.result_var.set("Please enter positive values for the number of dice and sides.")
            return

        # Roll the dice
        results = [random.randint(1, num_sides) for _ in range(num_dice)]

        # Display results in a matrix
        matrix = [results[i:i + 10] for i in range(0, len(results), 10)]
        formatted_results = "\n".join(" ".join(map(str, line)) for line in matrix)

        # Display the results
        self.result_var.set(f"Results:\n{formatted_results}")


if __name__ == "__main__":
    master = ctk.CTk()
    app = DiceRollerApp(master)
    master.mainloop()