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


class CardCountingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack Card Counting Trainer")

        self.deck = []
        self.user_count = 0
        self.correct_count = 0
        self.incorrect_count = 0

        self.label_decks = ctk.CTkLabel(master, text="Number of Decks:")
        self.label_decks.grid(row=0, column=0, padx=5, pady=5)

        self.entry_decks = ctk.CTkEntry(master)
        self.entry_decks.grid(row=0, column=1, padx=5, pady=5)

        self.start_button = ctk.CTkButton(master, text="Start", command=self.start_game)
        self.start_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.label_card = ctk.CTkLabel(master, text="")
        self.label_card.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.label_count = ctk.CTkLabel(master, text="Current Count:")
        self.label_count.grid(row=3, column=0, padx=5, pady=5)

        self.entry_count = ctk.CTkEntry(master)
        self.entry_count.grid(row=3, column=1, padx=5, pady=5)

        self.submit_button = ctk.CTkButton(master, text="Submit", command=self.check_count)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = ctk.CTkLabel(master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    @staticmethod
    def get_value(rank):
        if rank in ['2', '3', '4', '5', '6']:
            return 1
        elif rank in ['7', '8', '9']:
            return 0
        else:
            return -1

    def start_game(self):
        try:
            num_decks = int(self.entry_decks.get())
            self.create_deck(num_decks)
            random.shuffle(self.deck)
            self.deal_card()
            self.start_button.configure(state="disabled")
        except ValueError:
            self.result_label.configure(text="Please enter a valid number of decks.")

    def create_deck(self, num_decks):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(rank, suit) for _ in range(num_decks) for suit in suits for rank in ranks]

    def deal_card(self):
        if self.deck:
            card = self.deck.pop()
            self.label_card.configure(text=f"Card: {card[0]} of {card[1]}")
        else:
            self.show_results()

    def check_count(self):
        try:
            user_count = int(self.entry_count.get())
            if user_count == self.actual_count():
                self.correct_count += 1
                self.result_label.configure(text="Correct count!")
            else:
                self.incorrect_count += 1
                self.result_label.configure(text="Incorrect count.")
            self.entry_count.delete(0, tk.END)
            self.deal_card()
        except ValueError:
            self.result_label.configure(text="Please enter a valid count.")

    def actual_count(self):
        return sum(self.get_value(rank) for rank, _ in self.deck)

    def show_results(self):
        self.result_label.configure(text=f"Correct count: {self.correct_count}\n"
                                       f"Incorrect count: {self.incorrect_count}\n"
                                       f"Final Score: {self.correct_count - self.incorrect_count}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = CardCountingApp(root)
    root.mainloop()
