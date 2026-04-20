import tkinter as tk
from tkinter import ttk, messagebox


class BaseForm:
    def __init__(self, parent=None, title: str = "Form", size: str = "800x600"):
        if parent is None:
            self.window = tk.Tk()
        else:
            self.window = tk.Toplevel(parent)
            self.window.transient(parent)
        
        self.window.title(title)
        self.window.geometry(size)
        self.parent = parent
        self.center_window()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.container = ttk.Frame(self.window)
        self.container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.components = {}
        self.dialog_result = None


    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')


    def on_closing(self):
        if self.parent:
            self.window.grab_release()
        self.window.destroy()


    def show_dialog(self, message: str, title: str = "Info"):
        messagebox.showinfo(title, message)


    def show_error(self, message: str, title: str = "Error"):
        messagebox.showerror(title, message)


    def show_question(self, message: str, title: str = "Question") -> bool:
        return messagebox.askyesno(title, message)
    

    def show_modal(self):
        self.window.grab_set()
        self.window.focus_force()
        self.window.wait_window()
        return self.dialog_result
    
    
    def mainloop(self):
        if self.parent is None:
            self.window.mainloop()
        else:
            self.window.wait_window()