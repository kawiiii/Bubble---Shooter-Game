import tkinter as tk


class UsernamePopupWindow:
    color_background = '#047E97'

    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent, height=300, width=300, bg=self.color_background)
        self.username = tk.StringVar()

        label = tk.Label(self.toplevel, text="Enter username:", bg=self.color_background)
        entry_field = tk.Entry(self.toplevel, textvariable=self.username)
        button = tk.Button(self.toplevel, text="Submit", command=self.toplevel.destroy)

        label.pack(side="top", fill="x", padx=10, pady=10)
        entry_field.pack(side="top", fill="x", padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def show(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = self.username.get()
        return value


class AboutPopupWindow:
    filename = '../docs/about_text.txt'  # file with about-text
    color_background = '#047E97'

    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent, height=300, width=300, bg=self.color_background)
        self.username = tk.StringVar()

        # load about-text from file
        text = self.load_about_text()

        # create a label that contains loaded about-text
        label = tk.Label(self.toplevel,
                         text=text,
                         bg=self.color_background)
        label.pack(padx=10, pady=10)

    def load_about_text(self):
        """
        loads an about-text from specific file
        """
        with open(self.filename) as file:
            return file.read()
