import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime, timedelta
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


class RandomDateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Date App")
        self.root.resizable(False, False)

        # Variables
        self.year_var = tk.StringVar()
        self.year_var.set("2024")
        self.month_var = tk.StringVar()
        self.month_var.set("01")
        self.generated_date_var = tk.StringVar()

        # Create widgets
        self.label_year = ctk.CTkLabel(root, text="Enter Year:")
        self.entry_year = ctk.CTkEntry(root, textvariable=self.year_var)

        self.label_month = ctk.CTkLabel(root, text="Enter Month:")
        self.entry_month = ctk.CTkEntry(root, textvariable=self.month_var)

        self.button_generate_date = ctk.CTkButton(root, text="Generate Date", command=self.generate_date)

        self.label_generated_date = ctk.CTkLabel(root, text="Generated Date:")
        self.label_generated_date_value = ctk.CTkLabel(root, textvariable=self.generated_date_var)

        self.button_save_date = ctk.CTkButton(root, text="Save Date", command=self.save_date)

        self.label_error = ctk.CTkLabel(root, text="")

        # Grid layout
        self.label_year.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_year.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.label_month.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_month.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button_generate_date.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_generated_date.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.label_generated_date_value.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.button_save_date.grid(row=4, column=0, columnspan=2, pady=10)

        self.label_error.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_date(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            user_date = datetime(year, month, 1)
            days_in_month = (user_date.replace(month=user_date.month % 12 + 1, day=1) - timedelta(days=1)).day
            day = random.randint(1, days_in_month)
            generated_date = datetime(year, month, day)
            self.generated_date_var.set(generated_date.strftime("%Y-%m-%d"))
        except ValueError:
            self.label_error.configure(text="Error! Invalid year or month. Please enter valid values.")

    def save_date(self):
        if not self.generated_date_var.get():
            self.label_error.configure(text="Warning! Please generate a date before saving.")
            return

        response = messagebox.showinfo("Date saved!", "The program will now save your specified date!")
        if response:
            with open("target_date.txt", "w") as file:
                file.write(self.generated_date_var.get())
            self.label_error.configure(text="Saved! Date saved successfully.")


if __name__ == "__main__":
    master = ctk.CTk()
    app = RandomDateApp(master)
    master.mainloop()
