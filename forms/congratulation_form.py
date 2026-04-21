from .base_form import BaseForm
import Data
from tkinter import ttk

class CongratulationForm(BaseForm):
    def __init__(self, parent=None, score: int = 0, time_taken: int = 999):
        super().__init__(parent=parent, title="Congratulations!", size="300x250")
        self.score = score
        self.time_taken = time_taken
        self.initialize_components()


    def initialize_components(self):
        self.components['lbl_congrats'] = ttk.Label(self.container, text="Congratulations! You won!", font=("Arial", 14))
        self.components['lbl_congrats'].grid(row=0, column=0, columnspan=2, padx=(5, 10), pady=10)

        self.components['lbl_score'] = ttk.Label(self.container, text=f"Score: {self.score}", font=("Arial", 12))
        self.components['lbl_score'].grid(row=1, column=0, columnspan=2, padx=(5, 10), pady=10, sticky="ew")

        self.components['lbl_time'] = ttk.Label(self.container, text=f"Time taken: {self.time_taken}", font=("Arial", 12))
        self.components['lbl_time'].grid(row=2, column=0, columnspan=2, padx=(5, 10), pady=10, sticky="ew")

        self.components["lbl_name"] = ttk.Label(self.container, text="Enter your name: ", font=("Arial", 12))
        self.components["lbl_name"].grid(row=3, column=0, padx=(10, 5), pady=10, sticky="ew")
        self.components['entry_name'] = ttk.Entry(self.container, width=20)
        self.components['entry_name'].grid(row=3, column=1, padx=(5, 10), pady=10, sticky="ew")

        self.components['btn_ok'] = ttk.Button(self.container, text="OK", width=10, command=self.save_result)
        self.components['btn_ok'].grid(row=4, column=0, columnspan=2, padx=(5, 10), pady=10)

    
    def save_result(self):
        name = self.components['entry_name'].get().strip()
        if name == "":
            self.show_error("Enter your name!")
            return
        Data.add_record(name, self.score, self.time_taken)
        super().on_closing()

