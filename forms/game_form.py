import Data
import datetime
from tkinter import Canvas, END
from tkinter import ttk
from .base_form import BaseForm
from .congratulation_form import CongratulationForm

class GameForm(BaseForm):
    def __init__(self, parent=None):
        super().__init__(parent=parent, title="Game", size="425x350")
        self.initialize_components()
        
        
    def initialize_components(self):
        self.initialize_canvas()
        self.initialize_submit()
        settings = Data.get_settings()
        self.diff = settings["diff"]
        self.length = settings["length"]
        self.word = Data.get_word(diff=self.diff, length=self.length)
        self.unused_letters = "abcdefghijklmnopqrstuvwxyz  "
        self.visible_word = "_ " * len(self.word)
        self.score = 0
        self.mistakes = 0
        self.print_word(self.visible_word)
        self.print_unused_letters()
        self.start_time = datetime.datetime.now()


    def initialize_canvas(self):        
        self.components['canvas'] = Canvas(self.container, bg="white", width=400, height=250)
        self.components['canvas'].grid(row=0, column=0, columnspan=2)
        self.components['canvas'].create_line(50, 180, 150, 180, width=2)
        self.components['canvas'].create_line(100, 180, 100, 30, width=2)
        self.components['canvas'].create_line(100, 30, 200, 30, width=2)
        self.components['canvas'].create_line(200, 30, 200, 50, width=2)
        self.components['counter'] = ttk.Label(self.components['canvas'], text="Mistakes 0 out of 6")
        self.components['counter'].place(x=250, y=10)
        self.components['score'] = ttk.Label(self.components['canvas'], text="Score: 0")
        self.components['score'].place(x=250, y=30)


    def initialize_submit(self):
        self.components['entry'] = ttk.Entry(self.container, width=20)
        self.components['entry'].grid(row=1, column=0, padx=(10, 5), pady=10, sticky="ew")
        self.components['btn_submit'] = ttk.Button(
            self.container, 
            text="Submit", 
            width=8,
            command=self.submit_click
        )
        self.components['btn_submit'].grid(row=1, column=1, padx=(5, 10), pady=10, sticky="ew")


    def print_word(self, text):
        self.components['canvas'].delete("word")
        self.components['canvas'].create_text(200, 220, text=text, font=("Arial", 20), tags="word")


    def add_mistake(self):
        self.mistakes += 1
        self.update_score(-self.diff * self.length)
        self.components['counter'].config(text=f"Mistakes {self.mistakes} out of 6")
        match self.mistakes:
            case 1:
                self.components['canvas'].create_oval(175, 50, 225, 100, width=2)
            case 2:                
                self.components['canvas'].create_line(200, 100, 200, 150, width=2)
            case 3:                
                self.components['canvas'].create_line(200, 110, 180, 130, width=2)
            case 4:                
                self.components['canvas'].create_line(200, 110, 220, 130, width=2)
            case 5:                
                self.components['canvas'].create_line(200, 150, 180, 170, width=2)
            case 6:                
                self.components['canvas'].create_line(200, 150, 220, 170, width=2)
                self.show_dialog(f"Game over! The word was: {self.word}")
                self.on_closing()


    def update_score(self, points: int):
        self.score += points
        self.components['score'].config(text=f"Score: {self.score}")


    def print_unused_letters(self):
        self.components['canvas'].delete("letters")
        letters = ""
        for i in range(0, 4):
            for j in range(i*7, i*7+7):
                letters += " " + self.unused_letters[j]
            letters += "\n"
        self.components['canvas'].create_text(300, 100, text=f"Unused letters:\n{letters}", font=("Arial", 10), tags="letters")


    def congratulations(self):
        end_time = datetime.datetime.now()
        time_taken = int((end_time - self.start_time).total_seconds())
        congratulation_form = CongratulationForm(parent=self, score=self.score, time_taken=time_taken)
        congratulation_form.show_modal()
        self.on_closing()


    def create_display_word(self, letter: str) -> str:
        displayed_word = ""
        for l in self.word:
            if l in letter or l in self.visible_word:
                displayed_word += l + " "
            else:
                displayed_word += "_ "
        return displayed_word


    def check_letter(self, letter: str) -> bool:
        if letter not in self.unused_letters:
            return True
        self.unused_letters = self.unused_letters.replace(letter, " ")
        self.print_unused_letters()
        if letter in self.word:
            displayed_word = self.create_display_word(letter)
            self.print_word(displayed_word)
            self.visible_word = displayed_word
            if "_" not in displayed_word:
                self.congratulations()
            self.update_score(self.diff * self.length * 2)
            return True
        return False


    def submit_click(self):
        user_input = self.components['entry'].get()
        self.components['entry'].delete(0, END)
        user_input = user_input.lower().strip()
        if len(user_input) == 1 and self.check_letter(user_input):
            return
        elif len(user_input) > 1 and user_input == self.word:
            self.update_score(self.diff * self.length * 3)
            self.congratulations()
        self.add_mistake()
            