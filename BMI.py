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


class BMIConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.resizable(False, False)

        # Variables
        self.weight_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.bmi_result_var = tk.StringVar()

        # Variable initialization
        self.weight_var.set("0.00")
        self.height_var.set("0.00")

        # Create widgets
        self.label_weight = ctk.CTkLabel(root, text="Enter Weight:")
        self.entry_weight = ctk.CTkEntry(root, textvariable=self.weight_var)

        self.label_height = ctk.CTkLabel(root, text="Enter Height:")
        self.entry_height = ctk.CTkEntry(root, textvariable=self.height_var)

        self.label_units = ctk.CTkLabel(root, text="Units:")
        self.units_combobox = ctk.CTkComboBox(root, values=['kg/cm', 'lbs/inches'], state="readonly")
        self.units_combobox.set('kg/cm')  # Set default value

        self.calculate_button = ctk.CTkButton(root, text="Calculate BMI", command=self.calculate_bmi)

        self.result_label = ctk.CTkLabel(root, textvariable=self.bmi_result_var)

        # Grid layout
        self.label_weight.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.label_height.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_height.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.label_units.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.units_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_var.get())
            height = float(self.height_var.get())
        except tk.TclError:
            self.bmi_result_var.set("Invalid input. Please enter valid numbers.")
            return

        units = self.units_combobox.get()

        if units == 'kg/cm':
            bmi = weight / ((height / 100) ** 2)
        elif units == 'lbs/inches':
            bmi = (weight / (height ** 2)) * 703
        else:
            self.bmi_result_var.set("Invalid units. Please select valid units.")
            return

        self.bmi_result_var.set(f"Your BMI is: {bmi:.2f}")


if __name__ == "__main__":
    master = ctk.CTk()
    app = BMIConverterApp(master)
    master.mainloop()