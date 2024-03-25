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


class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.resizable(False, False)

        # Variables
        self.temperature_var = tk.StringVar()
        self.temperature_var.set("0.00")
        self.temperature_scale_var = tk.StringVar(value="Celsius")

        # Create widgets
        self.label_temperature = ctk.CTkLabel(root, text="Enter Temperature:")
        self.entry_temperature = ctk.CTkEntry(root, textvariable=self.temperature_var)

        self.label_scale = ctk.CTkLabel(root, text="Select Scale:")
        self.temperature_scale = ctk.CTkComboBox(root, values=['Celsius', 'Fahrenheit', 'Kelvin'], variable=self.temperature_scale_var)
        self.temperature_scale.set('Celsius')  # Set default value

        self.convert_button = ctk.CTkButton(root, text="Convert", command=self.convert_temperature)
        self.result_label = ctk.CTkLabel(root, text="")

        # Grid layout
        self.label_temperature.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_temperature.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.label_scale.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.temperature_scale.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_var.get())
        except ValueError:
            self.result_label.configure(text="Please enter a valid number.")
            return

        choice = self.temperature_scale_var.get()

        if choice == 'Celsius':
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.15
            self.result_label.configure(text=f"{temperature}°C is equal to:\n{fahrenheit:.2f}°F\n{kelvin:.2f}K")
        elif choice == 'Fahrenheit':
            celsius = (temperature - 32) * 5/9
            kelvin = (temperature - 32) * 5/9 + 273.15
            self.result_label.configure(text=f"{temperature}°F is equal to:\n{celsius:.2f}°C\n{kelvin:.2f}K")
        elif choice == 'Kelvin':
            celsius = temperature - 273.15
            fahrenheit = (temperature - 273.15) * 9/5 + 32
            self.result_label.configure(text=f"{temperature}K is equal to:\n{celsius:.2f}°C\n{fahrenheit:.2f}°F")


if __name__ == "__main__":
    master = ctk.CTk()
    app = TemperatureConverterApp(master)
    master.mainloop()
