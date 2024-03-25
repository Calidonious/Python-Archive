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

class PotentialEnergyCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Potential Energy Calculator")

        self.label = ctk.CTkLabel(master, text="Enter mass (kg):")
        self.label.pack()

        self.mass_entry = ctk.CTkEntry(master)
        self.mass_entry.pack()

        self.calculate_button = ctk.CTkButton(master, text="Calculate", command=self.calculate_energy)
        self.calculate_button.pack()

        self.result_label = ctk.CTkLabel(master, text="")
        self.result_label.pack()

    def calculate_energy(self):
        try:
            mass = float(self.mass_entry.get())
            g = 9.81  # Acceleration due to gravity in m/s^2
            energy = mass * g

            self.result_label.configure(text=f"Total potential energy: {energy:.2f} J")
        except ValueError:
            self.result_label.configure(text="Please enter a valid mass.")


if __name__ == "__main__":
    root = ctk.CTk()
    app = PotentialEnergyCalculator(root)
    root.mainloop()
