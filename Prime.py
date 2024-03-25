import tkinter as tk
import customtkinter as ctk
from math import isqrt


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


class PrimeNumberFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Prime Number Finder")
        self.root.resizable(False, False)

        self.label_start = ctk.CTkLabel(root, text="Start at:")
        self.label_start.grid(row=0, column=0, padx=10, pady=10)

        self.start_var = tk.StringVar()
        self.start_var.set("0")
        self.entry_start = ctk.CTkEntry(root, textvariable=self.start_var)
        self.entry_start.grid(row=0, column=1, padx=10, pady=10)

        self.label_stop = ctk.CTkLabel(root, text="Stop at:")
        self.label_stop.grid(row=1, column=0, padx=10, pady=10)

        self.stop_var = tk.StringVar()
        self.stop_var.set("1000")
        self.entry_stop = ctk.CTkEntry(root, textvariable=self.stop_var)
        self.entry_stop.grid(row=1, column=1, padx=10, pady=10)

        self.result_var = tk.StringVar()
        self.result_var.set("Prime numbers will be displayed here.")

        self.result_frame = ctk.CTkScrollableFrame(root, width=600, height=50)
        self.result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.label_result = ctk.CTkLabel(self.result_frame, textvariable=self.result_var)
        self.label_result.grid(row=0, column=0, padx=10, pady=10)

        self.num_columns = 10 # Number of columns in the matrix
        self.find_button = ctk.CTkButton(root, text="Find Primes", command=self.find_primes)
        self.find_button.grid(row=3, column=0, columnspan=2, pady=10)

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    def find_primes(self):
        try:
            start = int(self.start_var.get())
            stop = int(self.stop_var.get())
            primes = [num for num in range(start, stop + 1) if self.is_prime(num)]

            result_text = ""
            for i, prime in enumerate(primes, start=1):
                result_text += f"{prime}, "
                if i % self.num_columns == 0:
                    result_text = result_text.rstrip(", ") + ".\n"

            if primes:
                result_text = result_text.rstrip(", ") + "."  # Remove trailing comma before the dot.
            else:
                result_text = "No prime numbers in the given range."

            self.result_var.set(result_text)
        except ValueError:
            self.result_var.set("Please enter valid integer values for start and stop.")


if __name__ == "__main__":
    master = ctk.CTk()
    app = PrimeNumberFinder(master)
    master.mainloop()

