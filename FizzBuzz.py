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


def fizzbuzz():
    result = []
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            result.append('FizzBuzz')
        elif x % 3 == 0:
            result.append('Fizz')
        elif x % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(x))

    # New Matrix Generator
    matrix = [result[i:i + 10] for i in range(0, len(result), 10)]
    return matrix

class FizzBuzzApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FizzBuzz App")
        self.root.resizable(False, False)

        # Create widgets
        self.button_generate = ctk.CTkButton(root, text="Generate FizzBuzz", command=self.generate_and_display)
        self.label_result = ctk.CTkLabel(root, text="FizzBuzz Result:")
        self.text_result = ctk.CTkTextbox(root, height=185, width=330, state='disabled')

        # Grid layout
        self.button_generate.grid(row=0, column=0, pady=10)
        self.label_result.grid(row=1, column=0, pady=5)
        self.text_result.grid(row=2, column=0, pady=10)

    def generate_and_display(self):
        # Clear previous content
        self.text_result.configure(state='normal')
        self.text_result.delete('1.0', tk.END)

        # Generate FizzBuzz and display in matrix form
        fizzbuzz_result = fizzbuzz()
        for row in fizzbuzz_result:
            self.text_result.insert(tk.END, '  '.join(row) + '.\n')

        # Disable text widget to make it read-only
        self.text_result.configure(state='disabled')


if __name__ == "__main__":
    master = ctk.CTk()
    app = FizzBuzzApp(master)
    master.mainloop()

