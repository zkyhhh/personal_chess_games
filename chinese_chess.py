from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple
import tkinter as tk
from tkinter import messagebox

Board = List[List[str]]
Move = Tuple[int, int, int, int]


PIECE_VALUE = {
    "k": 10000,
    "r": 500,
    "n": 270,
    "b": 120,
    "a": 120,
    "c": 250,
    "p": 70,
}


def initial_board() -> Board:
    return [
        list("rnbakabnr"),
        list("........."),
        list(".c.....c."),
        list("p.p.p.p.p"),
        list("........."),
        list("........."),
        list("P.P.P.P.P"),
        list(".C.....C."),
        list("........."),
        list("RNBAKABNR"),
    ]


def clone_board(board: Board) -> Board:
    return [row[:] for row in board]


def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < 10 and 0 <= c < 9


def is_red(piece: str) -> bool:
    return piece.isupper()


def side_of(piece: str) -> Optional[str]:
    if piece == ".":
        return None
    return "red" if is_red(piece) else "black"


def enemy(side: str) -> str:
    return "black" if side == "red" else "red"


def in_palace(side: str, r: int, c: int) -> bool:
    if c < 3 or c > 5:
        return False
    if side == "red":
        return 7 <= r <= 9
    return 0 <= r <= 2


def crossed_river(side: str, r: int) -> bool:
    return r <= 4 if side == "red" else r >= 5


def find_king(board: Board, side: str) -> Optional[Tuple[int, int]]:
    target = "K" if side == "red" else "k"
    for r in range(10):
        for c in range(9):
            if board[r][c] == target:
                return r, c
    return None


def kings_face_each_other(board: Board) -> bool:
    rk = find_king(board, "red")
    bk = find_king(board, "black")
    if not rk or not bk:
        return False
    rr, rc = rk
    br, bc = bk
    if rc != bc:
        return False
    lo, hi = sorted((rr, br))
    for r in range(lo + 1, hi):
        if board[r][rc] != ".":
            return False
    return True


def generate_pseudo_moves(board: Board, r: int, c: int) -> List[Move]:
    piece = board[r][c]
    if piece == ".":
        return []
    side = side_of(piece)
    assert side is not None
    p = piece.lower()
    moves: List[Move] = []

    def add_if_enemy_or_empty(nr: int, nc: int) -> None:
        if not in_bounds(nr, nc):
            return
        tgt = board[nr][nc]
        if tgt == "." or side_of(tgt) != side:
            moves.append((r, c, nr, nc))

    if p == "r":
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            while in_bounds(nr, nc):
                tgt = board[nr][nc]
                if tgt == ".":
                    moves.append((r, c, nr, nc))
                else:
                    if side_of(tgt) != side:
                        moves.append((r, c, nr, nc))
                    break
                nr += dr
                nc += dc

    elif p == "n":
        knight_steps = [
            (-2, -1, -1, 0),
            (-2, 1, -1, 0),
            (2, -1, 1, 0),
            (2, 1, 1, 0),
            (-1, -2, 0, -1),
            (1, -2, 0, -1),
            (-1, 2, 0, 1),
            (1, 2, 0, 1),
        ]
        for dr, dc, lr, lc in knight_steps:
            leg_r, leg_c = r + lr, c + lc
            nr, nc = r + dr, c + dc
            if in_bounds(leg_r, leg_c) and board[leg_r][leg_c] == ".":
                add_if_enemy_or_empty(nr, nc)

    elif p == "b":
        for dr, dc in ((2, 2), (2, -2), (-2, 2), (-2, -2)):
            eye_r, eye_c = r + dr // 2, c + dc // 2
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc):
                continue
            if board[eye_r][eye_c] != ".":
                continue
            if side == "red" and nr < 5:
                continue
            if side == "black" and nr > 4:
                continue
            add_if_enemy_or_empty(nr, nc)

    elif p == "a":
        for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and in_palace(side, nr, nc):
                add_if_enemy_or_empty(nr, nc)

    elif p == "k":
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and in_palace(side, nr, nc):
                add_if_enemy_or_empty(nr, nc)

        other = find_king(board, enemy(side))
        if other is not None and other[1] == c:
            lo, hi = sorted((r, other[0]))
            clear = True
            for rr in range(lo + 1, hi):
                if board[rr][c] != ".":
                    clear = False
                    break
            if clear:
                moves.append((r, c, other[0], c))

    elif p == "c":
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            while in_bounds(nr, nc) and board[nr][nc] == ".":
                moves.append((r, c, nr, nc))
                nr += dr
                nc += dc

            nr += dr
            nc += dc
            while in_bounds(nr, nc):
                tgt = board[nr][nc]
                if tgt != ".":
                    if side_of(tgt) != side:
                        moves.append((r, c, nr, nc))
                    break
                nr += dr
                nc += dc

    elif p == "p":
        if side == "red":
            forward = [(-1, 0)]
            if crossed_river(side, r):
                forward.extend([(0, -1), (0, 1)])
        else:
            forward = [(1, 0)]
            if crossed_river(side, r):
                forward.extend([(0, -1), (0, 1)])
        for dr, dc in forward:
            nr, nc = r + dr, c + dc
            add_if_enemy_or_empty(nr, nc)

    return moves


def make_move(board: Board, mv: Move) -> Board:
    fr, fc, tr, tc = mv
    nb = clone_board(board)
    nb[tr][tc] = nb[fr][fc]
    nb[fr][fc] = "."
    return nb


def is_in_check(board: Board, side: str) -> bool:
    kpos = find_king(board, side)
    if kpos is None:
        return True
    kr, kc = kpos

    if kings_face_each_other(board):
        return True

    opp = enemy(side)
    for r in range(10):
        for c in range(9):
            pc = board[r][c]
            if pc == "." or side_of(pc) != opp:
                continue
            for _, _, tr, tc in generate_pseudo_moves(board, r, c):
                if tr == kr and tc == kc:
                    return True
    return False


def legal_moves(board: Board, side: str) -> List[Move]:
    all_moves: List[Move] = []
    for r in range(10):
        for c in range(9):
            pc = board[r][c]
            if pc == "." or side_of(pc) != side:
                continue
            for mv in generate_pseudo_moves(board, r, c):
                nb = make_move(board, mv)
                if not is_in_check(nb, side):
                    all_moves.append(mv)
    return all_moves


def evaluate(board: Board) -> int:
    total = 0
    for r in range(10):
        for c in range(9):
            p = board[r][c]
            if p == ".":
                continue
            val = PIECE_VALUE[p.lower()]
            side = side_of(p)
            if p.lower() == "p" and side is not None and crossed_river(side, r):
                val += 30
            if side == "red":
                total += val
            else:
                total -= val
    return total


@dataclass
class XiangqiAI:
    depth: int = 3

    def choose_move(self, board: Board, side: str) -> Optional[Move]:
        moves = legal_moves(board, side)
        if not moves:
            return None

        best_mv: Optional[Move] = None
        alpha, beta = -math.inf, math.inf
        best_score = -math.inf

        for mv in moves:
            nb = make_move(board, mv)
            score = -self._negamax(nb, self.depth - 1, -beta, -alpha, enemy(side))
            if score > best_score:
                best_score = score
                best_mv = mv
            if score > alpha:
                alpha = score
        return best_mv

    def _negamax(self, board: Board, depth: int, alpha: float, beta: float, side: str) -> float:
        if find_king(board, "red") is None:
            return -100000 if side == "red" else 100000
        if find_king(board, "black") is None:
            return -100000 if side == "black" else 100000

        moves = legal_moves(board, side)
        if not moves:
            if is_in_check(board, side):
                return -99999
            return 0

        if depth == 0:
            score = evaluate(board)
            return score if side == "red" else -score

        value = -math.inf
        for mv in moves:
            nb = make_move(board, mv)
            score = -self._negamax(nb, depth - 1, -beta, -alpha, enemy(side))
            if score > value:
                value = score
            if value > alpha:
                alpha = value
            if alpha >= beta:
                break
        return value


def print_board(board: Board) -> None:
    print("    0 1 2 3 4 5 6 7 8")
    print("   -------------------")
    for r in range(10):
        row = " ".join(board[r])
        print(f"{r:2d}| {row}")
    print()


def parse_move(text: str) -> Optional[Move]:
    parts = text.strip().split()
    if len(parts) != 4:
        return None
    try:
        fr, fc, tr, tc = map(int, parts)
    except ValueError:
        return None
    if not (in_bounds(fr, fc) and in_bounds(tr, tc)):
        return None
    return fr, fc, tr, tc


def move_to_text(mv: Move) -> str:
    fr, fc, tr, tc = mv
    return f"({fr},{fc}) -> ({tr},{tc})"


def run_cli() -> None:
    board = initial_board()
    ai = XiangqiAI(depth=3)

    print("Xiangqi AI")
    print("Pieces: Uppercase=Red, lowercase=Black")
    print("Input move: from_row from_col to_row to_col")
    print("Example: 9 0 8 0")

    human_side = "red"
    side_input = input("Choose your side [red/black], default red: ").strip().lower()
    if side_input in {"red", "black"}:
        human_side = side_input
    ai_side = enemy(human_side)
    turn = "red"

    while True:
        print_board(board)

        if find_king(board, "red") is None:
            print("Black wins")
            break
        if find_king(board, "black") is None:
            print("Red wins")
            break

        moves = legal_moves(board, turn)
        if not moves:
            if is_in_check(board, turn):
                print(f"{enemy(turn).capitalize()} wins by checkmate")
            else:
                print("Draw")
            break

        if turn == human_side:
            text = input("Your move (or 'q'): ").strip().lower()
            if text == "q":
                print("Game ended")
                break
            mv = parse_move(text)
            if mv is None or mv not in moves:
                print("Illegal move, try again")
                continue
            board = make_move(board, mv)
            if is_in_check(board, ai_side):
                print("Check")
        else:
            print("AI thinking...")
            mv = ai.choose_move(board, ai_side)
            if mv is None:
                print("You win")
                break
            print(f"AI move: {move_to_text(mv)}")
            board = make_move(board, mv)
            if is_in_check(board, human_side):
                print("Your king is in check")

        turn = enemy(turn)


class XiangqiGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Xiangqi AI")
        self.root.resizable(False, False)

        self.cell = 60
        self.margin = 40
        self.board_w = self.margin * 2 + self.cell * 8
        self.board_h = self.margin * 2 + self.cell * 9
        self.pick_radius = 22

        self.ai = XiangqiAI(depth=3)
        self.board = initial_board()
        self.human_side = "red"
        self.ai_side = "black"
        self.turn = "red"
        self.game_over = False
        self.selected: Optional[Tuple[int, int]] = None

        self.status = tk.StringVar(value="Choose side and start game")
        self._build_ui()
        self._redraw()

    def _build_ui(self) -> None:
        wrap = tk.Frame(self.root, padx=10, pady=10)
        wrap.pack()

        tk.Label(wrap, text="Xiangqi", font=("Consolas", 16, "bold")).pack()
        tk.Label(wrap, textvariable=self.status, fg="#1f4e79", font=("Consolas", 11)).pack(pady=(3, 8))

        self.canvas = tk.Canvas(
            wrap,
            width=self.board_w,
            height=self.board_h,
            bg="#f2d6a2",
            highlightthickness=1,
            highlightbackground="#7a5230",
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self._on_click)

        ctl = tk.Frame(wrap)
        ctl.pack(pady=(8, 0))
        tk.Button(ctl, text="Human First", width=12, command=lambda: self.start("red")).grid(row=0, column=0, padx=4)
        tk.Button(ctl, text="AI First", width=12, command=lambda: self.start("black")).grid(row=0, column=1, padx=4)
        tk.Button(ctl, text="Reset", width=12, command=self.reset).grid(row=0, column=2, padx=4)

    def start(self, human_side: str) -> None:
        self.board = initial_board()
        self.human_side = human_side
        self.ai_side = enemy(human_side)
        self.turn = "red"
        self.game_over = False
        self.selected = None
        self._redraw()

        if self.turn == self.human_side:
            self.status.set("Your turn")
        else:
            self.status.set("AI thinking...")
            self.root.after(120, self._ai_move)

    def reset(self) -> None:
        self.board = initial_board()
        self.game_over = False
        self.selected = None
        self.status.set("Choose side and start game")
        self._redraw()

    def _on_click(self, event: tk.Event) -> None:
        if self.game_over or self.turn != self.human_side:
            return
        pos = self._pixel_to_pos(event.x, event.y)
        if pos is None:
            return
        r, c = pos
        p = self.board[r][c]

        if self.selected is None:
            if p != "." and side_of(p) == self.human_side:
                self.selected = (r, c)
                self._redraw()
            return

        sr, sc = self.selected
        if (r, c) == (sr, sc):
            self.selected = None
            self._redraw()
            return

        if p != "." and side_of(p) == self.human_side:
            self.selected = (r, c)
            self._redraw()
            return

        mv = (sr, sc, r, c)
        legal = legal_moves(self.board, self.human_side)
        if mv not in legal:
            self.status.set("Illegal move")
            return

        self.board = make_move(self.board, mv)
        self.selected = None
        self.turn = self.ai_side
        self._redraw()
        if self._finish_if_needed():
            return

        if is_in_check(self.board, self.ai_side):
            self.status.set("Check, AI thinking...")
        else:
            self.status.set("AI thinking...")
        self.root.after(120, self._ai_move)

    def _ai_move(self) -> None:
        if self.game_over or self.turn != self.ai_side:
            return

        mv = self.ai.choose_move(self.board, self.ai_side)
        if mv is None:
            self.game_over = True
            self.status.set("You win")
            messagebox.showinfo("Result", "You win")
            return

        self.board = make_move(self.board, mv)
        self.turn = self.human_side
        self._redraw()
        if self._finish_if_needed():
            return

        if is_in_check(self.board, self.human_side):
            self.status.set("Your king is in check")
        else:
            self.status.set("Your turn")

    def _finish_if_needed(self) -> bool:
        if find_king(self.board, "red") is None:
            self.game_over = True
            self.status.set("Black wins")
            messagebox.showinfo("Result", "Black wins")
            return True
        if find_king(self.board, "black") is None:
            self.game_over = True
            self.status.set("Red wins")
            messagebox.showinfo("Result", "Red wins")
            return True

        moves = legal_moves(self.board, self.turn)
        if not moves:
            self.game_over = True
            if is_in_check(self.board, self.turn):
                winner = enemy(self.turn).capitalize()
                self.status.set(f"{winner} wins by checkmate")
                messagebox.showinfo("Result", f"{winner} wins by checkmate")
            else:
                self.status.set("Draw")
                messagebox.showinfo("Result", "Draw")
            return True
        return False

    def _pixel_to_pos(self, x: int, y: int) -> Optional[Tuple[int, int]]:
        c = round((x - self.margin) / self.cell)
        r = round((y - self.margin) / self.cell)
        if not in_bounds(r, c):
            return None
        px = self.margin + c * self.cell
        py = self.margin + r * self.cell
        if abs(px - x) > self.pick_radius or abs(py - y) > self.pick_radius:
            return None
        return r, c

    def _redraw(self) -> None:
        self.canvas.delete("all")
        self._draw_board_grid()
        self._draw_pieces()
        self._draw_selection()

    def _draw_board_grid(self) -> None:
        m = self.margin
        s = self.cell
        left, right = m, m + 8 * s
        top, bottom = m, m + 9 * s
        river_top = m + 4 * s
        river_bottom = m + 5 * s

        for r in range(10):
            y = m + r * s
            self.canvas.create_line(left, y, right, y, fill="#6b4a2b", width=2)

        for c in range(9):
            x = m + c * s
            if c == 0 or c == 8:
                self.canvas.create_line(x, top, x, bottom, fill="#6b4a2b", width=2)
            else:
                self.canvas.create_line(x, top, x, river_top, fill="#6b4a2b", width=2)
                self.canvas.create_line(x, river_bottom, x, bottom, fill="#6b4a2b", width=2)

        self.canvas.create_text((left + right) / 2, (river_top + river_bottom) / 2, text="CHU RIVER / HAN BORDER", fill="#7a5230", font=("Consolas", 10, "bold"))

        self.canvas.create_line(m + 3 * s, m, m + 5 * s, m + 2 * s, fill="#6b4a2b", width=2)
        self.canvas.create_line(m + 5 * s, m, m + 3 * s, m + 2 * s, fill="#6b4a2b", width=2)
        self.canvas.create_line(m + 3 * s, m + 7 * s, m + 5 * s, m + 9 * s, fill="#6b4a2b", width=2)
        self.canvas.create_line(m + 5 * s, m + 7 * s, m + 3 * s, m + 9 * s, fill="#6b4a2b", width=2)

    def _draw_pieces(self) -> None:
        symbol = {
            "K": "帅", "A": "仕", "B": "相", "N": "马", "R": "车", "C": "炮", "P": "兵",
            "k": "将", "a": "士", "b": "象", "n": "马", "r": "车", "c": "炮", "p": "卒",
        }
        m, s = self.margin, self.cell
        radius = 22
        for r in range(10):
            for c in range(9):
                p = self.board[r][c]
                if p == ".":
                    continue
                x = m + c * s
                y = m + r * s
                fg = "#b22222" if is_red(p) else "#1d3557"
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="#fef6e4", outline=fg, width=2)
                self.canvas.create_text(x, y, text=symbol[p], fill=fg, font=("Microsoft YaHei", 16, "bold"))

    def _draw_selection(self) -> None:
        if self.selected is None:
            return
        r, c = self.selected
        x = self.margin + c * self.cell
        y = self.margin + r * self.cell
        d = 28
        self.canvas.create_rectangle(x - d, y - d, x + d, y + d, outline="#2a9d8f", width=3)


def run() -> None:
    root = tk.Tk()
    XiangqiGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()