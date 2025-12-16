#!/usr/bin/env python3
"""
Unbeatable Tic-Tac-Toe using Minimax with Alpha-Beta pruning.
Save as tictactoe_ai.py and run: python3 tictactoe_ai.py
"""

import math
import random
from typing import List, Optional, Tuple

# Board positions are indices 0..8 laid out as:
#  0 | 1 | 2
# ---+---+---
#  3 | 4 | 5
# ---+---+---
#  6 | 7 | 8

WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


class Board:
    def __init__(self):
        self.cells: List[str] = [' '] * 9

    def make_move(self, idx: int, player: str) -> bool:
        """Place player 'X' or 'O' at idx if free. Return True if placed."""
        if 0 <= idx < 9 and self.cells[idx] == ' ':
            self.cells[idx] = player
            return True
        return False

    def available_moves(self) -> List[int]:
        return [i for i, v in enumerate(self.cells) if v == ' ']

    def is_full(self) -> bool:
        return ' ' not in self.cells

    def check_winner(self) -> Optional[str]:
        """Return 'X' or 'O' if that player has won, else None."""
        for a, b, c in WIN_COMBINATIONS:
            if self.cells[a] == self.cells[b] == self.cells[c] != ' ':
                return self.cells[a]
        return None

    def clone(self) -> 'Board':
        b = Board()
        b.cells = self.cells.copy()
        return b

    def __str__(self) -> str:
        s = ""
        for row in range(3):
            s += " {} | {} | {} \n".format(
                self.cells[row * 3], self.cells[row * 3 + 1], self.cells[row * 3 + 2]
            )
            if row < 2:
                s += "---+---+---\n"
        return s


def score_for_winner(winner: Optional[str], ai_player: str) -> int:
    """Return numeric score from AI perspective."""
    if winner is None:
        return 0
    return 1 if winner == ai_player else -1


def minimax(board: Board, depth: int, maximizing: bool, ai_player: str, human_player: str,
            alpha: int, beta: int) -> Tuple[int, Optional[int]]:
    """
    Minimax with alpha-beta.
    Returns (score, best_move_index)
    """
    winner = board.check_winner()
    if winner is not None:
        return score_for_winner(winner, ai_player), None
    if board.is_full():
        return 0, None

    best_move: Optional[int] = None

    if maximizing:
        max_eval = -math.inf
        for move in board.available_moves():
            new_board = board.clone()
            new_board.make_move(move, ai_player)
            eval_score, _ = minimax(new_board, depth + 1, False, ai_player, human_player, alpha, beta)
            # prefer quicker wins: tie-break by smaller depth (not necessary but good)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # beta cut-off
        return int(max_eval), best_move
    else:
        min_eval = math.inf
        for move in board.available_moves():
            new_board = board.clone()
            new_board.make_move(move, human_player)
            eval_score, _ = minimax(new_board, depth + 1, True, ai_player, human_player, alpha, beta)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # alpha cut-off
        return int(min_eval), best_move


def best_move_for_ai(board: Board, ai_player: str, human_player: str) -> int:
    """Return index of best move for AI. If board is empty, choose center or a corner."""
    # Quick heuristic: if board empty, take center for best play
    if board.available_moves() == list(range(9)):
        return 4  # center

    score, move = minimax(board, depth=0, maximizing=True, ai_player=ai_player,
                          human_player=human_player, alpha=-math.inf, beta=math.inf)
    if move is None:
        # fallback: random available
        return random.choice(board.available_moves())
    return move


def input_move_from_user(board: Board) -> int:
    """Ask the user for a move index (1..9)."""
    while True:
        try:
            user_in = input("Enter your move (1-9), or 'q' to quit: ").strip()
            if user_in.lower() == 'q':
                print("Quitting. Bye!")
                exit(0)
            idx = int(user_in) - 1
            if idx not in range(9):
                print("Please enter a number from 1 to 9.")
                continue
            if board.cells[idx] != ' ':
                print("That cell is already taken. Choose another.")
                continue
            return idx
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")


def choose_symbol() -> Tuple[str, str]:
    """Let human choose X or O. X goes first."""
    while True:
        c = input("Choose your symbol ('X' or 'O') [X goes first]: ").strip().upper()
        if c in ('X', 'O'):
            human = c
            ai = 'O' if human == 'X' else 'X'
            return human, ai
        print("Please enter 'X' or 'O'.")


def main():
    print("Tic-Tac-Toe (Unbeatable AI). Board positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()

    human_player, ai_player = choose_symbol()
    current_player = 'X'  # X always moves first
    board = Board()

    while True:
        print(board)
        winner = board.check_winner()
        if winner is not None:
            print(f"Player {winner} wins!")
            break
        if board.is_full():
            print("It's a draw!")
            break

        if current_player == human_player:
            print("Your turn.")
            move = input_move_from_user(board)
            board.make_move(move, human_player)
        else:
            print("AI is thinking...")
            move = best_move_for_ai(board, ai_player, human_player)
            board.make_move(move, ai_player)
            print(f"AI placed {ai_player} at position {move + 1}.")

        # swap
        current_player = 'O' if current_player == 'X' else 'X'

    print(board)
    print("Game over.")


if __name__ == "__main__":
    main()
