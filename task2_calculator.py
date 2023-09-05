import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title(" Simple Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = ttk.Label(root, textvariable=self.result_var, font=("New Roman", 24))
        self.result_label.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for button_text, row, col in self.buttons:
            ttk.Button(root, text=button_text, command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            if current_text == "0":
                new_text = button_text
            else:
                new_text = current_text + button_text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()