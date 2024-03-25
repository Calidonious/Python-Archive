import customtkinter as ctk
import math


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

class DecayRateCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Decay Rate Calculator")

        self.label_mass = ctk.CTkLabel(master, text="Enter mass (kg):")
        self.label_mass.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.mass_entry = ctk.CTkEntry(master)
        self.mass_entry.grid(row=0, column=1, padx=5, pady=5)
        self.mass_entry.configure(placeholder_text="0")

        self.label_material = ctk.CTkLabel(master, text="Select material:")
        self.label_material.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.material_combobox = ctk.CTkComboBox(master, values=list(RadioactiveMaterials.keys()))
        self.material_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.material_combobox.set("Select a material")

        self.calculate_button = ctk.CTkButton(master, text="Calculate", command=self.calculate_decay_rate)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = ctk.CTkLabel(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.half_life = None

    def set_half_life(self):
        material = self.material_combobox.get()
        self.half_life = RadioactiveMaterials[material]
        self.result_label.configure(text=f"Selected material: {material}, Half-life: {self.half_life} seconds")

    def calculate_decay_rate(self):
        self.set_half_life()
        try:
            mass = float(self.mass_entry.get())

            if mass <= 0 or self.half_life is None:
                raise ValueError("Mass and half-life must be positive numbers and material must be selected.")

            decay_rate = math.log(2) / self.half_life * mass
            decay_rate_per_minute = decay_rate * 60
            decay_rate_per_hour = decay_rate * 3600
            decay_rate_per_day = decay_rate * 3600 * 24  # Convert from kg/s to kg/day

            # Calculate decay time
            decay_time_seconds = mass / decay_rate
            decay_time_minutes = decay_time_seconds / 60
            decay_time_hours = decay_time_minutes / 60
            decay_time_days = decay_time_hours / 24
            decay_time_months = decay_time_days / 30.4375
            decay_time_years = decay_time_days / 365.25

            self.result_label.configure(text=f"Decay rate of your selected material:\n"
                                          f"Kg/Second: {decay_rate:.14f}\n"
                                          f"Kg/Minute: {decay_rate_per_minute:.14f}\n"
                                          f"Kg/Hour: {decay_rate_per_hour:.14f}\n"
                                          f"Kg/Day: {decay_rate_per_day:.14f}\n\n"
                                          
                                          f"Decay time of your selected mass:\n"
                                          f"Seconds: {decay_time_seconds:.2f}\n"
                                          f"Minutes: {decay_time_minutes:.2f}\n"
                                          f"Hours: {decay_time_hours:.2f}\n"
                                          f"Days: {decay_time_days:.2f}\n"
                                          f"Months: {decay_time_months:.2f}\n"
                                          f"Years: {decay_time_years:.2f}")
        except ValueError as ve:
            self.result_label.configure(text=str(ve))


# Dictionary mapping radioactive materials to their half-lives in seconds
RadioactiveMaterials = {
    "Uranium-238": 4.468e9,           # Half-life: 4.468 billion years
    "Plutonium-239": 2.41e4,          # Half-life: 24,100 years
    "Carbon-14": 5730,                # Half-life: 5730 years
    "Radium-226": 1600*365*24*3600,   # Half-life: 1600 years
    "Potassium-40": 1.277e9,          # Half-life: 1.277 billion years
    "Thorium-232": 1.405e10,          # Half-life: 14.05 billion years
    "Strontium-90": 28.8*365*24*3600, # Half-life: 28.8 years
    "Cesium-137": 30*365*24*3600,     # Half-life: 30 years
    "Iodine-131": 8.02*24*3600,       # Half-life: 8.02 days
    "Tritium": 4500*365*24*3600,      # Half-life: 4500 years
    "Radon-222": 3.8235*24*3600,      # Half-life: 3.8235 days
    "Americium-241": 432.2*365*24*3600,# Half-life: 432.2 years
    "Neptunium-237": 2.14e6,          # Half-life: 2.14 million years
    "Strontium-89": 50.5*365*24*3600, # Half-life: 50.5 days
    "Cobalt-60": 5.271*365*24*3600,   # Half-life: 5.271 years
    "Polonium-210": 138.376*24*3600,  # Half-life: 138.376 days
    "Ruthenium-106": 1.0104*365*24*3600,# Half-life: 1.0104 years
    "Promethium-145": 17.7*24*3600,   # Half-life: 17.7 days
    "Barium-133": 10.51*365*24*3600,  # Half-life: 10.51 years
    "Yttrium-90": 64*365*24*3600,     # Half-life: 64 hours
}


if __name__ == "__main__":
    root = ctk.CTk()
    app = DecayRateCalculator(root)
    root.mainloop()



