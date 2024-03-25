import tkinter as tk
from tkinter import messagebox
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

class CardCounterApp:
    def __init__(self, master):
        self.cards_frame = None
        self.deal_button = None
        self.label_count = None
        self.start_button = None
        self.num_decks = None
        self.label_decks = None
        self.master = master
        self.master.title("Blackjack Card Counter")

        self.deck = []
        self.count = 0
        self.cards_dealt = []

        self.create_widgets()

    @staticmethod
    def get_value(rank):
        if rank in ['2', '3', '4', '5', '6']:
            return 1
        elif rank in ['7', '8', '9']:
            return 0
        else:
            return -1

    def create_widgets(self):
        self.label_decks = ctk.CTkLabel(self.master, text="Number of Decks:")
        self.label_decks.grid(row=0, column=0, padx=10, pady=10)

        self.num_decks = ctk.CTkEntry(self.master)
        self.num_decks.grid(row=0, column=1, padx=10, pady=10)

        self.start_button = ctk.CTkButton(self.master, text="Start", command=self.start_game)
        self.start_button.grid(row=0, column=2, padx=10, pady=10)

        self.label_count = ctk.CTkLabel(self.master, text="Current Count: 0")
        self.label_count.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.deal_button = ctk.CTkButton(self.master, text="Deal", command=self.deal_card)
        self.deal_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.cards_frame = ctk.CTkScrollableFrame(self.master)
        self.cards_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def create_deck(self, num_decks):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(rank, suit) for _ in range(num_decks) for suit in suits for rank in ranks]

    def start_game(self):
        try:
            num_decks = int(self.num_decks.get())
            if num_decks <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid number of decks.")
            return

        self.create_deck(num_decks)
        random.shuffle(self.deck)
        self.count = 0
        self.cards_dealt = []

        self.label_count.configure(text=f"Current Count: {self.count}")

        self.deal_button.configure(state="normal")

    def actual_count(self):
        return sum(self.get_value(rank) for rank, _ in self.deck)

    def deal_card(self):
        if not self.deck:
            tk.messagebox.showinfo("End of Deck", "All cards have been dealt.")
            self.deal_button.configure(state="disabled")
            return

        card = self.deck.pop()
        self.cards_dealt.append(card)

        self.count = self.actual_count()

        self.label_count.configure(text=f"Current Count: {self.count}")

        self.display_dealt_cards()

    def display_dealt_cards(self):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        for i, card in enumerate(self.cards_dealt):
            ctk.CTkLabel(self.cards_frame, text=f"Card {i+1}: {card}").pack()


if __name__ == "__main__":
    root = ctk.CTk()
    app = CardCounterApp(root)
    root.mainloop()

