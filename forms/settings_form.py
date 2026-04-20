from tkinter import *
from tkinter import ttk
from .base_form import *
import Data

class SettingsForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent=parent, title="Settings", size="200x250")
        self.initialize_components()
        settings = Data.load_settings()
        self.components['spb_diff'].set(settings['diff'])
        self.components['spb_len'].set(settings['length'])

    def initialize_components(self):
        self.initialize_diff()
        self.initialize_length()

        self.components['btn_save'] = ttk.Button(
            self.container,
            text="Save",
            width=10,
            command=self.on_closing
        )
        self.components['btn_save'].place(anchor="c", relx=.5, rely=.5, y=80)


    def initialize_diff(self):
        self.components['lbl_diff'] = ttk.Label(
            self.container,
            text="Difficulty\n* 1 - common\n* 5 - very rare",
        )
        self.components['lbl_diff'].place(anchor="c", relx=.5, rely=.5, y=-80)

        self.components['spb_diff'] = ttk.Spinbox(
            self.container, 
            from_=1, to=5, 
            width=10
        )
        self.components['spb_diff'].place(anchor="c", relx=.5, rely=.5, y=-40)

    
    def initialize_length(self):
        self.components['lbl_len'] = ttk.Label(
            self.container, 
            text="Word length"
        )
        self.components['lbl_len'].place(anchor="c", relx=.5, rely=.5, y=0)

        self.components['spb_len'] = ttk.Spinbox(
            self.container, 
            from_=5, to=15, 
            width=10
        )
        self.components['spb_len'].place(anchor="c", relx=.5, rely=.5, y=20)


    def on_closing(self):
        diff = self.components['spb_diff'].get()
        length = self.components['spb_len'].get()
        diff = int(diff) if diff.isdigit() else 3
        length = int(length) if length.isdigit() else 6
        Data.save_settings(diff, length)
        self.window.grab_release()
        self.window.destroy()

