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


class BlackjackGame:

    def __init__(self, root):

        self.root = root
        self.root.title("Blackjack Game")

        self.money = self.load_money()

        self.money_label = None
        self.dealer_hand_label = None
        self.player_hand_label = None

        self.deck = []
        self.player_hand = []
        self.dealer_hand = []

        self.bet_amount = tk.StringVar()
        self.bet_amount.set("0")

        self.create_widgets()

    def save_money(self):
        with open("cash.txt", "w") as file:
            file.write(str(self.money))

    def restart_game(self):
        self.money = 2000
        self.save_money()
        self.update_money_label()
        self.reset_game()

    def reset_game(self):
        self.deck = self.generate_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.update_player_hand_label()
        self.update_dealer_hand_label()
        self.update_money_label()

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def player_turn(self):
        self.deal_card(self.player_hand)
        self.update_player_hand_label()

        if self.calculate_hand_value(self.player_hand) > 21:
            self.end_game()

    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

        self.update_dealer_hand_label()
        self.end_game()

    def start_hand(self):
        bet = int(self.bet_amount.get())
        self.bet_amount.set(str(bet))
        if bet <= 0 or bet > self.money:
            return

        self.money -= bet
        self.update_money_label()

        self.reset_game()
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        self.update_player_hand_label()
        self.update_dealer_hand_label()

    def end_game(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)


        if player_value > 21 or (21 >= dealer_value >= player_value):
            result = "You lost!"

        else:
            self.money += int(self.bet_amount.get()) * 4
            result = "You won!"

        self.update_money_label()
        self.save_money()
        self.show_result(result)

    def show_result(self, result):
        result_label = ctk.CTkLabel(self.root, text=result)
        result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def update_player_hand_label(self):
        player_hand_str = ', '.join([f"{card['rank']} of {card['suit']}" for card in self.player_hand])
        player_value = self.calculate_hand_value(self.player_hand)
        self.player_hand_label.configure(text=f"Player Hand: {player_hand_str} (Value: {player_value})")

    def update_dealer_hand_label(self):
        dealer_hand_str = ', '.join([f"{card['rank']} of {card['suit']}" for card in self.dealer_hand])
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        self.dealer_hand_label.configure(text=f"Dealer Hand: {dealer_hand_str} (Value: {dealer_value})")

    def update_money_label(self):
        self.money_label.configure(text=f"Money: ${self.money}")

    def create_widgets(self):
        self.player_hand_label = ctk.CTkLabel(self.root, text="Player Hand:")
        self.player_hand_label.grid(row=4, column=0, padx=10, pady=10)

        self.dealer_hand_label = ctk.CTkLabel(self.root, text="Dealer Hand:")
        self.dealer_hand_label.grid(row=4, column=1, padx=10, pady=10)

        ctk.CTkButton(self.root, text="Hit", command=self.player_turn).grid(row=2, column=0, padx=10, pady=10)
        ctk.CTkButton(self.root, text="Stand", command=self.dealer_turn).grid(row=2, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.root, text="Bet: $").grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkEntry(self.root, textvariable=self.bet_amount).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(self.root, text="Start Hand", command=self.start_hand).grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkButton(self.root, text="Save Game", command=self.save_money).grid(row=3, column=0, padx=10, pady=10)
        ctk.CTkButton(self.root, text="Restart Game", command=self.restart_game).grid(row=3, column=1, padx=10, pady=10)

        self.money_label = ctk.CTkLabel(self.root, text=f"Money: ${self.money}")
        self.money_label.grid(row=1, column=0, padx=10, pady=10)

        self.update_player_hand_label()
        self.update_dealer_hand_label()
        self.update_money_label()

    @staticmethod
    def generate_deck():
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    @staticmethod
    def load_money():
        try:
            with open("cash.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 2000

    @staticmethod
    def calculate_hand_value(hand):
        value = sum([10 if card['rank'] in ['J', 'Q', 'K'] else 11 if card['rank'] == 'A' else int(card['rank'])
                     for card in hand])
        num_aces = sum([1 for card in hand if card['rank'] == 'A'])

        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1

        return value


if __name__ == "__main__":
    master = ctk.CTk()
    game = BlackjackGame(master)
    master.mainloop()


