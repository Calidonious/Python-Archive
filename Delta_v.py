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


class RocketCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rocket Payload Calculator")
        self.resizable(False, False)

        master_menu_frame = ctk.CTkFrame(self)
        master_menu_frame.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        menu_frame= ctk.CTkFrame(master_menu_frame)
        menu_frame.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        self.intro_label = ctk.CTkLabel(menu_frame, text="This program calculates all the specs of the rocket,\n"
                                                   "You will need to get your payload(satellite) into orbit,\n"
                                                   "At your desired altitude, it asks you to select a engine,\n"
                                                   "As well as the amount of engines,\n"
                                                   "Your rocket needs to have a thrust to weight ratio of 1.00,\n"
                                                   "In order to fly ex. 0.75 means your engine can lift %75,\n"
                                                   "Of the rocket weight and you need to add more engines.\n"
                                                   "The average range of satellite weights is 100-3500kg in real life.")
        self.intro_label.grid(row=0, columnspan=2, padx=10, pady=10)

        self.warning_label = ctk.CTkLabel(menu_frame, text="Limitations of this program!\n"
                                                     "\n-1. It assumes your rocket is single stage,\n"
                                                     "And that your taking the whole rocket to space,\n"
                                                     "Which is not efficient compared to multi-stage.\n"
                                                     "\n-2. It assumes your going to go straight up,\n"
                                                     "And not use a curved assent profile,\n"
                                                     "Which is obviously way more efficient.\n"
                                                     "\n-3. It assumes gravity is constant, it is not,\n"
                                                     "In real life gravity decreases exponentially the farther from earth you are,\n"
                                                     "Meaning you will need less thrust and use less fuel as you ascend.\n"
                                                     "\n-4. It assumes your going full throttle the whole way,\n"
                                                     "In real life you would feather the throttle out as you ascend,\n"
                                                     "Saving you fuel because your not wasting fuel \n"
                                                     "By over speeding and fighting against the atmosphere.\n"
                                                     "\n-5. It assumes the isp, thrust and fuel density values of the rocket,\n"
                                                     "Will not change or fluctuate during flight and that you will get the rated fuel economy.\n"
                                                     "\n-6. it assumes the rocket will remain the same weight during the entire flight,\n"
                                                     "In real life your rocket will lose weight as it uses the fuel which would save fuel.\n"
                                                     "\nKeeping these things in mind,\n"
                                                     "You will more then likely need way less fuel then listed to get to orbit,\n"
                                                     "But it greatly depends on your launch strategy!")
        self.warning_label.grid(row=1, columnspan=2, padx=10, pady=5)

        menu_frame2 = ctk.CTkFrame(master_menu_frame)
        menu_frame2.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        main_menu_frame = ctk.CTkFrame(menu_frame2)
        main_menu_frame.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)


        self.payload_weight_label = ctk.CTkLabel(main_menu_frame, text="Payload Weight (kg):")
        self.payload_weight_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.payload_weight_entry = ctk.CTkEntry(main_menu_frame, placeholder_text="500")
        self.payload_weight_entry.grid(row=0, column=1, padx=10, pady=5)

        self.altitude_label = ctk.CTkLabel(main_menu_frame, text="Orbit Altitude (km):")
        self.altitude_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.altitude_entry = ctk.CTkEntry(main_menu_frame, placeholder_text="200000")
        self.altitude_entry.grid(row=1, column=1, padx=10, pady=5)

        self.engine_label = ctk.CTkLabel(main_menu_frame, text="Select Rocket Engine:")
        self.engine_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.engine_var = tk.StringVar(value="")  # Default value is empty
        self.engine_combobox = ctk.CTkComboBox(main_menu_frame, variable=self.engine_var, values=list(Rocket.ROCKET_ENGINES.keys()))
        self.engine_combobox.set("RS-25 - Liquid Hydrogen")
        self.engine_combobox.grid(row=2, column=1, ipadx=35, padx=10, pady=5, sticky='ew')

        self.num_engines_label = ctk.CTkLabel(main_menu_frame, text="Number of Engines:")
        self.num_engines_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.num_engines_entry = ctk.CTkEntry(main_menu_frame, placeholder_text="1")
        self.num_engines_entry.grid(row=3, column=1, padx=10, pady=5)

        self.fuel_label = ctk.CTkLabel(self, text="Select Fuel Type:")
        # self.fuel_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.fuel_var = tk.StringVar(value="")  # Default value is empty
        self.fuel_combobox = ctk.CTkComboBox(self, variable=self.fuel_var)
        self.fuel_combobox['values'] = list(Rocket.FUEL_TYPES.keys())
        # self.fuel_combobox.grid(row=4, column=1, padx=10, pady=5)


        self.calculate_button = ctk.CTkButton(main_menu_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, columnspan=2, padx=10, pady=10)

        result_menu_frame = ctk.CTkScrollableFrame(menu_frame2, width=320, height=250)
        result_menu_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        self.results_label = ctk.CTkLabel(result_menu_frame, text="")
        self.results_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def calculate(self):
        try:
            payload_weight = float(self.payload_weight_entry.get())
            altitude = float(self.altitude_entry.get())
            num_engines = int(self.num_engines_entry.get())
            engine = self.engine_var.get()
            fuel_type = self.fuel_var.get()

            # If engine or fuel is not selected, pick the best engine and fuel
            if not engine:
                engine = max(Rocket.ROCKET_ENGINES, key=lambda x: Rocket.ROCKET_ENGINES[x]["Thrust"])
            if not fuel_type:
                fuel_type = Rocket.ROCKET_ENGINES[engine]["Fuel_Type"]

            rocket = Rocket(payload_weight, altitude, engine, fuel_type, num_engines)
            self.results_label.configure(text=rocket.calculate_performance())
        except ValueError:
            self.results_label.configure(text="Please enter valid numbers.")

class Rocket:
    FUEL_TYPES = {
        "Liquid Hydrogen": {"Density": 0.07},
        "Kerosene": {"Density": 0.8},
        "Liquid Methane": {"Density": 0.05},
        "RP-1": {"Density": 0.81},
        "Liquid Oxygen": {"Density": 1.141},
        "N2O4": {"Density": 1.446},
        "UDMH": {"Density": 0.81},
        "MMH": {"Density": 0.876},
        "Hydrazine": {"Density": 1.021},
        "Hydrogen Peroxide": {"Density": 1.4},
        "Hydroxylammonium Nitrate": {"Density": 1.86},
        "HTPB": {"Density": 1.65},
        "Solid Propellant": {"Density": 1.7},
    }

    ROCKET_ENGINES = {
        "AJ-10 - N2O4": {"ISP": 319, "Thrust": 43000, "Fuel_Type": "N2O4"},
        "Vernier - N2O4": {"ISP": 312, "Thrust": 100, "Fuel_Type": "N2O4"},
        "R-4D - N2O4": {"ISP": 312, "Thrust": 490, "Fuel_Type": "N2O4"},
        "RD-180 - Liquid Hydrogen": {"ISP": 311, "Thrust": 4150000, "Fuel_Type": "Liquid Hydrogen"},
        "RS-25 - Liquid Hydrogen": {"ISP": 452, "Thrust": 1860000, "Fuel_Type": "Liquid Hydrogen"},
        "J-2 - Liquid Hydrogen": {"ISP": 421, "Thrust": 1000000, "Fuel_Type": "Liquid Hydrogen"},
        "RS-68A - Liquid Hydrogen": {"ISP": 420, "Thrust": 3800000, "Fuel_Type": "Liquid Hydrogen"},
        "RL10 - Liquid Hydrogen": {"ISP": 444, "Thrust": 110000, "Fuel_Type": "Liquid Hydrogen"},
        "HM7B - Liquid Hydrogen": {"ISP": 446, "Thrust": 62000, "Fuel_Type": "Liquid Hydrogen"},
        "LE-5 - Liquid Hydrogen": {"ISP": 444, "Thrust": 13700, "Fuel_Type": "Liquid Hydrogen"},
        "Vulcain 2 - Liquid Hydrogen": {"ISP": 434, "Thrust": 13800, "Fuel_Type": "Liquid Hydrogen"},
        "BE-3U - Liquid Hydrogen": {"ISP": 446, "Thrust": 49000, "Fuel_Type": "Liquid Hydrogen"},
        "RS-27 - Liquid Oxygen": {"ISP": 303, "Thrust": 890000, "Fuel_Type": "Liquid Oxygen"},
        "RS-27A - Liquid Oxygen": {"ISP": 303, "Thrust": 1000000, "Fuel_Type": "Liquid Oxygen"},
        "RS-27B - Liquid Oxygen": {"ISP": 303, "Thrust": 1000000, "Fuel_Type": "Liquid Oxygen"},
        "RS-27C - Liquid Oxygen": {"ISP": 303, "Thrust": 1050000, "Fuel_Type": "Liquid Oxygen"},
        "RD-0146 - Liquid Oxygen": {"ISP": 465, "Thrust": 146000, "Fuel_Type": "Liquid Oxygen"},
        "RL10B-2 - Liquid Oxygen": {"ISP": 450, "Thrust": 110000, "Fuel_Type": "Liquid Oxygen"},
        "RS-68B - Liquid Oxygen/Kerosene": {"ISP": 410, "Thrust": 4000000, "Fuel_Type": "Liquid Oxygen"},
        "HM7C - Liquid Oxygen/Kerosene": {"ISP": 453, "Thrust": 68000, "Fuel_Type": "Liquid Oxygen"},
        "Viking - Liquid Oxygen/Kerosene": {"ISP": 330, "Thrust": 69000, "Fuel_Type": "Liquid Oxygen"},
        "RL-60 - Liquid Oxygen/Liquid Hydrogen": {"ISP": 465, "Thrust": 266000, "Fuel_Type": "Liquid Oxygen"},
        "Merlin 1D - Kerosene": {"ISP": 282, "Thrust": 845000, "Fuel_Type": "Kerosene"},
        "Newton - Liquid Oxygen/Kerosene": {"ISP": 312, "Thrust": 24000, "Fuel_Type": "Liquid Oxygen"},
        "F-1 - RP-1": {"ISP": 304, "Thrust": 6770000, "Fuel_Type": "RP-1"},
        "F-1B - RP-1": {"ISP": 304, "Thrust": 7800000, "Fuel_Type": "RP-1"},
        "Rutherford - Liquid Methane": {"ISP": 343, "Thrust": 24250, "Fuel_Type": "Liquid Methane"},
        "LR-91 - Hydrazine": {"ISP": 315, "Thrust": 68, "Fuel_Type": "Hydrazine"},
        "LR-87 - Hydrazine": {"ISP": 312, "Thrust": 445000, "Fuel_Type": "Hydrazine"},
        "LR-89 - Hydrazine": {"ISP": 312, "Thrust": 822000, "Fuel_Type": "Hydrazine"},
        "LE-5 - Hydrazine": {"ISP": 444, "Thrust": 13700, "Fuel_Type": "Hydrazine"},
        "LE-9 - Hydrogen Peroxide": {"ISP": 446, "Thrust": 77000, "Fuel_Type": "Hydrogen Peroxide"},
        "LE-10 - Hydrogen Peroxide": {"ISP": 451, "Thrust": 116000, "Fuel_Type": "Hydrogen Peroxide"},
        "LE-7A - Hydrogen Peroxide": {"ISP": 431, "Thrust": 875000, "Fuel_Type": "Hydrogen Peroxide"},
        "Fregat-SB - Hydrogen Peroxide": {"ISP": 333, "Thrust": 27500, "Fuel_Type": "Hydrogen Peroxide"},
        "HM7 - UDMH": {"ISP": 446, "Thrust": 62000, "Fuel_Type": "UDMH"},
        "HM7B-NA - UDMH": {"ISP": 446, "Thrust": 62000, "Fuel_Type": "UDMH"},
        "Castor 120 - Solid Propellant": {"ISP": 270, "Thrust": 513000, "Fuel_Type": "Solid Propellant"},
        "Castor 30 - Solid Propellant": {"ISP": 270, "Thrust": 128000, "Fuel_Type": "Solid Propellant"},
        "Castor 300 - Solid Propellant": {"ISP": 270, "Thrust": 444000, "Fuel_Type": "Solid Propellant"},
        "Castor 4A - Solid Propellant": {"ISP": 255, "Thrust": 97400, "Fuel_Type": "Solid Propellant"},
        "Star 63 - Solid Propellant": {"ISP": 276, "Thrust": 640000, "Fuel_Type": "Solid Propellant"},
        "Star 48BV - Solid Propellant": {"ISP": 284, "Thrust": 66700, "Fuel_Type": "Solid Propellant"},
        "Star 30BP - Solid Propellant": {"ISP": 269, "Thrust": 28800, "Fuel_Type": "Solid Propellant"},
        "Star 48GX - Solid Propellant": {"ISP": 284, "Thrust": 66700, "Fuel_Type": "Solid Propellant"},
    }

    # Constants for chassis weight estimation (values are approximate)
    PAYLOAD_TO_CHASSIS_RATIO = 0.02  # Ratio of chassis weight to payload weight
    FUEL_TO_CHASSIS_RATIO = 0.04     # Ratio of chassis weight to propellant weight

    def __init__(self, payload_weight, altitude, engine, fuel_type, num_engines):
        self.payload_weight = payload_weight
        self.altitude = altitude
        self.engine = engine
        self.fuel_type = fuel_type
        self.num_engines = num_engines

    def calculate_performance(self):
        engine_thrust = self.ROCKET_ENGINES[self.engine]["Thrust"] * self.num_engines
        engine_isp = self.ROCKET_ENGINES[self.engine]["ISP"]
        fuel_density = self.FUEL_TYPES[self.fuel_type]["Density"]
        fuel_liters_needed = self.calculate_fuel_liters(fuel_density, engine_thrust, engine_isp)
        propellant_weight = self.get_propellant_weight(fuel_density, engine_thrust, engine_isp)
        chassis_weight = self.estimate_chassis_weight()
        rocket_weight = self.payload_weight + propellant_weight + chassis_weight
        thrust_weight_ratio = self.get_thrust_weight_ratio(rocket_weight, engine_thrust)
        burn_time = self.altitude / engine_isp  # Burn time calculation
        delta_v = self.calculate_delta_v(propellant_weight)

        thrust_weight_ratio1 = 0
        num_engine = 0

        while thrust_weight_ratio1 <= 1.00:
            num_engine += 1
            engine_thrust1 = self.ROCKET_ENGINES[self.engine]["Thrust"] * num_engine
            rocket_weight1 = self.payload_weight + propellant_weight + chassis_weight
            thrust_weight_ratio1 = self.get_thrust_weight_ratio(rocket_weight1, engine_thrust1)

        return f"Total Weight: {rocket_weight:.2f} kg\n" \
               f"Payload Weight: {self.payload_weight:.2f} kg\n" \
               f"Chassis Weight: {chassis_weight:.2f} kg\n" \
               f"Fuel Weight needed: {propellant_weight:.2f} kg\n" \
               f"Selected Rocket Engine: {self.engine}\n" \
               f"Number of Engines: {self.num_engines}\n" \
               f"Fuel Type: {self.fuel_type}\n" \
               f"Fuel Needed (Liters): {fuel_liters_needed:.2f}\n" \
               f"Selected Fuel Density: {fuel_density} kg/L\n" \
               f"Total Engine Thrust: {engine_thrust} N\n" \
               f"Thrust to Weight Ratio: {thrust_weight_ratio:.2f}\n" \
               f"Engines for Thrust-to-Weight Ratio > 1.00: {num_engine}\n" \
               f"Engine ISP: {engine_isp} s\n" \
               f"Burn Time: {burn_time:.2f} seconds\n" \
               f"Delta-V: {delta_v:.2f} m/s"

    def get_propellant_weight(self, fuel_density, engine_thrust, engine_isp):
        # Calculate propellant weight based on the selected fuel's density
        fuel_liters_needed = self.calculate_fuel_liters(fuel_density, engine_thrust, engine_isp)
        propellant_weight = fuel_liters_needed * fuel_density
        return propellant_weight

    @staticmethod
    def get_thrust_weight_ratio(rocket_weight, engine_thrust):
        # Calculate thrust-to-weight ratio based on rocket weight and engine thrust
        thrust_weight_ratio = engine_thrust / rocket_weight
        return thrust_weight_ratio

    def calculate_fuel_liters(self, fuel_density, engine_thrust, engine_isp):
        # Calculate the fuel needed based on altitude, rocket parameters, and engine specifics
        burn_time = self.altitude / engine_isp  # Assuming linear ascent
        fuel_consumption_rate = engine_thrust / engine_isp  # Constant thrust assumed
        total_fuel_needed = fuel_consumption_rate * burn_time
        fuel_liters_needed = total_fuel_needed / fuel_density
        return fuel_liters_needed

    def calculate_delta_v(self, propellant_weight):
        # Constants for delta-V calculation (values are approximate)
        g0 = 9.81  # Earth's surface gravity (m/s^2)
        earth_radius = 6371000  # Earth's radius (m)
        altitude = self.altitude
        # Total mass of the rocket, including payload
        total_mass = self.payload_weight + propellant_weight
        payload_mass = self.payload_weight
        # Delta-V formula: delta-V = sqrt(g0 * earth_radius) * (sqrt(2 * (altitude + earth_radius)) - sqrt(earth_radius))
        delta_v = (g0 * total_mass / (total_mass - payload_mass)) ** 0.5 * \
                  (2 * (altitude + earth_radius)) ** 0.5 - earth_radius ** 0.5
        return delta_v

    def estimate_chassis_weight(self):
        # Estimate the weight of the rocket's chassis based on payload and propellant weight
        chassis_weight_from_payload = self.payload_weight * self.PAYLOAD_TO_CHASSIS_RATIO
        chassis_weight_from_fuel = self.get_propellant_weight(self.FUEL_TYPES[self.fuel_type]["Density"], self.ROCKET_ENGINES[self.engine]["Thrust"],
                                                              self.ROCKET_ENGINES[self.engine]["ISP"]) * self.FUEL_TO_CHASSIS_RATIO
        total_chassis_weight = chassis_weight_from_payload + chassis_weight_from_fuel
        return total_chassis_weight


if __name__ == "__main__":
    app = RocketCalculator()
    app.mainloop()


