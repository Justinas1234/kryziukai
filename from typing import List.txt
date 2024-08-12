from typing import List

class Board:
    def __init__(self):
        self.board: List[str] = [str(i) for i in range(1, 10)]

    def display(self) -> None:
        """Displays the current state of the board."""
        print()
        for row in range(3):
            print("|", self.board[row * 3], "|", self.board[row * 3 + 1], "|", self.board[row * 3 + 2], "|")
            if row < 2:
                print("|---|---|---|")

    def update(self, position: int, marker: str) -> None:
        """Updates the board with a player's marker at a given position."""
        self.board[position - 1] = marker

    def available_moves(self) -> List[int]:
        """Returns a list of available moves."""
        return [i for i in range(1, 10) if self.board[i - 1].isdigit()]

    def is_winner(self, marker: str) -> bool:
        """Checks if a marker has won the game."""
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        return any(all(self.board[pos] == marker for pos in combo) for combo in win_combinations)

    def is_full(self) -> bool:
        """Checks if the board is full."""
        return all(not spot.isdigit() for spot in self.board)
