import math
import tkinter as tk
from tkinter import messagebox


class AlphaBetaTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Alpha-Beta Tic-Tac-Toe")
        self.root.resizable(False, False)

        self.human = "X"
        self.ai = "O"
        self.board = [""] * 9
        self.game_started = False
        self.game_over = False
        self.human_turn = True

        self.status = tk.StringVar(value="Choose first player")
        self.cells = []
        self._build_ui()

    def _build_ui(self):
        wrap = tk.Frame(self.root, padx=12, pady=12)
        wrap.pack()

        tk.Label(wrap, text="Tic-Tac-Toe", font=("Consolas", 14, "bold")).grid(
            row=0, column=0, columnspan=3, pady=(0, 8)
        )
        tk.Label(wrap, textvariable=self.status, font=("Consolas", 10), fg="#1f4e79").grid(
            row=1, column=0, columnspan=3, pady=(0, 10)
        )

        board_frame = tk.Frame(wrap)
        board_frame.grid(row=2, column=0, columnspan=3)
        for idx in range(9):
            r, c = divmod(idx, 3)
            btn = tk.Button(
                board_frame,
                text="",
                width=6,
                height=3,
                font=("Consolas", 16, "bold"),
                command=lambda i=idx: self.play_human(i),
            )
            btn.grid(row=r, column=c, padx=3, pady=3)
            self.cells.append(btn)

        control = tk.Frame(wrap)
        control.grid(row=3, column=0, columnspan=3, pady=(10, 0))
        tk.Button(control, text="Human First", width=11, command=lambda: self.start(True)).grid(
            row=0, column=0, padx=4
        )
        tk.Button(control, text="AI First", width=11, command=lambda: self.start(False)).grid(
            row=0, column=1, padx=4
        )
        tk.Button(control, text="Reset", width=11, command=self.reset).grid(row=0, column=2, padx=4)

        self.set_board_enabled(False)

    def start(self, human_first):
        self.board = [""] * 9
        self.game_started = True
        self.game_over = False
        self.human_turn = human_first
        self.refresh()
        if human_first:
            self.status.set("Your turn")
            self.set_board_enabled(True)
        else:
            self.status.set("AI thinking...")
            self.set_board_enabled(False)
            self.root.after(200, self.play_ai)

    def reset(self):
        self.board = [""] * 9
        self.game_started = False
        self.game_over = False
        self.human_turn = True
        self.status.set("Choose first player")
        self.refresh()
        self.set_board_enabled(False)

    def play_human(self, idx):
        if not self.game_started or self.game_over or not self.human_turn:
            return
        if self.board[idx] != "":
            return

        self.board[idx] = self.human
        self.refresh()
        if self.finish_if_needed():
            return

        self.human_turn = False
        self.status.set("AI thinking...")
        self.set_board_enabled(False)
        self.root.after(120, self.play_ai)

    def play_ai(self):
        if self.game_over:
            return
        move = self.get_best_move()
        if move is not None:
            self.board[move] = self.ai
        self.refresh()
        if self.finish_if_needed():
            return
        self.human_turn = True
        self.status.set("Your turn")
        self.set_board_enabled(True)

    def finish_if_needed(self):
        result = self.judge(self.board)
        if result is None:
            return False

        self.game_over = True
        self.set_board_enabled(False)
        if result == "draw":
            self.status.set("Draw")
            messagebox.showinfo("Result", "Draw")
        elif result == self.human:
            self.status.set("You win")
            messagebox.showinfo("Result", "You win")
        else:
            self.status.set("AI wins")
            messagebox.showinfo("Result", "AI wins")
        return True

    def get_best_move(self):
        best_score = -math.inf
        best_move = None
        for mv in self.legal_moves(self.board):
            self.board[mv] = self.ai
            score = self.alpha_beta(self.board, maximizing=False, alpha=-math.inf, beta=math.inf)
            self.board[mv] = ""
            if score > best_score:
                best_score = score
                best_move = mv
        return best_move

    def alpha_beta(self, board, maximizing, alpha, beta):
        terminal = self.judge(board)
        if terminal is not None:
            if terminal == self.ai:
                return 1
            if terminal == self.human:
                return -1
            return 0

        if maximizing:
            value = -math.inf
            for mv in self.legal_moves(board):
                board[mv] = self.ai
                value = max(value, self.alpha_beta(board, False, alpha, beta))
                board[mv] = ""
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value

        value = math.inf
        for mv in self.legal_moves(board):
            board[mv] = self.human
            value = min(value, self.alpha_beta(board, True, alpha, beta))
            board[mv] = ""
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

    def refresh(self):
        for i, btn in enumerate(self.cells):
            mark = self.board[i]
            color = "#c0392b" if mark == "X" else "#1f618d" if mark == "O" else "black"
            btn.config(text=mark, fg=color)

    def set_board_enabled(self, enabled):
        state = tk.NORMAL if enabled else tk.DISABLED
        for btn in self.cells:
            btn.config(state=state)

    @staticmethod
    def legal_moves(board):
        return [i for i, x in enumerate(board) if x == ""]

    @staticmethod
    def judge(board):
        lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in lines:
            if board[a] and board[a] == board[b] == board[c]:
                return board[a]
        if all(cell != "" for cell in board):
            return "draw"
        return None


def run():
    root = tk.Tk()
    AlphaBetaTicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    run()
