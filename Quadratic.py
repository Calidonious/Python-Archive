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


class QuadraticEquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quadratic Equation Solver")
        self.root.resizable(False, False)

        # Variables
        self.a_var = tk.StringVar()
        self.b_var = tk.StringVar()
        self.c_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Variable initialization
        self.a_var.set("0.00")
        self.b_var.set("0.00")
        self.c_var.set("0.00")

        # Create widgets
        self.label_a = ctk.CTkLabel(root, text="Enter coefficient a:")
        self.entry_a = ctk.CTkEntry(root, textvariable=self.a_var)

        self.label_b = ctk.CTkLabel(root, text="Enter coefficient b:")
        self.entry_b = ctk.CTkEntry(root, textvariable=self.b_var)

        self.label_c = ctk.CTkLabel(root, text="Enter coefficient c:")
        self.entry_c = ctk.CTkEntry(root, textvariable=self.c_var)

        self.solve_button = ctk.CTkButton(root, text="Solve Quadratic Equation", command=self.solve_equation)
        self.result_label = ctk.CTkLabel(root, textvariable=self.result_var)

        # Grid layout
        self.label_a.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_a.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.label_b.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_b.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.label_c.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_c.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.solve_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def solve_equation(self):
        try:
            a = float(self.a_var.get())
            b = float(self.b_var.get())
            c = float(self.c_var.get())
        except ValueError:
            self.result_var.set("Please enter a valid number.")
            return

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            self.result_var.set(f"The roots are real and distinct: {root1:.2f}, {root2:.2f}")
        elif discriminant == 0:
            root1 = -b / (2*a)
            self.result_var.set(f"The root is real and equal: {root1:.2f}")
        else:
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            root1 = f"{real_part:.2f} + {imaginary_part:.2f}i"
            root2 = f"{real_part:.2f} - {imaginary_part:.2f}i"
            self.result_var.set(f"The roots are complex conjugates: {root1}, {root2}")


if __name__ == "__main__":
    master = ctk.CTk()
    app = QuadraticEquationSolverApp(master)
    master.mainloop()