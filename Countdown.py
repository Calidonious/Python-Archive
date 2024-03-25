import tkinter as tk
import customtkinter as ctk
from datetime import datetime


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


class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown App")
        self.root.resizable(False, False)

        # Variables
        self.target_date_var = tk.StringVar()
        self.countdown_var = tk.StringVar()
        self.error_str = tk.StringVar()

        # Create widgets
        self.label_target_date = ctk.CTkLabel(root, text="Target Date:")
        self.entry_target_date = ctk.CTkEntry(root, textvariable=self.target_date_var, placeholder_text=self.error_str.get())
        self.button_set_target_date = ctk.CTkButton(root, text="Set Target Date", command=self.set_target_date)
        self.label_countdown = ctk.CTkLabel(root, text="Countdown:")
        self.label_countdown_value = ctk.CTkLabel(root, textvariable=self.countdown_var)

        # Grid layout
        self.label_target_date.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_target_date.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.button_set_target_date.grid(row=1, column=0, columnspan=2, pady=10)
        self.label_countdown.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.label_countdown_value.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Load target date from file
        self.load_target_date()

        # Update countdown display
        self.update_countdown_display()

    def set_target_date(self):
        try:
            target_date = datetime.strptime(self.target_date_var.get(), "%Y-%m-%d")
        except ValueError:
            self.error_str.set("Error! Invalid date format. Please use YYYY-MM-DD.")
            return

        # Save target date to file
        with open("target_date.txt", "w") as file:
            file.write(target_date.strftime("%Y-%m-%d"))

        # Update countdown display
        self.update_countdown_display()

    def load_target_date(self):
        try:
            with open("target_date.txt", "r") as file:
                stored_date = file.read().strip()
                if stored_date:
                    self.target_date_var.set(stored_date)
        except FileNotFoundError:
            pass

    def update_countdown_display(self):
        try:
            target_date = datetime.strptime(self.target_date_var.get(), "%Y-%m-%d")
        except ValueError:
            return

        current_date = datetime.now()
        time_difference = target_date - current_date

        if time_difference.total_seconds() < 0:
            self.countdown_var.set("Date expired")
        else:
            years, remainder = divmod(time_difference.days, 365)
            months, days = divmod(remainder, 30)
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            countdown_text = f"{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
            self.countdown_var.set(countdown_text)


if __name__ == "__main__":
    master = ctk.CTk()
    app = CountdownApp(master)
    master.mainloop()