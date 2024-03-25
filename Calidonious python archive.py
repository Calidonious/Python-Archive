import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import *
from datetime import timedelta
import hashlib
import datetime
import subprocess
import sys
from PIL import Image


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

# Calling theme function
set_appear_theme()


# Class containing entire application
class App:

    # Application initialization function
    def __init__(self, root):

        # Root functions
        self.root = root
        self.root.title("Calidonious' python archive")
        self.root.resizable(False, False)
        self.root.iconbitmap('Calidonious logo.ico')

        # Variables
        self.current_time_var = tk.StringVar()
        self.time_difference_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.save_username_var = tk.BooleanVar()
        self.logged_in_user = None
        self.option_menu_theme = None
        self.option_menu_appearance = None

        # Load data
        self.dictionary = self.load_dictionary()
        self.login_names = self.load_login_names()

        # Check if an account needs to be created
        if not self.dictionary:
            self.create_account()

        # Check if a user is already logged in
        if self.login_names:
            for username in self.login_names:
                if username in self.dictionary:
                    self.logged_in_user = username
                    self.is_login_expired()
                else:
                    self.show_login_screen()
            else:
                pass
        else:
            self.show_login_screen()

    # Menus
    def show_login_screen(self):

        ###

        # Login Screen
        login_frame = ctk.CTkFrame(self.root)
        login_frame.grid(row=0, column=0, sticky='nesw')
        self.root.geometry("270x523")

        ##

        # Login image frame
        login_frame_image = ctk.CTkFrame(login_frame)
        login_frame_image.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        # Image variable
        my_image = ctk.CTkImage(light_image=Image.open("Cali_Logo.png"),
                                dark_image=Image.open("Cali_Logo.png"),
                                size=(230, 230))

        # Image label
        ctk.CTkLabel(login_frame_image, image=my_image, text="").grid(row=0, column=0, padx=10, pady=10)

        ##

        # Main login frame
        login_frame_main = ctk.CTkFrame(login_frame)
        login_frame_main.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        #########################################################################################################
        # Login frame1
        login_frame1 = ctk.CTkFrame(login_frame_main)
        login_frame1.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)


        # Login frame1 widgets
        ctk.CTkLabel(login_frame1, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        username_entry = ctk.CTkEntry(login_frame1, textvariable=self.username_var)
        username_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ctk.CTkLabel(login_frame1, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        password_entry = ctk.CTkEntry(login_frame1, textvariable=self.password_var, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)


        #########################################################################################################
        #login frame2
        login_frame2 = ctk.CTkFrame(login_frame_main)
        login_frame2.grid(row=1, column=0, padx=10, pady=10)

        # login frame2 widgets
        login_button = ctk.CTkButton(login_frame2, text="Login", command=self.login)
        login_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        create_account_button = ctk.CTkButton(login_frame2, text="Create Account", command=self.create_account)
        create_account_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def create_account(self):

        ###

        # Create Account Screen
        create_account_frame = ctk.CTkFrame(self.root)
        create_account_frame.grid(row=0, column=0, sticky='nesw')
        self.root.geometry("270x250")

        ##

        # Main account frame
        create_account_frame_main = ctk.CTkFrame(create_account_frame)
        create_account_frame_main.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)


        #########################################################################################################
        # Account frame1
        create_account_frame1 = ctk.CTkFrame(create_account_frame_main)
        create_account_frame1.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)


        # Account frame1 widgets
        ctk.CTkLabel(create_account_frame1, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        new_username_entry = ctk.CTkEntry(create_account_frame1)
        new_username_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ctk.CTkLabel(create_account_frame1, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        new_password_entry = ctk.CTkEntry(create_account_frame1, show="*")
        new_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)


        #########################################################################################################
        # Account frame2
        create_account_frame2 = ctk.CTkFrame(create_account_frame_main)
        create_account_frame2.grid(row=1, column=0, padx=10, pady=10)


        # Account frame2 widgets
        create_button = ctk.CTkButton(create_account_frame2, text="Create Account", command=lambda: self.save_account(new_username_entry.get(), new_password_entry.get()))
        create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        back_button = ctk.CTkButton(create_account_frame2, text="Back",command=self.show_login_screen)
        back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def logged_in(self):

        ####

        # Main Menu super frame
        menu_frame = ctk.CTkFrame(self.root)
        menu_frame.grid(row=0, column=0, sticky='nesw')
        self.root.geometry("1020x820")

        ###

        # Calidonious image frame
        menu_frame_image = ctk.CTkFrame(menu_frame)
        menu_frame_image.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        # Image variable
        my_image = ctk.CTkImage(light_image=Image.open("calidonious banner 940x250.jpg"),
                                dark_image=Image.open("calidonious banner 940x250.jpg"),
                                size=(980, 250))

        # Image label
        ctk.CTkLabel(menu_frame_image, image=my_image, text="").grid(row=0, column=0, padx=10, pady=10)


        ###

        # Main menu Frame
        menu_frame_main = ctk.CTkFrame(menu_frame)
        menu_frame_main.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)


        ##

        # Main top frame
        menu_frame_top = ctk.CTkFrame(menu_frame_main)
        menu_frame_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        #########################################################################################################
        # Menu frame 1 stuff
        menu_frame1= ctk.CTkFrame(menu_frame_top)
        menu_frame1.grid(row=0, column=0, padx=10, pady=10)

        ###############################################
        # Menu frame for label1
        menu_frame_label1 = ctk.CTkFrame(menu_frame1)
        menu_frame_label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Label1
        ctk.CTkLabel(menu_frame_label1, text="Games").grid(row=0, column=0, columnspan=2, padx=30, pady=5)

        # Scrollable games frame
        games_frame = ctk.CTkScrollableFrame(menu_frame1, width=330, height=10)
        games_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Buttons in menu frame1
        button1 = ctk.CTkButton(games_frame, text="Guess the number", command=self.guess)
        button1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button2 = ctk.CTkButton(games_frame, text="Sorting hat", command=self.sorting)
        button2.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        button3 = ctk.CTkButton(games_frame, text="Magic 8 ball", command=self.magic)
        button3.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button4 = ctk.CTkButton(games_frame, text="Dice sim", command=self.dice)
        button4.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        button5 = ctk.CTkButton(games_frame, text="Lotto sim", command=self.lotto)
        button5.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        button6 = ctk.CTkButton(games_frame, text="Coin flip", command=self.coin)
        button6.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

        button7 = ctk.CTkButton(games_frame, text="Blackjack", command=self.black)
        button7.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button8 = ctk.CTkButton(games_frame, text="Bomb Defused!", command=self.bomb)
        button8.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

        button9 = ctk.CTkButton(games_frame, text="Rad-rat", command=self.rad_rat)
        button9.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        button10 = ctk.CTkButton(games_frame, text="Card counting game", command=self.cardcountgame)
        button10.grid(row=5, column=2, columnspan=2, padx=10, pady=10)


        #########################################################################################################
        # Menu frame 2 stuff
        menu_frame2 = ctk.CTkFrame(menu_frame_top)
        menu_frame2.grid(row=0, column=1, padx=10, pady=10)


        ###############################################
        # Menu frame for label2
        menu_frame_label2 = ctk.CTkFrame(menu_frame2)
        menu_frame_label2.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Label2
        ctk.CTkLabel(menu_frame_label2, text="Utilities").grid(row=0, column=0, columnspan=2, padx=30, pady=5)

        # Scrollable utilities frame
        utilities_frame = ctk.CTkScrollableFrame(menu_frame2, width=500, height=10)
        utilities_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        # Buttons in menu frame
        button1u = ctk.CTkButton(utilities_frame, text="Grade", command=self.grade)
        button1u.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        button2u = ctk.CTkButton(utilities_frame, text="PH", command=self.ph)
        button2u.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

        button3u = ctk.CTkButton(utilities_frame, text="Quad", command=self.quad)
        button3u.grid(row=0, column=4, columnspan=2, padx=10, pady=10)

        button4u = ctk.CTkButton(utilities_frame, text="BMI", command=self.bmi)
        button4u.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        button5u = ctk.CTkButton(utilities_frame, text="cash", command=self.cash)
        button5u.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        button6u = ctk.CTkButton(utilities_frame, text="Temp", command=self.temp)
        button6u.grid(row=1, column=4, columnspan=2, padx=10, pady=10)

        button7u = ctk.CTkButton(utilities_frame, text="Fizz", command=self.fizz)
        button7u.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        button8u = ctk.CTkButton(utilities_frame, text="Random Day", command=self.rand_day)
        button8u.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        button9u = ctk.CTkButton(utilities_frame, text="Countdown", command=self.count)
        button9u.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

        button10u = ctk.CTkButton(utilities_frame, text="Prime finder", command=self.prime)
        button10u.grid(row=3, column=0, padx=10, pady=10)

        button11u = ctk.CTkButton(utilities_frame, text="Delta-V", command=self.delta)
        button11u.grid(row=3, column=2, padx=10, pady=10)

        button12u = ctk.CTkButton(utilities_frame, text="Potential energy", command=self.potential)
        button12u.grid(row=3, column=4, padx=10, pady=10)

        button13u = ctk.CTkButton(utilities_frame, text="E=mc2", command=self.e_mc2)
        button13u.grid(row=4, column=0, padx=10, pady=10)

        button14u = ctk.CTkButton(utilities_frame, text="Nuke decay", command=self.nuke)
        button14u.grid(row=4, column=2, padx=10, pady=10)

        button15u = ctk.CTkButton(utilities_frame, text="Auto card counter", command=self.card_count)
        button15u.grid(row=4, column=4, padx=10, pady=10)

        ##

        # Main bottom frame
        menu_frame_bottom = ctk.CTkFrame(menu_frame_main)
        menu_frame_bottom.grid(row=1, column=0, padx=10, pady=10)


        #########################################################################################################
        # Menu frame 3 stuff
        menu_frame3 = ctk.CTkFrame(menu_frame_bottom)
        menu_frame3.grid(row=3, column=0, padx=10, pady=10)

        # Obtaining variables
        try:
            with open('target_date2.txt', 'r') as file:
                for line in file:
                    saved_time = datetime.datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S.%f')
                    formatted_time_str = saved_time.strftime('%H:%M:%S')

        except FileNotFoundError:
            return True

        self.update_time()

        # Schedule the update_time function to run periodically
        self.root.after(1000, self.update_time)

        # Menu frame3 labels
        ctk.CTkLabel(menu_frame3, text="Current time:").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(menu_frame3, textvariable=self.current_time_var).grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(menu_frame3, text="Last login time:").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(menu_frame3, text=f"{formatted_time_str}").grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(menu_frame3, text="Time since last login:").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkLabel(menu_frame3, textvariable=self.time_difference_var).grid(row=2, column=1, padx=10, pady=5)


        ########################################################################################################
        # Menu frame 4 stuff
        menu_frame4 = ctk.CTkFrame(menu_frame_bottom)
        menu_frame4.grid(row=3, column=1, padx=10, pady=10)


        ###############################################
        # Menu frame for label3
        menu_frame_label4 = ctk.CTkFrame(menu_frame4)
        menu_frame_label4.grid(row=0, column=1, columnspan=2, sticky='nesw', padx=10, pady=10)

        # Label4
        username = self.logged_in_user
        ctk.CTkLabel(menu_frame_label4, text=f"Username: {username}").grid(row=0, column=1, columnspan=2, padx=5, pady=5)


        # Buttons in frame4
        logout_button = ctk.CTkButton(menu_frame4, text="Logout", command=self.logout)
        logout_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        delete_account_button = ctk.CTkButton(menu_frame4, text="Delete Account", command=self.delete_account)
        delete_account_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)


        ##

        # Main bottom frame2
        menu_frame_bottom2 = ctk.CTkFrame(menu_frame_main)
        menu_frame_bottom2.grid(row=1, column=1, padx=10, pady=10)

        ########################################################################################################
        menu_frame_appearance = ctk.CTkFrame(menu_frame_bottom2)
        menu_frame_appearance.grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkLabel(menu_frame_appearance, text="appearance mode:").grid(row=0, column=0, padx=5, pady=5)

        choices = ["System", "dark", "light"]
        self.option_menu_appearance = ctk.CTkOptionMenu(menu_frame_appearance, values=choices, command=ctk.set_appearance_mode)
        self.option_menu_appearance.grid(row=1, column=0, padx=5, pady=5)

        theme_button = ctk.CTkButton(menu_frame_appearance, text="Save appearance mode", command=self.set_appearance)
        theme_button.grid(row=2, column=0, padx=10, pady=10)

        ########################################################################################################
        menu_frame_theme = ctk.CTkFrame(menu_frame_bottom2)
        menu_frame_theme.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(menu_frame_theme, text="Color theme:").grid(row=2, column=0, padx=5, pady=5)

        choices2 = ["pink", "purple", "red", "orange", "yellow", 'light-green', "green", "dark-green", "light-blue", "blue", "dark-blue"]
        self.option_menu_theme = ctk.CTkOptionMenu(menu_frame_theme, values=choices2)
        self.option_menu_theme.grid(row=3, column=0, padx=5, pady=5)

        theme_button = ctk.CTkButton(menu_frame_theme, text="Switch theme", command=self.set_theme)
        theme_button.grid(row=4, column=0, padx=10, pady=10)


    # login functions
    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if self.authenticate(username, password):
            self.logged_in_user = username
            self.save_login_time()
            self.save_login_names()
            self.logged_in()
        else:
            self.show_login_error()

    def authenticate(self, username, password):
        encoded_password = self.hash_password(password)
        return self.dictionary.get(username) == encoded_password

    def is_login_expired(self):
        try:
            with open('target_date2.txt', 'r') as file:
                for line in file:
                    saved_time = datetime.datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S.%f')
                    current_time = datetime.datetime.now()
                    time_difference = current_time - saved_time

                    if time_difference > timedelta(minutes=30):

                        self.logout()

                    else:
                        self.logged_in()

        except FileNotFoundError:
            return True

    def update_time(self):
        try:
            with open('target_date2.txt', 'r') as file:
                for line in file:
                    saved_time = datetime.datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S.%f')
                    current_time = datetime.datetime.now()
                    time_difference = current_time - saved_time

                    # Calculate hours, minutes, and seconds
                    hours, remainder = divmod(time_difference.total_seconds(), 3600)
                    minutes, seconds = divmod(remainder, 60)

                    # Format the time difference as a string
                    formatted_time_difference = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
        except FileNotFoundError:
            return True

        # Get the current time and update the label
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.current_time_var.set(current_time)
        time_difference2 = formatted_time_difference
        self.time_difference_var.set(time_difference2)

        # Schedule the update_time function to run again after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_time)

    # Account creation functions
    def save_data(self):
        # Save dictionary
        with open('Dictionary.txt', 'w') as file:
            for username, password in self.dictionary.items():
                file.write(f"{username}:{password}\n")

        # Save login names
        with open('login_names.txt', 'w') as file:
            for username in self.login_names:
                file.write(f"{username}\n")

    def save_dictionary(self):
        with open('Dictionary.txt', 'w') as file:
            for username, password in self.dictionary.items():
                file.write(f"{username}:{password}\n")

    def save_account(self, new_username, new_password):
        encoded_password = self.hash_password(new_password)
        self.dictionary[new_username] = encoded_password
        self.login_names.append(new_username)
        self.save_data()
        self.logged_in_user = new_username
        self.show_login_screen()

    # Main menu functions
    def save_login_names(self):
        username = self.username_var.get()
        with open('login_names.txt', 'w') as file:
            file.write(f"{username}\n")

    def delete_account(self):
        if self.logged_in_user:
            confirm = messagebox.askyesno("Delete Account", "Are you sure you want to delete your account?")
            if confirm:
                # Remove the account from the dictionary
                del self.dictionary[self.logged_in_user]
                self.login_names.remove(self.logged_in_user)
                self.save_data()
                self.logged_in_user = None
                self.logout()

    def logout(self):
        self.logged_in_user = None
        self.logout_cleanup()
        self.show_login_screen()

    # Functions for setting theme and appearance
    def set_appearance(self):

        messagebox.showinfo("Appearance mode saved!", "you have successfully saved the appearance mode!")

        appearance_select = self.option_menu_appearance.get()

        with open("appearance.txt", "w") as file:
            file.write(appearance_select)

    def set_theme(self):

        confirm = messagebox.showinfo("Theme Saved", "The program will now restart to apply the theme!")

        if confirm:
            theme_select = self.option_menu_theme.get()

            with open("theme.txt", "w") as file:
                file.write(theme_select)
            self.restart_application()

    def restart_application(self):
        # Close the current application window
        self.root.destroy()

        # Restart the application using subprocess
        python_executable = sys.executable
        subprocess.Popen([python_executable, *sys.argv])


    # Static methods for login/out functions
    @staticmethod
    def load_dictionary():
        try:
            with open('Dictionary.txt', 'r') as file:
                lines = file.readlines()
                return {line.split(':')[0]: line.split(':')[1].strip() for line in lines if line.strip()}
        except FileNotFoundError:
            return {}

    @staticmethod
    def load_login_names():
        try:
            with open('login_names.txt', 'r') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            return []

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def show_login_error():
        messagebox.showerror("Login Error", "Invalid username or password!")

    @staticmethod
    def save_login_time():
        with open('target_date2.txt', 'w') as file:
            file.write(f"{datetime.datetime.now()}\n")

    @staticmethod
    def logout_cleanup():
        open('target_date2.txt', 'w').close()
        open('login_names.txt', 'w').close()

    # Static methods for launching main menu programs

    # Games
    @staticmethod
    def guess():
        guess_path = 'GuessNumber.py'

        # Use subprocess to launch the script
        subprocess.run(['python', guess_path])

    @staticmethod
    def sorting():
        sorting_path = 'Sortinghat.py'

        # Use subprocess to launch the script
        subprocess.run(['python', sorting_path])

    @staticmethod
    def magic():
        magic_path = 'Magic8.py'

        # Use subprocess to launch the script
        subprocess.run(['python', magic_path])

    @staticmethod
    def dice():
        dice_path = 'Dice.py'

        # Use subprocess to launch the script
        subprocess.run(['python', dice_path])

    @staticmethod
    def lotto():
        lotto_path = 'Lottery.py'

        # Use subprocess to launch the script
        subprocess.run(['python', lotto_path])

    @staticmethod
    def coin():
        coin_path = 'CoinFlip.py'

        # Use subprocess to launch the script
        subprocess.run(['python', coin_path])

    @staticmethod
    def black():
        black_path = 'Blackjack.py'

        # Use subprocess to launch the script
        subprocess.run(['python', black_path])

    @staticmethod
    def bomb():
        bomb_path = 'Bomb.py'

        # Use subprocess to launch the script
        subprocess.run(['python', bomb_path])

    @staticmethod
    def rad_rat():
        rat_path = 'radrat.py'

        # Use subprocess to launch the script
        subprocess.run(['python', rat_path])

    @staticmethod
    def cardcountgame():
        count_game_path = 'Cardcountgame.py'

        # Use subprocess to launch the script
        subprocess.run(['python', count_game_path])


    # Utilities
    @staticmethod
    def grade():
        grade_path = 'Grade.py'

        # Use subprocess to launch the script
        subprocess.run(['python', grade_path])

    @staticmethod
    def ph():
        ph_path = 'PH.py'

        # Use subprocess to launch the script
        subprocess.run(['python', ph_path])

    @staticmethod
    def quad():
        quad_path = 'Quadratic.py'

        # Use subprocess to launch the script
        subprocess.run(['python', quad_path])

    @staticmethod
    def bmi():
        bmi_path = 'BMI.py'

        # Use subprocess to launch the script
        subprocess.run(['python', bmi_path])

    @staticmethod
    def cash():
        cash_path = 'CashEx.py'

        # Use subprocess to launch the script
        subprocess.run(['python', cash_path])

    @staticmethod
    def temp():
        temp_path = 'TempConverter.py'

        # Use subprocess to launch the script
        subprocess.run(['python', temp_path])

    @staticmethod
    def fizz():
        fizz_path = 'FizzBuzz.py'

        # Use subprocess to launch the script
        subprocess.run(['python', fizz_path])

    @staticmethod
    def rand_day():
        rand_path = 'Randomday.py'

        # Use subprocess to launch the script
        subprocess.run(['python', rand_path])

    @staticmethod
    def count():
        count_path = 'Countdown.py'

        # Use subprocess to launch the script
        subprocess.run(['python', count_path])

    @staticmethod
    def prime():
        prime_path = 'Prime.py'

        # Use subprocess to launch the script
        subprocess.run(['python', prime_path])

    @staticmethod
    def delta():
        delta_path = 'Delta_v.py'

        # Use subprocess to launch the script
        subprocess.run(['python', delta_path])

    @staticmethod
    def potential():
        potential_path = 'Potentalenergy.py'

        # Use subprocess to launch the script
        subprocess.run(['python', potential_path])

    @staticmethod
    def e_mc2():
        e_mc2_path = 'E-mc2.py'

        # Use subprocess to launch the script
        subprocess.run(['python', e_mc2_path])

    @staticmethod
    def nuke():
        nuke_path = 'Nukedecay.py'

        # Use subprocess to launch the script
        subprocess.run(['python', nuke_path])

    @staticmethod
    def card_count():
        card_path = 'cardcounter.py'

        # Use subprocess to launch the script
        subprocess.run(['python', card_path])


# Function for starting application
def app_run():
    root = ctk.CTk()
    App(root)
    root.mainloop()


# Running main function on start
if __name__ == "__main__":
    app_run()

