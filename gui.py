import tkinter as tk


class GameBoard(tk.Frame):
    def __init__(self, *nargs, **kwargs):
        super().__init__(*nargs, **kwargs)
        self.buttons = [[None for x in range(3)] for y in range(3)]
        self.create_buttons(text="", highlightbackground="grey")

    def create_buttons(self, **kwargs):
        maxrow = 3
        maxcol = 3
        for row in range(maxrow):
            for col in range(maxcol):
                self.buttons[row][col] = tk.Button(self, **kwargs)
                button = self.buttons[row][col]
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nesw")
            for x in range(maxrow):
                self.columnconfigure(x, weight=1)
            for x in range(maxcol):
                self.rowconfigure(x, weight=1)

    def click_button(self, row, column, label, color):
        button = self.buttons[row][column]
        button.config(highlightbackground=color)
        button.config(fg=color)
        button.config(text=label)



if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500, 500)
    board = GameBoard(root)
    board.pack(expand=True, fill="both")
    root.mainloop()
