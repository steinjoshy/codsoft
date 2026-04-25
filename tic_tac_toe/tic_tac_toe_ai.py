"""Unbeatable Tic-Tac-Toe AI using Minimax with alpha-beta pruning.

Run:
    python tic_tac_toe/tic_tac_toe_ai.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple


HUMAN = "X"
AI = "O"
EMPTY = " "


WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


@dataclass
class Game:
    board: List[str]

    @classmethod
    def new(cls) -> "Game":
        return cls(board=[EMPTY] * 9)

    def available_moves(self) -> Iterable[int]:
        return (i for i, cell in enumerate(self.board) if cell == EMPTY)

    def place(self, pos: int, player: str) -> bool:
        if pos < 0 or pos > 8 or self.board[pos] != EMPTY:
            return False
        self.board[pos] = player
        return True

    def winner(self) -> Optional[str]:
        for a, b, c in WIN_LINES:
            if self.board[a] != EMPTY and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_draw(self) -> bool:
        return self.winner() is None and all(cell != EMPTY for cell in self.board)

    def is_terminal(self) -> bool:
        return self.winner() is not None or self.is_draw()

    def render(self) -> str:
        cells = [self.board[i] if self.board[i] != EMPTY else str(i + 1) for i in range(9)]
        return (
            f"\n {cells[0]} | {cells[1]} | {cells[2]}\n"
            "---+---+---\n"
            f" {cells[3]} | {cells[4]} | {cells[5]}\n"
            "---+---+---\n"
            f" {cells[6]} | {cells[7]} | {cells[8]}\n"
        )


def minimax(game: Game, maximizing: bool, alpha: int, beta: int, depth: int = 0) -> int:
    winner = game.winner()
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if game.is_draw():
        return 0

    if maximizing:
        best_score = -10_000
        for move in game.available_moves():
            game.board[move] = AI
            score = minimax(game, maximizing=False, alpha=alpha, beta=beta, depth=depth + 1)
            game.board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score

    best_score = 10_000
    for move in game.available_moves():
        game.board[move] = HUMAN
        score = minimax(game, maximizing=True, alpha=alpha, beta=beta, depth=depth + 1)
        game.board[move] = EMPTY
        best_score = min(best_score, score)
        beta = min(beta, best_score)
        if beta <= alpha:
            break
    return best_score


def best_ai_move(game: Game) -> int:
    best_score = -10_000
    chosen_move = -1

    for move in game.available_moves():
        game.board[move] = AI
        score = minimax(game, maximizing=False, alpha=-10_000, beta=10_000, depth=0)
        game.board[move] = EMPTY

        if score > best_score:
            best_score = score
            chosen_move = move

    return chosen_move


def read_human_move(game: Game) -> int:
    while True:
        raw = input("Choose your move (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        pos = int(raw) - 1
        if pos not in range(9):
            print("Move must be between 1 and 9.")
            continue

        if game.board[pos] != EMPTY:
            print("That spot is already taken. Try a different move.")
            continue

        return pos


def main() -> None:
    print("Tic-Tac-Toe: You are X, AI is O.")
    print("Board positions are numbered 1 through 9.")

    game = Game.new()

    while not game.is_terminal():
        print(game.render())
        human_move = read_human_move(game)
        game.place(human_move, HUMAN)

        if game.is_terminal():
            break

        ai_move = best_ai_move(game)
        game.place(ai_move, AI)
        print(f"AI chooses position {ai_move + 1}.")

    print(game.render())
    winner = game.winner()
    if winner == HUMAN:
        print("You win! (This should be very hard.)")
    elif winner == AI:
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw! Perfect play from both sides.")


if __name__ == "__main__":
    main()
