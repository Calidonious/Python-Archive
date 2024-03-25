import tkinter as tk
import customtkinter as ctk
from forex_python.converter import CurrencyRates


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


class CurrencyConverterApp:
    def __init__(self, master):

        # Master frame configuration
        self.master = master
        self.master.title("Currency Converter")
        self.master.geometry("270x240")
        self.master.minsize(270,240)
        self.master.resizable(False,False)

        # List of supported currency codes
        self.available_conversions = {
            "EuroMember Countries" : "EUR",
            "Indonesia Rupiah" : "IDR",
            "Bulgaria Lev" : "BGN",
            "Israel Shekel" : "ILS",
            "United Kingdom Pound" : "GBP",
            "Denmark Krone" : "DKK",
            "Canada Dollar" : "CAD",
            "Japan Yen" : "JPY",
            "Hungary Forint" : "HUF",
            "Romania NewLeu" : "RON",
            "Malaysia Ringgit" : "MYR",
            "Sweden Krona" : "SEK",
            "Singapore Dollar" : "SGD",
            "Hong-Kong Dollar" : "HKD",
            "Australia Dollar" : "AUD",
            "Switzerland Franc" : "CHF",
            "Korea(South) Won" : "KRW",
            "China Yuan Renminbi" : "CNY",
            "Turkey Lira" : "TRY",
            "Croatia Kuna" : "HRK",
            "New-Zealand Dollar" : "NZD",
            "Thailand Baht" : "THB",
            "United-States Dollar" : "USD",
            "Norway Krone" : "NOK",
            "Russia Ruble" : "RUB",
            "India Rupee" : "INR",
            "Mexico Peso" : "MXN",
            "Czech-Republic Koruna" : "CZK",
            "Brazil Real" : "BRL",
            "Poland Zloty" : "PLN",
            "Philippines Peso" : "PHP",
            "South Africa Rand" : "ZAR",
        }

        # widgets

        # Base currency label
        self.base_currency_label = ctk.CTkLabel(master, text="Base Currency:")
        self.base_currency_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Base currency entry field
        self.base_currency_var = tk.StringVar()
        self.base_currency_var.set("Canada Dollar")
        self.base_currency_combo = ctk.CTkComboBox(master, variable=self.base_currency_var, values=list(self.available_conversions.keys()))
        self.base_currency_combo.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # self.base_currency_entry = ctk.CTkEntry(master,textvariable=self.base_currency_var)
        # self.base_currency_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")


        # Target currency label
        self.target_currency_label = ctk.CTkLabel(master, text="Target Currency:")
        self.target_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Target currency entry field
        self.target_currency_var = tk.StringVar()
        self.target_currency_var.set("United-States Dollar")
        self.target_currency_combo = ctk.CTkComboBox(master, variable=self.target_currency_var, values=list(self.available_conversions.keys()))
        self.target_currency_combo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # self.target_currency_entry = ctk.CTkEntry(master, textvariable=self.target_currency_var)
        # self.target_currency_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")


        # Amount label
        self.amount_label = ctk.CTkLabel(master, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Amount entry
        self.amount_var = tk.StringVar()
        self.amount_var.set("0.00")
        self.amount_entry = ctk.CTkEntry(master, textvariable=self.amount_var)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Conversion button
        self.convert_button = ctk.CTkButton(master, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Conversion result label
        self.result_label = ctk.CTkLabel(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def convert_currency(self):

        # Variable get
        selected_base = self.base_currency_var.get()
        base_currency = self.available_conversions[selected_base]

        selected_target = self.target_currency_var.get()
        target_currency = self.available_conversions[selected_target]

        # base_currency = self.base_currency_var.get().upper()
        # target_currency = self.target_currency_var.get().upper()
        amount = float(self.amount_var.get())

        c = CurrencyRates()

        # Conversion Logic
        try:
            exchange_rate = c.get_rate(base_currency.upper(), target_currency.upper())
            converted_amount = round(amount * exchange_rate, 2)
            result_text = f"{amount} {base_currency} is equal to {converted_amount} {target_currency}"
            self.result_label.configure(text=result_text)
        except Exception as e:
            self.result_label.configure(text=f"Error: {e}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = CurrencyConverterApp(root)
    root.mainloop()
