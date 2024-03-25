import tkinter as tk
import customtkinter as ctk
import random


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


class Magic8BallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic 8 Ball")

        # Variables
        self.question_var = tk.StringVar()
        self.question_var.set("What is your question?")
        self.response_var = tk.StringVar()

        # Create widgets
        self.label_question = ctk.CTkLabel(root, text="Ask a Question:")
        self.entry_question = ctk.CTkEntry(root, textvariable=self.question_var, width=40)
        self.ask_button = ctk.CTkButton(root, text="Ask", command=self.ask_magic_8_ball)
        self.response_label = ctk.CTkLabel(root, textvariable=self.response_var)

        # Grid layout
        self.label_question.grid(row=0, column=2, padx=10, pady=10)
        self.entry_question.grid(row=1, column=2, padx=10, pady=10, sticky="nesw")
        self.ask_button.grid(row=2, column=2, columnspan=2,padx=10, pady=10)
        self.response_label.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    def ask_magic_8_ball(self):
        question = self.question_var.get()
        if not question:
            self.response_var.set("Please enter a question.")
            return

        num = random.randint(1, 9)

        if num >= 9:
            response = 'Yes - definitely.'
        elif num == 8:
            response = 'It is decidedly so.'
        elif num == 7:
            response = 'Without a doubt.'
        elif num == 6:
            response = 'Reply hazy, try again.'
        elif num == 5:
            response = 'Ask again later.'
        elif num == 4:
            response = 'Better not tell you now.'
        elif num == 3:
            response = 'My sources say no.'
        elif num == 2:
            response = 'Outlook not so good.'
        else:
            response = 'Very doubtful.'

        self.response_var.set(f"Question: {question}\nMagic 8 Ball says: {response}")


if __name__ == "__main__":
    master = ctk.CTk()
    app = Magic8BallApp(master)
    master.mainloop()
