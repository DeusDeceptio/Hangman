from tkinter import *
from tkinter import ttk
from .base_form import BaseForm

class LeaderboardForm(BaseForm):
    def __init__(self, parent=None):
        super().__init__(parent=parent, title="Leaderboard", size="400x300")
        self.initialize_components()

    def initialize_components(self):
        pass