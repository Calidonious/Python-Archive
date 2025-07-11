import tkinter as tk
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


class RocketCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rocket Payload Calculator")
        self.resizable(False, False)

        ## Stuff in ctk.CTk ##
        master_menu_frame = ctk.CTkFrame(self)
        master_menu_frame.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)
        ## End of stuff in ctk.CTk ##

        ## Stuff in Master_menu_frame ##
        menu_frame= ctk.CTkFrame(master_menu_frame)
        menu_frame.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        ## Stuff in menu_frame ##
        self.intro_label = ctk.CTkLabel(menu_frame, text="This program calculates all the specs of the rocket,\n"
                                                   "You will need to get your payload(satellite) into orbit,\n"
                                                   "At your desired altitude, it asks you to select a engine,\n"
                                                   "As well as the amount of engines,\n"
                                                   "Your rocket needs to have a thrust to weight ratio of 1.00,\n"
                                                   "In order to fly ex. 0.75 means your engine can lift %75,\n"
                                                   "Of the rocket weight and you need to add more engines.\n"
                                                   "The average range of satellite weights is 100-3500kg in real life.\n\n"
                                                    "The range of average altitudes depends on your misson requirements,\n"
                                                    "The boundary commonly used to define the beginning of space is the Kármán line,\n"
                                                    "The Kármán line is located approximately 100 kilometers above sea level.\n\n"
                                                         
                                                    "Low Earth Orbit (LEO): 160 kilometers to 2,000 kilometers. \n"
                                                    "Uses: Earth observation, communication, and scientific missions.\n\n"
                                                         
                                                    "Medium Earth Orbit (MEO): 2,000 kilometers to 35,786 kilometers.\n"
                                                    "Uses: Navigation satellites, such as those used in GPS systems.\n\n"
                                                         
                                                    "Geostationary Orbit (GEO): 35,786 kilometers above Earth's equator\n"
                                                    "and orbit at the same speed as the Earth's rotation.\n"
                                                    "Uses: communication and weather satellites.\n\n"
                                                         
                                                    "Highly Elliptical Orbit (HEO): 200 to 40000 kilometers.\n"
                                                    "One point of the orbit close to Earth and the other far away.\n"
                                                    "Uses: communication, navigation, and scientific missions.\n\n"
                                                         
                                                    "Polar Orbit: 700 kilometers to 1,200 kilometers and orbit the Earth's poles.\n"
                                                    "uses: Earth observation and scientific missions.")
        self.intro_label.grid(row=0, column=0, padx=10, pady=10)

        main_menu_frame = ctk.CTkFrame(menu_frame)
        main_menu_frame.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)
        ## End stuff in Menu_frame ##


        ## Stuff in main_menu_frame ##
        self.payload_weight_label = ctk.CTkLabel(main_menu_frame, text="Payload Weight (kg):")
        self.payload_weight_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.payload_weight_entry = ctk.CTkEntry(main_menu_frame, placeholder_text="500")
        self.payload_weight_entry.grid(row=0, column=1, padx=10, pady=5)

        self.altitude_label = ctk.CTkLabel(main_menu_frame, text="Orbit Altitude (km):")
        self.altitude_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.altitude_entry = ctk.CTkEntry(main_menu_frame, placeholder_text="35786")
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

        self.calculate_button = ctk.CTkButton(main_menu_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, columnspan=2, padx=10, pady=10)
        ## End of stuff in main_menu_frame ##

        ## menu_frame2 is in master_menu_frame alongside menu_frame ##
        menu_frame2 = ctk.CTkFrame(master_menu_frame)
        menu_frame2.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)
        ## End of stuff in Master_menu_frame ##

        ## Stuff in menu_frame2 ##
        self.warning_label = ctk.CTkLabel(menu_frame2, text="Limitations of this program!\n"
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
        self.warning_label.grid(row=0, column=0, padx=10, pady=10)

        result_menu_frame = ctk.CTkScrollableFrame(menu_frame2, width=320, height=250)
        result_menu_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        ## End of stuff in Menu_frame2 ##

        ## Stuff in result_menu_frame ##
        lab_frame =  ctk.CTkFrame(result_menu_frame, fg_color="gray20")
        lab_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        ## Stuff in lab_frame ##
        self.results_label1 = ctk.CTkLabel(lab_frame, text="Results below!")
        self.results_label1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=175, pady=5)
        ## End of stuff in lab_frame##

        self.results_label = ctk.CTkLabel(result_menu_frame, text="")
        self.results_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        ## End of stuff in result_menu_frame ##

    def calculate(self):
        try:
            payload_weight = float(self.payload_weight_entry.get())
            altitude = float(self.altitude_entry.get())
            num_engines = int(self.num_engines_entry.get())
            engine = self.engine_var.get()
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
    "AJ-10 - N2O4": {"ISP": 319, "Thrust": 43000, "Fuel_Type": "N2O4", "Weight": 98},
    "Vernier - N2O4": {"ISP": 312, "Thrust": 100, "Fuel_Type": "N2O4", "Weight": 100},
    "R-4D - N2O4": {"ISP": 312, "Thrust": 490, "Fuel_Type": "N2O4", "Weight": 250},
    "RD-180 - Liquid Hydrogen": {"ISP": 311, "Thrust": 4150000, "Fuel_Type": "Liquid Hydrogen", "Weight": 5300},
    "RS-25 - Liquid Hydrogen": {"ISP": 452, "Thrust": 1860000, "Fuel_Type": "Liquid Hydrogen", "Weight": 3500},
    "J-2 - Liquid Hydrogen": {"ISP": 421, "Thrust": 1000000, "Fuel_Type": "Liquid Hydrogen", "Weight": 1800},
    "RS-68A - Liquid Hydrogen": {"ISP": 420, "Thrust": 3800000, "Fuel_Type": "Liquid Hydrogen", "Weight": 3300},
    "RL10 - Liquid Hydrogen": {"ISP": 444, "Thrust": 110000, "Fuel_Type": "Liquid Hydrogen", "Weight": 310},
    "HM7B - Liquid Hydrogen": {"ISP": 446, "Thrust": 62000, "Fuel_Type": "Liquid Hydrogen", "Weight": 300},
    "LE-5 - Liquid Hydrogen": {"ISP": 444, "Thrust": 13700, "Fuel_Type": "Liquid Hydrogen", "Weight": 300},
    "Vulcain 2 - Liquid Hydrogen": {"ISP": 434, "Thrust": 13800, "Fuel_Type": "Liquid Hydrogen", "Weight": 2000},
    "BE-3U - Liquid Hydrogen": {"ISP": 446, "Thrust": 49000, "Fuel_Type": "Liquid Hydrogen", "Weight": 2000},
    "RS-27 - Liquid Oxygen": {"ISP": 303, "Thrust": 890000, "Fuel_Type": "Liquid Oxygen", "Weight": 1200},
    "RS-27A - Liquid Oxygen": {"ISP": 303, "Thrust": 1000000, "Fuel_Type": "Liquid Oxygen", "Weight": 1200},
    "RS-27B - Liquid Oxygen": {"ISP": 303, "Thrust": 1000000, "Fuel_Type": "Liquid Oxygen", "Weight": 1200},
    "RS-27C - Liquid Oxygen": {"ISP": 303, "Thrust": 1050000, "Fuel_Type": "Liquid Oxygen", "Weight": 1200},
    "RD-0146 - Liquid Oxygen": {"ISP": 465, "Thrust": 146000, "Fuel_Type": "Liquid Oxygen", "Weight": 400},
    "RL10B-2 - Liquid Oxygen": {"ISP": 450, "Thrust": 110000, "Fuel_Type": "Liquid Oxygen", "Weight": 310},
    "RS-68B - Liquid Oxygen/Kerosene": {"ISP": 410, "Thrust": 4000000, "Fuel_Type": "Liquid Oxygen", "Weight": 3300},
    "HM7C - Liquid Oxygen/Kerosene": {"ISP": 453, "Thrust": 68000, "Fuel_Type": "Liquid Oxygen", "Weight": 300},
    "Viking - Liquid Oxygen/Kerosene": {"ISP": 330, "Thrust": 69000, "Fuel_Type": "Liquid Oxygen", "Weight": 900},
    "RL-60 - Liquid Oxygen/Liquid Hydrogen": {"ISP": 465, "Thrust": 266000, "Fuel_Type": "Liquid Oxygen", "Weight": 450},
    "Merlin 1D - Kerosene": {"ISP": 282, "Thrust": 845000, "Fuel_Type": "Kerosene", "Weight": 470},
    "Newton - Liquid Oxygen/Kerosene": {"ISP": 312, "Thrust": 24000, "Fuel_Type": "Liquid Oxygen", "Weight": 200},
    "F-1 - RP-1": {"ISP": 304, "Thrust": 6770000, "Fuel_Type": "RP-1", "Weight": 8500},
    "F-1B - RP-1": {"ISP": 304, "Thrust": 7800000, "Fuel_Type": "RP-1", "Weight": 9000},
    "Rutherford - Liquid Methane": {"ISP": 343, "Thrust": 24250, "Fuel_Type": "Liquid Methane", "Weight": 200},
    "LR-91 - Hydrazine": {"ISP": 315, "Thrust": 68, "Fuel_Type": "Hydrazine", "Weight": 340},
    "LR-87 - Hydrazine": {"ISP": 312, "Thrust": 445000, "Fuel_Type": "Hydrazine", "Weight": 700},
    "LR-89 - Hydrazine": {"ISP": 312, "Thrust": 822000, "Fuel_Type": "Hydrazine", "Weight": 1000},
    "LE-5 - Hydrazine": {"ISP": 444, "Thrust": 13700, "Fuel_Type": "Hydrazine", "Weight": 300},
    "LE-9 - Hydrogen Peroxide": {"ISP": 446, "Thrust": 77000, "Fuel_Type": "Hydrogen Peroxide", "Weight": 1200},
    "LE-10 - Hydrogen Peroxide": {"ISP": 451, "Thrust": 116000, "Fuel_Type": "Hydrogen Peroxide", "Weight": 1300},
    "LE-7A - Hydrogen Peroxide": {"ISP": 431, "Thrust": 875000, "Fuel_Type": "Hydrogen Peroxide", "Weight": 1700},
    "Fregat-SB - Hydrogen Peroxide": {"ISP": 333, "Thrust": 27500, "Fuel_Type": "Hydrogen Peroxide", "Weight": 950},
    "HM7 - UDMH": {"ISP": 446, "Thrust": 62000, "Fuel_Type": "UDMH", "Weight": 300},
    "HM7B-NA - UDMH": {"ISP": 446, "Thrust": 62000, "Fuel_Type": "UDMH", "Weight": 300},
    "Castor 120 - Solid Propellant": {"ISP": 270, "Thrust": 513000, "Fuel_Type": "Solid Propellant", "Weight": 6000},
    "Castor 30 - Solid Propellant": {"ISP": 270, "Thrust": 128000, "Fuel_Type": "Solid Propellant", "Weight": 2000},
    "Castor 300 - Solid Propellant": {"ISP": 270, "Thrust": 444000, "Fuel_Type": "Solid Propellant", "Weight": 4000},
    "Castor 4A - Solid Propellant": {"ISP": 255, "Thrust": 97400, "Fuel_Type": "Solid Propellant", "Weight": 1500},
    "Star 63 - Solid Propellant": {"ISP": 276, "Thrust": 640000, "Fuel_Type": "Solid Propellant", "Weight": 3000},
    "Star 48BV - Solid Propellant": {"ISP": 284, "Thrust": 66700, "Fuel_Type": "Solid Propellant", "Weight": 1100},
    "Star 30BP - Solid Propellant": {"ISP": 269, "Thrust": 28800, "Fuel_Type": "Solid Propellant", "Weight": 900},
    "Star 48GX - Solid Propellant": {"ISP": 284, "Thrust": 66700, "Fuel_Type": "Solid Propellant", "Weight": 1100},
    }


    def __init__(self, payload_weight, altitude, engine, fuel_type, num_engines):
        self.payload_weight = payload_weight
        self.altitude = altitude
        self.engine = engine
        self.fuel_type = fuel_type
        self.num_engines = num_engines

    def calculate_performance(self):
        engine_thrust = self.ROCKET_ENGINES[self.engine]["Thrust"] * self.num_engines
        engine_isp = self.ROCKET_ENGINES[self.engine]["ISP"]
        engine_weight = self.ROCKET_ENGINES[self.engine]["Weight"] * self.num_engines
        fuel_density = self.FUEL_TYPES[self.fuel_type]["Density"]
        burn_time = self.altitude / engine_isp
        fuel_liters_needed = (engine_thrust / engine_isp) * burn_time / fuel_density
        propellant_weight = fuel_liters_needed * fuel_density
        chassis_weight = self.estimate_chassis_weight(propellant_weight)
        dry_mass = self.payload_weight + chassis_weight + engine_weight
        rocket_weight = self.payload_weight + propellant_weight + chassis_weight + engine_weight
        thrust_weight_ratio = engine_thrust / rocket_weight
        delta_v = self.calculate_delta_v(propellant_weight, dry_mass, engine_isp)
        orbital_delta_v = self.calculate_orbital_delta_v()

        if thrust_weight_ratio <= 1.00:
            needed_engines = "Add more thrust!"
        else:
            needed_engines = "Ready for Lift-off!"


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
               f"Do i have enough engines?: {needed_engines}\n" \
               f"Engine ISP: {engine_isp} s\n" \
               f"Burn Time: {burn_time:.2f} seconds\n" \
               f"Delta-V Available: {delta_v:.2f} m/s" \
               f"Delta-V required for altitude: {orbital_delta_v:.2f} m/s"

    def calculate_delta_v(self, propellant_weight, dry_mass, engine_isp):
        # Calculates total amount of delta-v availale in the rocket
        # Constants for delta-V calculation (values are approximate)
        g0 = 9.81  # Earth's surface gravity (m/s^2)
        m0 = dry_mass + propellant_weight
        mf = dry_mass
        Isp = engine_isp
        # delta v = isp x gravitational constiant x log((drymass+propellent)/drymass)
        delta_v = Isp * g0 * math.log(m0 / mf)
        return delta_v
    
    def calculate_orbital_delta_v(self):
        # Calculates how much delta-v is required to reach desired altitude
        # Constants
        G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
        M = 5.972e24     # mass of Earth (kg)
        R = 6371000      # Earth's radius in meters
        altitude = self.altitude
        r = R + altitude  # Total distance from Earth's center

        # Orbital Delta-V formula: delta-V = sqrt(g0 * earth_radius) * (sqrt(2 * (altitude + earth_radius)) - sqrt(earth_radius))
        orbital_velocity = math.sqrt(G * M / r)  # m/s
        return orbital_velocity


    def estimate_chassis_weight(self, propellant_weight):

        # Constants for chassis weight estimation (values are approximate)
        payload_chassis_ratio = 0.02  # Ratio of chassis weight to payload weight
        fuel_chassis_ratio = 0.02  # Ratio of chassis weight to propellant weight

        # Estimate the weight of the rocket's chassis based on payload and propellant weight
        chassis_weight_from_payload = self.payload_weight * payload_chassis_ratio
        chassis_weight_from_fuel = propellant_weight * fuel_chassis_ratio
        total_chassis_weight = chassis_weight_from_payload + chassis_weight_from_fuel
        return total_chassis_weight


if __name__ == "__main__":
    app = RocketCalculator()
    app.mainloop()
