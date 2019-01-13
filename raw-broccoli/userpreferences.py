import tkinter as tk
from tkinter import ttk

prefs = {"Language": "en_GB"}
    
def get_prefs(self):
        return self.prefs

class PreferencesWindow():
    def __init__ (self):
        self.rootwindow = tk.Tk()
        self.rootwindow.iconbitmap(default='img\\broccoli.ico')
        self.rootwindow.title("User Preferences")

        self.rootwindow.resizable(width=tk.FALSE, height=tk.FALSE)
        self.rootwindow.geometry("%sx%s"%(self.rootwindow.winfo_reqwidth(), 100))

        self.language()

        self.confirm_button = tk.Button(self.rootwindow, text="Confirm", command=self.confirm)
        self.confirm_button.grid(row=1, column=0)

        self.cancel_button = tk.Button(self.rootwindow, text="Cancel", command = lambda: self.rootwindow.destroy())
        self.cancel_button.grid(row=1, column=1)

        #Root Window draw
        self.rootwindow.update()
        self.rootwindow.mainloop()

    def language(self):
        languages = ["en_GB", "en_US", "es", "fr_FR", "pt_PT"]

        langlabel = tk.Label(self.rootwindow, text="Language")
        langlabel.grid(row=0, column=0)

        self.lang = tk.ttk.Combobox(self.rootwindow, state="readonly", width = 15)
        self.lang.set(prefs["Language"])
        self.lang["values"] = languages
        self.lang.grid(row=0, column=1)

    def confirm(self):
        prefs["Language"] = self.lang.get()
        self.rootwindow.destroy()

#pw = PreferencesWindow()
