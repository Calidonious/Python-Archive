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


class CoinFlipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coin Flipper")
        self.root.resizable(False, False)

        # Variables
        self.result_var = tk.StringVar()

        # Create widgets
        self.flip_button = ctk.CTkButton(root, text="Flip Coin", command=self.flip_coin)
        self.result_label = ctk.CTkLabel(root, textvariable=self.result_var)

        # Grid layout
        self.flip_button.grid(row=0, column=0, padx=10, pady=10)
        self.result_label.grid(row=1, column=0, padx=10, pady=10)

    def flip_coin(self):
        result = random.choice(['Heads', 'Tails'])
        self.result_var.set(f"The coin landed on: {result}")


if __name__ == "__main__":
    master = ctk.CTk()
    app = CoinFlipApp(master)
    master.mainloop()