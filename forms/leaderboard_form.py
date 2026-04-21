from tkinter import ttk
from .base_form import BaseForm
import Data

class LeaderboardForm(BaseForm):
    def __init__(self, parent=None):
        super().__init__(parent=parent, title="Leaderboard", size="400x300")
        self.initialize_components()

    def initialize_components(self):
        self.initialize_leaderboard()
        self.print_leaderboard()


    def initialize_leaderboard(self):
        self.components['lbl_title'] = ttk.Label(self.container, text="Top Players", font=("Arial", 16))
        self.components['lbl_title'].pack(pady=10, anchor="n")
        self.components['table'] = ttk.Treeview(self.container, columns=("Name", "Score", "Time"), show="headings")
        self.components['table'].heading("Name", text="Name")
        self.components['table'].heading("Score", text="Score")
        self.components['table'].heading("Time", text="Time")
        self.components['table'].column("Name", width=150, anchor="center")
        self.components['table'].column("Score", width=100, anchor="center")
        self.components['table'].column("Time", width=100, anchor="center")
        self.components['table'].pack(fill="both", expand=True)


    def print_leaderboard(self):
        self.leaderboard = Data.get_leaderboard()
        self.leaderboard = Data.sort_leaderboard(self.leaderboard)
        self.fill_leaderboard(self.leaderboard)


    def fill_leaderboard(self, leaderboard: list):
        for record in leaderboard:
            self.components['table'].insert(parent="", index="end", values=(record["name"], record["score"], record["time"]))