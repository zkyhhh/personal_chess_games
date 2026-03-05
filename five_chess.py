import tkinter as tk
from tkinter import messagebox


class GomokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku")
        self.root.resizable(False, False)

        self.board_size = 15
        self.cell = 36
        self.padding = 28
        self.stone_r = 14
        self.board_px = self.padding * 2 + self.cell * (self.board_size - 1)

        self.vs_ai = True
        self.human_player = 1  # black
        self.ai_player = 2  # white

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False
        self.ai_thinking = False
        self.history = []

        self.status_var = tk.StringVar(value="Black to move")

        self.build_ui()
        self.draw_board()

    def build_ui(self):
        container = tk.Frame(self.root, padx=10, pady=10)
        container.pack()

        top = tk.Frame(container)
        top.pack(fill="x")

        tk.Label(top, text="Gomoku", font=("Consolas", 14, "bold")).pack(side="left")
        tk.Label(top, textvariable=self.status_var, font=("Consolas", 10), fg="#1f4e79").pack(side="left", padx=12)

        self.mode_button = tk.Button(top, text="Mode: Human vs AI", width=16, command=self.toggle_mode)
        self.mode_button.pack(side="right", padx=4)
        tk.Button(top, text="Undo", width=8, command=self.undo).pack(side="right", padx=4)
        tk.Button(top, text="Reset", width=8, command=self.reset_game).pack(side="right", padx=4)

        self.canvas = tk.Canvas(
            container,
            width=self.board_px,
            height=self.board_px,
            bg="#d8a45d",
            highlightthickness=1,
            highlightbackground="#7f5b2a",
        )
        self.canvas.pack(pady=(10, 0))
        self.canvas.bind("<Button-1>", self.on_click)

    def toggle_mode(self):
        self.vs_ai = not self.vs_ai
        mode_text = "Mode: Human vs AI" if self.vs_ai else "Mode: Human vs Human"
        self.mode_button.config(text=mode_text)
        self.reset_game()

    def draw_board(self):
        self.canvas.delete("all")

        for i in range(self.board_size):
            x0 = self.padding
            y = self.padding + i * self.cell
            x1 = self.padding + self.cell * (self.board_size - 1)
            self.canvas.create_line(x0, y, x1, y, fill="#5e3e1f", width=1)

            x = self.padding + i * self.cell
            y0 = self.padding
            y1 = self.padding + self.cell * (self.board_size - 1)
            self.canvas.create_line(x, y0, x, y1, fill="#5e3e1f", width=1)

        stars = [(3, 3), (3, 7), (3, 11), (7, 3), (7, 7), (7, 11), (11, 3), (11, 7), (11, 11)]
        for r, c in stars:
            cx, cy = self.board_to_pixel(r, c)
            self.canvas.create_oval(cx - 3, cy - 3, cx + 3, cy + 3, fill="#4a2f14", outline="")

        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c] != 0:
                    self.draw_stone(r, c, self.board[r][c])

    def board_to_pixel(self, row, col):
        x = self.padding + col * self.cell
        y = self.padding + row * self.cell
        return x, y

    def pixel_to_board(self, x, y):
        col = round((x - self.padding) / self.cell)
        row = round((y - self.padding) / self.cell)
        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            px, py = self.board_to_pixel(row, col)
            if abs(px - x) <= self.cell * 0.45 and abs(py - y) <= self.cell * 0.45:
                return row, col
        return None

    def draw_stone(self, row, col, player):
        x, y = self.board_to_pixel(row, col)
        if player == 1:
            fill = "#101010"
            outline = "#222222"
        else:
            fill = "#f2f2f2"
            outline = "#bbbbbb"
        self.canvas.create_oval(
            x - self.stone_r,
            y - self.stone_r,
            x + self.stone_r,
            y + self.stone_r,
            fill=fill,
            outline=outline,
            width=1.5,
        )

    def on_click(self, event):
        if self.game_over or self.ai_thinking:
            return

        if self.vs_ai and self.current_player != self.human_player:
            return

        pos = self.pixel_to_board(event.x, event.y)
        if pos is None:
            return

        row, col = pos
        if self.board[row][col] != 0:
            return

        self.place_stone(row, col)

        if self.vs_ai and not self.game_over and self.current_player == self.ai_player:
            self.ai_thinking = True
            self.status_var.set("AI is thinking...")
            self.root.after(150, self.ai_move)

    def place_stone(self, row, col):
        player = self.current_player
        self.board[row][col] = player
        self.history.append((row, col, player))
        self.draw_stone(row, col, player)

        if self.is_winner(row, col, player):
            self.game_over = True
            winner = "Black" if player == 1 else "White"
            self.status_var.set(f"{winner} wins")
            messagebox.showinfo("Game Over", f"{winner} wins!")
            return

        if len(self.history) == self.board_size * self.board_size:
            self.game_over = True
            self.status_var.set("Draw")
            messagebox.showinfo("Game Over", "Draw")
            return

        self.current_player = 2 if self.current_player == 1 else 1
        self.update_turn_text()

    def update_turn_text(self):
        if self.vs_ai:
            if self.current_player == self.human_player:
                self.status_var.set("Your turn (Black)")
            else:
                self.status_var.set("AI turn (White)")
        else:
            self.status_var.set("Black to move" if self.current_player == 1 else "White to move")

    def ai_move(self):
        if self.game_over:
            self.ai_thinking = False
            return

        move = self.find_best_move(self.ai_player)
        if move is not None:
            self.place_stone(move[0], move[1])
        self.ai_thinking = False

    def find_best_move(self, player):
        candidates = self.get_candidate_moves()
        if not candidates:
            center = self.board_size // 2
            return center, center

        enemy = 1 if player == 2 else 2
        best_score = -1
        best_move = None

        for row, col in candidates:
            attack = self.score_point(row, col, player)
            defense = self.score_point(row, col, enemy)
            # Prefer attack, but boost strong defensive responses.
            score = attack * 10 + defense * 8
            if score > best_score:
                best_score = score
                best_move = (row, col)

        return best_move

    def get_candidate_moves(self):
        if not self.history:
            center = self.board_size // 2
            return [(center, center)]

        candidates = set()
        for row, col, _player in self.history:
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    r = row + dr
                    c = col + dc
                    if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == 0:
                        candidates.add((r, c))
        return list(candidates)

    def score_point(self, row, col, player):
        scores = []
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            left_count, left_open = self.count_line(row, col, -dr, -dc, player)
            right_count, right_open = self.count_line(row, col, dr, dc, player)
            total = left_count + right_count + 1
            open_ends = int(left_open) + int(right_open)
            scores.append(self.pattern_score(total, open_ends))
        return max(scores)

    def count_line(self, row, col, dr, dc, player):
        cnt = 0
        r = row + dr
        c = col + dc
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
            cnt += 1
            r += dr
            c += dc
        open_end = 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == 0
        return cnt, open_end

    def pattern_score(self, total, open_ends):
        if total >= 5:
            return 100000
        if total == 4:
            if open_ends == 2:
                return 20000
            if open_ends == 1:
                return 4000
        if total == 3:
            if open_ends == 2:
                return 1800
            if open_ends == 1:
                return 300
        if total == 2:
            if open_ends == 2:
                return 120
            if open_ends == 1:
                return 30
        if total == 1 and open_ends == 2:
            return 8
        return 1

    def is_winner(self, row, col, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.count_one_side(row, col, dr, dc, player)
            count += self.count_one_side(row, col, -dr, -dc, player)
            if count >= 5:
                return True
        return False

    def count_one_side(self, row, col, dr, dc, player):
        cnt = 0
        r, c = row + dr, col + dc
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
            cnt += 1
            r += dr
            c += dc
        return cnt

    def undo(self):
        if not self.history:
            return

        self.game_over = False
        steps = 2 if self.vs_ai else 1
        removed = 0
        while self.history and removed < steps:
            row, col, player = self.history.pop()
            self.board[row][col] = 0
            self.current_player = player
            removed += 1

        self.ai_thinking = False
        self.draw_board()
        self.update_turn_text()

    def reset_game(self):
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.history = []
        self.current_player = 1
        self.game_over = False
        self.ai_thinking = False
        self.draw_board()
        self.update_turn_text()


def run():
    root = tk.Tk()
    GomokuGame(root)
    root.mainloop()


if __name__ == "__main__":
    run()
