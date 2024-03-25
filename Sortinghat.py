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


class HarryPotterSortingHatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Harry Potter House Sorting Quiz")

        # Variables
        self.gryffindor = 0
        self.ravenclaw = 0
        self.hufflepuff = 0
        self.slytherin = 0

        # Create widgets
        self.label_question1 = ctk.CTkLabel(root, text="Do you like dawn or dusk?")
        self.radio_var1 = tk.IntVar()
        self.radio1_dawn = ctk.CTkRadioButton(root, text="Dawn", variable=self.radio_var1, value=1)
        self.radio1_dusk = ctk.CTkRadioButton(root, text="Dusk", variable=self.radio_var1, value=2)

        self.label_question2 = ctk.CTkLabel(root, text="When I'm dead, I want people to remember me as:")
        self.radio_var2 = tk.IntVar()
        self.radio2_good = ctk.CTkRadioButton(root, text="The Good", variable=self.radio_var2, value=1)
        self.radio2_great = ctk.CTkRadioButton(root, text="The Great", variable=self.radio_var2, value=2)
        self.radio2_wise = ctk.CTkRadioButton(root, text="The Wise", variable=self.radio_var2, value=3)
        self.radio2_bold = ctk.CTkRadioButton(root, text="The Bold", variable=self.radio_var2, value=4)

        self.label_question3 = ctk.CTkLabel(root, text="Which kind of instrument most pleases your ear?")
        self.radio_var3 = tk.IntVar()
        self.radio3_violin = ctk.CTkRadioButton(root, text="The Violin", variable=self.radio_var3, value=1)
        self.radio3_trumpet = ctk.CTkRadioButton(root, text="The Trumpet", variable=self.radio_var3, value=2)
        self.radio3_piano = ctk.CTkRadioButton(root, text="The Piano", variable=self.radio_var3, value=3)
        self.radio3_drum = ctk.CTkRadioButton(root, text="The Drum", variable=self.radio_var3, value=4)

        self.sort_button = ctk.CTkButton(root, text="Sort Me!", command=self.sort_user)
        self.result_label = ctk.CTkLabel(root, text="Your House Will Appear Here")

        # Grid layout
        self.label_question1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.radio1_dawn.grid(row=1, column=0, padx=10, pady=5)
        self.radio1_dusk.grid(row=1, column=1, padx=10, pady=5)

        self.label_question2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.radio2_good.grid(row=3, column=0, padx=10, pady=5)
        self.radio2_great.grid(row=3, column=1, padx=10, pady=5)
        self.radio2_wise.grid(row=4, column=0, padx=10, pady=5)
        self.radio2_bold.grid(row=4, column=1, padx=10, pady=5)

        self.label_question3.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
        self.radio3_violin.grid(row=6, column=0, padx=10, pady=5)
        self.radio3_trumpet.grid(row=6, column=1, padx=10, pady=5)
        self.radio3_piano.grid(row=7, column=0, padx=10, pady=5)
        self.radio3_drum.grid(row=7, column=1, padx=10, pady=5)

        self.sort_button.grid(row=8, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=9, column=0, columnspan=2, pady=10)

    def sort_user(self):
        answers = [
            self.radio_var1.get(),
            self.radio_var2.get(),
            self.radio_var3.get()
        ]

        for answer in answers:
            if answer == 1:
                self.gryffindor += 1
                self.ravenclaw += 1
            elif answer == 2:
                self.hufflepuff += 1
                self.slytherin += 1
            elif answer == 3:
                self.ravenclaw += 1
                self.hufflepuff += 1
            elif answer == 4:
                self.gryffindor += 1
                self.slytherin += 1

        house = self.determine_house()
        self.display_result(house)

    def determine_house(self):
        max_points = max(self.gryffindor, self.ravenclaw, self.hufflepuff, self.slytherin)

        if max_points == self.gryffindor and max_points > 1:
            return "Gryffindor"
        elif max_points == self.ravenclaw and max_points > 1:
            return "Ravenclaw"
        elif max_points == self.hufflepuff and max_points > 1:
            return "Hufflepuff"
        elif max_points == self.slytherin and max_points > 1:
            return "Slytherin"
        else:
            return "No House"

    def display_result(self, house):
        if house != "No House":
            self.result_label.configure(text=f"Congratulations! You are in {house}!")
        else:
            self.result_label.configure(text="You didn't get 2 points in any house. Try again!")


if __name__ == "__main__":
    master = ctk.CTk()
    app = HarryPotterSortingHatApp(master)
    master.mainloop()