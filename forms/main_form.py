from tkinter import ttk
from .base_form import BaseForm
from .settings_form import SettingsForm
from .game_form import GameForm
from .leaderboard_form import LeaderboardForm


class MainForm(BaseForm):
    def __init__(self):
        super().__init__(parent=None, title="Hangman", size="250x250")
        self.initialize_components()

    def initialize_components(self):
        self.components['btn_start'] = ttk.Button(
            self.container,
            text="Start",
            width=25,
            command=self.btn_start_click
        )
        self.components['btn_start'].place(anchor="center", relx=.5, rely=.5, y=-50)

        self.components['btn_settings'] = ttk.Button(
            text="Settings",
            width=25,
            command=self.btn_settings_click
        )
        self.components['btn_settings'].place(anchor="center", relx=.5, rely=.5, y=0)

        self.components['btn_leaderboard'] = ttk.Button(
            text="Leaderboard",
            width=25,
            command=self.btn_leaderboard_click
        )
        self.components['btn_leaderboard'].place(anchor="center", relx=.5, rely=.5, y=50)

    def btn_settings_click(self):
        settings_form = SettingsForm(self.window)
        settings_form.show_modal()

    def btn_start_click(self):
        game_form = GameForm(self.window)
        game_form.show_modal()

    def btn_leaderboard_click(self):
        leaderboard_form = LeaderboardForm(self.window)
        leaderboard_form.show_modal()
