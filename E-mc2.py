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

class MassToEnergyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Mass to Energy Converter")

        self.label_mass = ctk.CTkLabel(master, text="Enter mass (kg):")
        self.label_mass.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.mass_entry = ctk.CTkEntry(master)
        self.mass_entry.grid(row=0, column=1, padx=5, pady=5)

        self.calculate_button = ctk.CTkButton(master, text="Calculate", command=self.calculate_energy)
        self.calculate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = ctk.CTkLabel(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def calculate_energy(self):
        try:
            mass = float(self.mass_entry.get())

            if mass <= 0:
                raise ValueError("Mass must be a positive number.")

            speed_of_light = 299792458  # Speed of light in meters per second
            energy = mass * (speed_of_light ** 2)

            # Convert energy to various metrics
            energy_in_hot_dogs = energy / 310000  # Average energy in a hotdog (310,000 joules)
            energy_in_suns = energy / 4e26  # Energy output of the sun in joules (4 x 10^26)
            energy_in_bigmacs = energy / 2450000  # Average energy in a Big Mac (2,450,000 joules)
            energy_in_kilowatt_hours = energy / 3600000  # 1 kilowatt-hour = 3.6 million joules
            energy_in_bananas = energy / 40000000  # Average energy in a banana (40,000,000 joules)
            energy_in_lightning_strikes = energy / 1000000000  # Average energy in a lightning strike (1 billion joules)
            energy_in_atomic_bombs = energy / 4.184e12  # Average energy in a ton of TNT (4.184 x 10^12 joules)
            energy_in_aa_batteries = energy / (2.4 * 3600)  # Average energy in an AA battery (2.4 watt-hours)
            energy_in_pizzas = energy / 2000000  # Average energy in a large pizza (2,000,000 joules)
            energy_in_coffee_cups = energy / 200000  # Average energy in a cup of coffee (200,000 joules)
            energy_in_spaceship_launches = energy / 3.9e10  # Energy used in a space shuttle launch (39 billion joules)
            energy_in_earthquakes = energy / 1e15  # Energy released by a magnitude 6 earthquake (1 trillion joules)
            energy_in_eiffel_tower_elevations = energy / 750000000000  # Energy required to lift the Eiffel Tower (750 billion joules)
            energy_in_bitcoins = energy / 8.155e16  # Energy consumed for mining one bitcoin (81,550,000,000,000,000 joules)
            energy_in_cars_driven = energy / 9e6  # Average energy consumption of a car driven for one hour (9 million joules)
            energy_in_human_calories = energy / 4184  # Energy equivalent of one dietary calorie (4,184 joules)
            energy_in_hurricanes = energy / 6.2e14  # Average energy released by a hurricane in a day (620 trillion joules)
            energy_in_airplane_flights = energy / 32000000  # Average energy consumption of a flight across the US (32 million joules)
            energy_in_tnt = energy / 4.184e9  # Average energy in one gram of TNT (4.184 x 10^9 joules)
            energy_in_c4 = energy / 6.189e9  # Average energy in one gram of C4 explosive (6.189 x 10^9 joules)


            # Update result label text
            result_text = f"Energy equivalent: {energy:.2f} joules\n\n"
            result_text += f"Weird Conversion metrics:\n\n"
            result_text += f"Foods:\n"
            result_text += f"Equivalent to {energy_in_hot_dogs:.2f} hot dogs\n"
            result_text += f"Equivalent to {energy_in_bigmacs:.2f} Big Macs\n"
            result_text += f"Equivalent to {energy_in_bananas:.2f} bananas\n"
            result_text += f"Equivalent to {energy_in_pizzas:.2f} large pizzas\n"
            result_text += f"Equivalent to {energy_in_coffee_cups:.2f} cups of coffee\n"
            result_text += f"Equivalent to {energy_in_human_calories:.2f} dietary calories\n\n"

            result_text += f"Power:\n"
            result_text += f"Equivalent to {energy_in_kilowatt_hours:.2f} kilowatt-hours\n"
            result_text += f"Equivalent to {energy_in_aa_batteries:.2f} AA batteries\n"
            result_text += f"Equivalent to {energy_in_bitcoins:.10f} bitcoins mined\n\n"

            result_text += f"Transportation:\n"
            result_text += f"Equivalent to {energy_in_cars_driven:.2f} hours of driving a car\n"
            result_text += f"Equivalent to {energy_in_spaceship_launches:.2f} space shuttle launches\n"
            result_text += f"Equivalent to {energy_in_airplane_flights:.2f} flights across the US\n"
            result_text += f"Equivalent to {energy_in_eiffel_tower_elevations:.2f} times lifting the Eiffel Tower\n\n"

            result_text += f"Explosive things:\n"
            result_text += f"Equivalent to {energy_in_atomic_bombs:.2f} atomic bombs\n"
            result_text += f"Equivalent to {energy_in_tnt:.2f} grams of TNT\n"
            result_text += f"Equivalent to {energy_in_c4:.2f} grams of C4 explosive\n"
            result_text += f"Equivalent to {energy_in_suns:.10f} suns\n\n"

            result_text += f"Natural disasters:\n"
            result_text += f"Equivalent to {energy_in_lightning_strikes:.2f} lightning strikes\n"
            result_text += f"Equivalent to {energy_in_earthquakes:.2f} magnitude 6 earthquakes\n"
            result_text += f"Equivalent to {energy_in_hurricanes:.2f} hurricanes in terms of energy"

            self.result_label.configure(text=result_text)

        except ValueError as ve:
            self.result_label.configure(text=str(ve))

if __name__ == "__main__":
    root = ctk.CTk()
    app = MassToEnergyConverter(root)
    root.mainloop()
