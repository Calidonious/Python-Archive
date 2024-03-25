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


class TestGradesConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Grades Converter")
        self.root.resizable(False, False)

        # Variables
        self.correct_var = tk.StringVar()
        self.total_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Variable initialization
        self.correct_var.set('0')
        self.total_var.set("0")

        # Create widgets
        self.label_correct = ctk.CTkLabel(root, text="Enter number of correct answers:")
        self.entry_correct = ctk.CTkEntry(root, textvariable=self.correct_var)
        self.label_total = ctk.CTkLabel(root, text="Enter total number of questions:")
        self.entry_total = ctk.CTkEntry(root, textvariable=self.total_var)
        self.convert_button = ctk.CTkButton(root, text="Convert to Percentage", command=self.convert_to_percentage)
        self.result_label = ctk.CTkLabel(root, textvariable=self.result_var)

        # Grid layout
        self.label_correct.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_correct.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.label_total.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_total.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_to_percentage(self):
        try:
            correct = int(self.correct_var.get())
            total = int(self.total_var.get())
        except ValueError:
            self.result_var.set("Please enter a valid number.")
            return

        if 0 <= correct <= total:
            percentage = (correct / total) * 100
            self.result_var.set(f"Your percentage is: {percentage:.2f}%")
            if percentage >= 60:
                self.result_var.set(f"Congratulations! You passed with {percentage:.2f}%.")
            else:
                self.result_var.set(f"You failed with {percentage:.2f}%. Better luck next time.")
        else:
            self.result_var.set("Invalid input. Please enter valid values.")


if __name__ == "__main__":
    master = ctk.CTk()
    app = TestGradesConverterApp(master)
    master.mainloop()