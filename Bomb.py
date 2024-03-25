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

# Global Variable for scope
global selected_list

# Class that holds entire app
class BombDefusingGame:

    # App initialization settings and gui
    def __init__(self, master):


        self.root = master
        self.root.title("Bomb Defused!")


        self.difficulty_var = tk.StringVar()
        self.difficulty_combobox = None
        self.hard_tasks = None
        self.medium_tasks = None
        self.easy_tasks = None
        self.task_stat_label = None

        self.bombs_defused = 0
        self.money = 10000
        self.time_remaining = 0
        self.tasks_completed = 0
        self.max_tasks = 2
        self.max_attempts = 5
        self.attempts = 0

        self.task_difficulty = [
            "Easy bombs $3000",
            "Medium bombs $4000",
            "Hard bombs $5000",
        ]

        self.easy_tasks = [
            self.enter_random_string,
            self.press_and_hold_button,
            self.select_right_button,
            self.guess_number,
        ]

        self.medium_tasks = [
            self.math_challenge,
            self.code_breaking,
            self.trivia_question,
        ]

        self.hard_tasks = [
            self.chemical_element_identification,
            self.riddle_solving,
            self.math_puzzle,
        ]

        self.strings = [
            "PENIS",
            "BOOB",
            "BOOM",
            "TICK",
        ]


        self.master_frame= ctk.CTkFrame(self.root)
        self.master_frame.grid(row=0, column=0, padx=10, pady=10)


        self.label_frame = ctk.CTkFrame(self.master_frame)
        self.label_frame.grid(row=0, column=0, padx=10, pady=10)

        # GUI elements
        self.defused_label = ctk.CTkLabel(self.label_frame, text="Bombs Defused: 0")
        self.defused_label.grid(row=0,column=0, padx=10, pady=10)

        self.money_label = ctk.CTkLabel(self.label_frame, text="Money: $10000")
        self.money_label.grid(row=1,column=0, padx=10, pady=10)

        self.time_label = ctk.CTkLabel(self.label_frame, text="Time Remaining: 0:00")
        self.time_label.grid(row=2,column=0, padx=10, pady=10)

        self.attempts_label = ctk.CTkLabel(self.label_frame, text="Attempts Left: 5")
        self.attempts_label.grid(row=3,column=0, padx=10, pady=10)

        self.tasks_completed_label = ctk.CTkLabel(self.label_frame, text="Tasks Completed: 0")
        self.tasks_completed_label.grid(row=4,column=0, padx=10, pady=10)


        self.scroll_frame = ctk.CTkFrame(self.master_frame)
        self.scroll_frame.grid(row=0, column=1, padx=10, pady=10)

        self.task_label = ctk.CTkLabel(self.scroll_frame, text="")
        self.task_label.grid(row=0,column=0, padx=10, pady=10)

        self.taskframe = ctk.CTkScrollableFrame(self.scroll_frame, width=200, height=50)
        self.taskframe.grid(row=1,column=0, padx=10, pady=10)

        self.start_button = ctk.CTkButton(self.master_frame, text="Defuse Bomb!", command=self.start_game)
        self.start_button.grid(row=2, column=1, padx=10, pady=10)

        self.end_frame = ctk.CTkFrame(self.master_frame)

        self.difficulty_combobox = ctk.CTkComboBox(self.master_frame, variable=self.difficulty_var, values=self.task_difficulty)
        self.difficulty_combobox.set("Easy bombs $3000")
        self.difficulty_combobox.grid(row=2, column=0, padx=10, pady=10)

        # Load saved data
        self.load_saved_data()


    # Data loading and saving functions for saved games
    def load_saved_data(self):
        try:
            with open("bomb.txt", "r") as file:
                data = file.readline().split()
                if len(data) == 3:
                    self.bombs_defused, self.money, _ = map(int, data)
                    self.update_display()
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("bomb.txt", "w") as file:
            file.write(f"{self.bombs_defused} {self.money} 0")


    # Function for updating various displays in game
    def update_display(self):
        self.defused_label.configure(text=f"Bombs Defused: {self.bombs_defused}")
        self.money_label.configure(text=f"Money: ${self.money}")
        self.attempts_label.configure(text=f"Attempts Left: {self.max_attempts - self.attempts}")
        self.tasks_completed_label.configure(text=f"Tasks Completed: {self.tasks_completed}")

    def update_time_display(self):

        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.time_label.configure(text=f"Time Remaining: {minutes}:{seconds:02}")
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.root.after(1000, self.update_time_display)
        else:
            self.end_game()


    # Function that clears the game display and starts a new bomb
    def start_game(self):
        self.clear_game()
        self.start_next_bomb()

    # Function for initializing the current bomb defusing attempt
    def start_next_bomb(self):
        self.time_remaining = random.randint(120, 300)
        self.tasks_completed = 0
        self.attempts = 0
        self.money -= 1000  # Deduct 1000 dollars for attempting to defuse the bomb
        self.update_display()
        self.update_time_display()
        self.run_task()

    # Function for end game logic and gui
    def end_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.time_remaining = 0

        self.master_frame = ctk.CTkFrame(root)
        self.master_frame.grid(row=0, column=0, padx=10, pady=10)

        self.end_frame = ctk.CTkFrame(self.master_frame)
        self.end_frame.grid(row=0, column=0, padx=10, pady=10)

        if self.tasks_completed >= self.max_tasks:
            self.bombs_defused += 1
            ctk.CTkLabel(self.end_frame, text=f"Congratulations! You defused {self.bombs_defused} bombs!").grid(row=0, column=0, padx=10, pady=10)
            task_list = self.difficulty_var.get()

            if task_list == "Easy bombs $3000":
                self.money += 3000
            elif task_list == "Medium bombs $4000":
                self.money += 4000
            elif task_list == "Hard bombs $5000":
                self.money += 5000

        elif self.time_remaining <= 0:
            ctk.CTkLabel(self.end_frame, text="Sorry, you ran out of time!").grid(row=0, column=0, padx=10, pady=10)
        else:
            ctk.CTkLabel(self.end_frame, text=f"Sorry, you failed to defuse the bomb after {self.max_attempts} attempts.").grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkLabel(self.end_frame, text=f"Total money: ${self.money}").grid(row=1, column=0, padx=10, pady=10)

        ctk.CTkButton(self.end_frame, text="Defuse Bomb!", command=self.start_game).grid(row=3, column=0, padx=10, pady=10)

        self.difficulty_combobox = ctk.CTkComboBox(self.end_frame, variable=self.difficulty_var, values=self.task_difficulty)
        self.difficulty_combobox.set("Easy bombs $3000")
        self.difficulty_combobox.grid(row=2, column=0, padx=10, pady=10)

        ctk.CTkButton(self.end_frame, text="Save Game", command=self.save_data).grid(row=4, column=0, padx=10, pady=10)

        ctk.CTkButton(self.end_frame, text="Reset Game", command=self.reset_game).grid(row=5, column=0, padx=10, pady=10)

        ctk.CTkButton(self.end_frame, text="Quit", command=self.root.destroy).grid(row=6, column=0, padx=10, pady=10)

    # Function for resetting (deleting) your game
    def reset_game(self):
        self.bombs_defused = 0
        self.money = 10000
        self.save_data()
        self.update_display()

    def clear_frame(self):
        for widgets in self.taskframe.winfo_children():
            widgets.destroy()

    # Function for clearing the game when you finish a game and gui
    def clear_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.master_frame = ctk.CTkFrame(root)
        self.master_frame.grid(row=0, column=0, padx=10, pady=10)


        self.label_frame = ctk.CTkFrame(self.master_frame)
        self.label_frame.grid(row=0, column=0, padx=10, pady=10)

        self.defused_label = ctk.CTkLabel(self.label_frame, text=f"Bombs Defused: {self.bombs_defused}")
        self.defused_label.grid(row=0, column=0, padx=10, pady=10)

        self.money_label = ctk.CTkLabel(self.label_frame, text=f"money: {self.money}")
        self.money_label.grid(row=1, column=0, padx=10, pady=10)

        self.time_label = ctk.CTkLabel(self.label_frame, text="Time Remaining: 0:00")
        self.time_label.grid(row=2, column=0, padx=10, pady=10)

        self.attempts_label = ctk.CTkLabel(self.label_frame, text="Attempts Left: 5")
        self.attempts_label.grid(row=3, column=0, padx=10, pady=10)

        self.tasks_completed_label = ctk.CTkLabel(self.label_frame, text="Tasks Completed: 0")
        self.tasks_completed_label.grid(row=4, column=0, padx=10, pady=10)


        self.scroll_frame = ctk.CTkFrame(self.master_frame)
        self.scroll_frame.grid(row=0, column=1, padx=10, pady=10)

        self.task_label = ctk.CTkLabel(self.scroll_frame, text="")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        self.taskframe = ctk.CTkScrollableFrame(self.scroll_frame, width=200, height=50)
        self.taskframe.grid(row=1, column=0, padx=10, pady=10)


        self.task_stat_label = ctk.CTkLabel(self.master_frame, text="")
        self.task_stat_label.grid(row=2, column=1, columnspan=2, padx=10, pady=10)


    # Function for selecting a function if the game allows it
    def run_task(self):
        global selected_list

        if self.tasks_completed >= self.max_tasks or self.attempts >= self.max_attempts or self.time_remaining <= 0:
            self.end_game()
        else:
            task_list = self.difficulty_var.get()

            if task_list == "Easy bombs $3000":
                selected_list = self.easy_tasks
            elif task_list == "Medium bombs $4000":
                selected_list = self.medium_tasks
            elif task_list == "Hard bombs $5000":
                selected_list = self.hard_tasks

            task = random.choice(selected_list)
            task()

    # Easy Task functions
    def enter_random_string(self):
        string = random.choice(self.strings)
        res = string[0].upper() + string[1:].lower()
        self.task_label.configure(text=f"Enter this string: {res}")
        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        def check_string():
            if entry.get().upper() == str(string):
                self.task_completed("String entered successfully!")
            else:
                self.task_failed("String entered incorrectly!")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_string).pack(pady=10)

    def press_and_hold_button(self):
        self.task_label.configure(text="Press and hold the button")

        def hold_button():
            self.task_completed("Button held successfully!")

        button = ctk.CTkButton(self.taskframe, text="Hold me", command=lambda: self.root.after(3000, hold_button))
        button.pack(pady=10)

    def select_right_button(self):
        self.task_label.configure(text="Select the right button")

        correct_button = random.randint(1, 3)

        def check_button(button_num):
            if button_num == correct_button:
                self.task_completed("Correct button selected!")
            else:
                self.task_failed("Incorrect button selected!")

        ctk.CTkButton(self.taskframe, text="Button 1", command=lambda: check_button(1)).pack(pady=5)
        ctk.CTkButton(self.taskframe, text="Button 2", command=lambda: check_button(2)).pack(pady=5)
        ctk.CTkButton(self.taskframe, text="Button 3", command=lambda: check_button(3)).pack(pady=5)

    def guess_number(self):
        self.task_label.configure(text="Guess the number (1-10)")

        correct_number = random.randint(1, 10)

        def check_number():
            try:
                guess = int(entry.get())
                if guess == correct_number:
                    self.task_completed("Number guessed correctly!")
                else:
                    self.task_failed("Number guessed incorrectly!")
            except ValueError:
                pass

        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)
        ctk.CTkButton(self.taskframe, text="Submit", command=check_number).pack(pady=10)


    # Medium task functions
    def math_challenge(self):
        # Generate a random math problem
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])

        # Display the math problem to the player
        problem = f"{num1} {operator} {num2} = ?"

        # Get the player's input
        self.task_label.configure(text=f"Solve the math problem: {problem} ")
        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        def check_answer():
            correct_answer = eval(f"{num1} {operator} {num2}")
            try:
                if int(entry.get()) == correct_answer:
                    self.task_completed("number entered successfully!")
                else:
                    self.task_failed("number entered incorrectly!")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_answer).pack(pady=10)

    def code_breaking(self):
        # List of words for code breaking
        words = ["python", "programming", "code", "challenge", "game", "developer", "computer"]

        # Select a random word
        selected_word = random.choice(words)

        # Scramble the letters of the word
        scrambled_word = ''.join(random.sample(selected_word, len(selected_word)))

        # Display the scrambled word to the player
        self.task_label.configure(text=f"Code to break: {scrambled_word}")

        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        def check_answer():
            try:
                if entry.get().lower() == selected_word:
                    self.task_completed("Correct! Code breaking successful.")
                else:
                    self.task_failed(f"Incorrect. The correct word is '{selected_word}'. Bomb exploded!")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_answer).pack(pady=10)

    def trivia_question(self):
        # List of trivia questions and their correct answers
        questions_and_answers = {
            "What is the capital of France?": "Paris",
            "In which year did the Titanic sink?": "1912",
            "Who painted the Mona Lisa?": "Leonardo da Vinci",
            "What is the largest planet in our solar system?": "Jupiter",
            "How many continents are there in the world?": "7",
            "Which famous scientist developed the theory of relativity?": "Einstein"
        }

        # Select a random trivia question
        selected_question = random.choice(list(questions_and_answers.keys()))

        # Display the trivia question to the player
        self.task_label.configure(text="Trivia Question: " + selected_question)

        # Get the player's input
        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        # Check if the player's answer is correct
        def check_answer():
            try:
                if entry.get().lower() == questions_and_answers[selected_question].lower():
                    self.task_completed("Correct! Trivia question answered.")
                else:
                    correct_answer = questions_and_answers[selected_question]
                    self.task_failed(f"Incorrect. The correct answer is {correct_answer}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_answer).pack(pady=10)


    # Hard task functions
    def chemical_element_identification(self):
        # List of chemical elements
        elements = [
            {"symbol": "H", "name": "Hydrogen"},
            {"symbol": "He", "name": "Helium"},
            {"symbol": "Li", "name": "Lithium"},
            {"symbol": "Be", "name": "Beryllium"},
            {"symbol": "B", "name": "Boron"},
            {"symbol": "C", "name": "Carbon"},
            {"symbol": "N", "name": "Nitrogen"},
            # ... add more elements as needed
        ]

        # Select a random element
        selected_element = random.choice(elements)

        # Display the symbol of the element to the player
        self.task_label.configure(text=f"Name Chemical element: {selected_element['symbol']}")

        # Get the player's input
        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        # Check if the player's guess is correct
        if entry.get().capitalize() == selected_element['name']:
            print("Correct! Chemical element identified.")
        else:
            print(f"Incorrect. The correct element is {selected_element['name']}. Bomb exploded!")


        def check_answer():
            try:
                if entry.get().capitalize() == selected_element['name']:
                    self.task_completed("Correct! Code breaking successful.")
                else:
                    self.task_failed(f"Incorrect. The correct element is {selected_element['name']}. Bomb exploded!")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_answer).pack(pady=10)

    def riddle_solving(self):
        # List of riddles
        riddles = [
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "The more you take, the more you leave behind. What am I?",
            "I can fly without wings. I can cry without eyes. Wherever I go, darkness follows me. What am I?",
            "The person who makes it, sells it. The person who buys it never uses it. What is it?",
            "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "What has keys but can't open locks?"
        ]

        # Select a random riddle
        selected_riddle = random.choice(riddles)

        # Display the riddle to the player
        self.task_label.configure(text="Riddle: " + selected_riddle)

        # Get the player's input
        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        def check_answer():
            try:
                # Check if the player's guess is correct
                riddle_lower = selected_riddle.lower()
                if "wind" in riddle_lower and "echo" in entry.get().lower():
                    self.task_completed("Correct! Riddle solved.")
                elif "take" in riddle_lower and "footsteps" in entry.get().lower():
                    self.task_completed("Correct! Riddle solved.")
                elif "fly" in riddle_lower and "a star" in entry.get().lower():
                    self.task_completed("Correct! Riddle solved.")
                elif "makes it" in riddle_lower and "a coffin" in entry.get().lower():
                    self.task_completed("Correct! Riddle solved.")
                elif "mine" in riddle_lower and "a pencil" in entry.get().lower():
                    self.task_completed("Correct! Riddle solved.")
                elif "keys" in riddle_lower and "a piano" in entry.get().lower():
                    self.task_completed("Correct! Riddle solved.")
                else:
                    self.task_failed(f"Incorrect. The correct answer is {selected_riddle}. Bomb exploded!")


            except ValueError:
                print("Invalid input. Please enter a valid number.")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_answer).pack(pady=10)

    def math_puzzle(self):
        # Generate a random math puzzle
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        operator1 = random.choice(['+', '-'])
        operator2 = random.choice(['*', '/'])

        # Display the math puzzle to the player
        self.task_label.configure(text=f"{num1} {operator1} {num2} {operator2} {num3}")

        # Get the player's input
        entry = ctk.CTkEntry(self.taskframe)
        entry.pack(pady=10)

        # Check if the player's answer is correct
        def check_answer():
            try:
                correct_answer = eval(f"{num1} {operator1} {num2} {operator2} {num3}")
                user_answer = int(entry.get())
                if user_answer == correct_answer:
                    self.task_completed("Correct! puzzle solved.")
                else:
                    self.task_failed(f"Incorrect. The correct answer is {correct_answer}. Bomb exploded!")

                    # Handle the game over logic here
            except ValueError:
                self.task_label.configure(text="Invalid input. Please enter a valid number.")

        ctk.CTkButton(self.taskframe, text="Submit", command=check_answer).pack(pady=10)


    # Functions for when tasks are either complete or failed
    def task_completed(self, message):
        self.tasks_completed += 1
        self.update_display()
        self.task_stat_label.configure(text=f"{message}")
        self.root.after(2000, self.run_task)
        self.clear_frame()

    def task_failed(self, message):
        self.attempts += 1
        self.update_display()
        self.task_stat_label.configure(text=f"{message}")
        self.root.after(2000, self.run_task)
        self.clear_frame()


if __name__ == "__main__":
    root = ctk.CTk()
    game = BombDefusingGame(root)
    root.mainloop()

