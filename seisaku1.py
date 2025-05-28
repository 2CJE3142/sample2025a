import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("三目並べ")
        self.current_player = "○"
        self.buttons = []
        self.game_over = False
        self.create_board()
        self.create_reset_button()

    def create_board(self):
        board_frame = tk.Frame(self.root, bd=5, relief="solid")
        board_frame.grid(row=0, column=0, padx=10, pady=10)

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    board_frame, text="", font=("Arial", 32), width=5, height=2,
                    command=lambda r=row, c=col: self.on_click(r, c),
                    relief="solid", borderwidth=2
                )
                button.grid(row=row, column=col)
                self.buttons.append(button)

    def create_reset_button(self):
        reset_btn = tk.Button(
            self.root, text="リセット", font=("Arial", 16), width=15,
            command=self.reset_game
        )
        reset_btn.grid(row=1, column=0, pady=10)

    def on_click(self, row, col):
        if self.game_over:
            return

        index = row * 3 + col
        button = self.buttons[index]

        if button["text"] == "":
            button["text"] = self.current_player
            if self.check_winner(self.current_player):
                messagebox.showinfo("勝利", f"{self.current_player} の勝ちです！")
                self.game_over = True
            elif all(b["text"] != "" for b in self.buttons):
                messagebox.showinfo("引き分け", "引き分けです。")
                self.game_over = True
            else:
                self.current_player = "×" if self.current_player == "○" else "○"

    def check_winner(self, player):
        combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横判定
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦判定
            [0, 4, 8], [2, 4, 6]              # 斜め判定
        ]
        return any(all(self.buttons[i]["text"] == player for i in combo) for combo in combos)

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
        self.current_player = "○"
        self.game_over = False

# アプリ起動
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
