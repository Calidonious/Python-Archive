import tkinter as tk
import customtkinter as ctk


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


class PhCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("pH Checker")
        self.root.resizable(False, False)

        # Variables
        self.pH_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Variable initialization
        self.pH_var.set("0")

        # Create widgets
        self.label_pH = ctk.CTkLabel(root, text="Enter pH value:")
        self.entry_pH = ctk.CTkEntry(root, textvariable=self.pH_var)
        self.check_button = ctk.CTkButton(root, text="Check pH", command=self.check_ph)
        self.result_label = ctk.CTkLabel(root, textvariable=self.result_var)

        # Grid layout
        self.label_pH.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_pH.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.check_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def check_ph(self):
        try:
            ph_value = float(self.pH_var.get())
        except ValueError:
            self.result_var.set("Please enter a valid number.")
            return

        if 0 <= ph_value <= 14:
            if 7 < ph_value <= 14:
                self.result_var.set("Basic (Alkaline)")
            elif 6 <= ph_value <= 8:
                self.result_var.set("Neutral")
            elif 0 <= ph_value < 7:
                self.result_var.set("Acidic")
        else:
            self.result_var.set("Invalid pH value. Please enter a value between 0 and 14.")


if __name__ == "__main__":
    master = ctk.CTk()
    app = PhCheckerApp(master)
    master.mainloop()