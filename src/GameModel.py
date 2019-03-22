import random


class Model:
    """Class responsible for storing the game state."""

    def __init__(self, num_players, player_list):
        """Initialize an empty game board with given rows and columns."""

        self.board = []

        for row in range(19):
            self.board.append([])
            for column in range(19):
                # Set every cell to value 0 to represent an empty tile
                self.board[row].append(0)

        self.num_players = num_players
        self.player_list = player_list

    def get_board(self):
        """Return the current board state."""
        return self.board

    def get_num_players(self):
        """Return the number of players in the game."""
        return self.num_players

    def get_player_list(self):
        """Return the dictionary of players and their colors in the game."""
        return self.player_list

    def is_claimed(self, player, row, column):
        """Check if a given tile is claimed by the given player."""

        if self.board[row][column] == player:
            return True
        else:
            return False

    def randomize(self):
        """Generate a random spot on the grid and check if
            its available"""
        first = random.randint(0, 18)
        second = random.randint(0, 18)
        while True:
            if self.board[first][second] == 0:
                return [first, second]
            else:
                first = random.randint(0, 18)
                second = random.randint(0, 18)

    def is_won(self, player, row, column):
        """Check if a given player has won the game."""

        # Check horizontal

        # Check left
        left = 0
        for i in range(1, 5):
            if (0 <= column - i <= 18):
                if self.is_claimed(player, row, column - i):
                    left += 1
                else:
                    break

                    # Check right
        right = 0
        for i in range(1, 5):
            if (0 <= column + i < 18):
                if self.is_claimed(player, row, column + i):
                    right += 1
                else:
                    break

                    # Check if horizontal win
        if ((left + right + 1) >= 5):
            return True

            # Check vertical

        # Check top
        top = 0
        for i in range(1, 5):
            if (0 <= row - i <= 18):
                if self.is_claimed(player, row - i, column):
                    top += 1
                else:
                    break

                    # Check bottom
        bottom = 0
        for i in range(1, 5):
            if (0 <= row + i <= 18):
                if self.is_claimed(player, row + i, column):
                    bottom += 1
                else:
                    break

        # Check if vertical win
        if ((top + bottom + 1) >= 5):
            return True

            # Check diagonal (1)

        # Check top left
        topleft = 0
        for i in range(1, 5):
            if (0 <= row - i <= 18) and (0 <= column - i <= 18):
                if self.is_claimed(player, row - i, column - i):
                    topleft += 1
                else:
                    break

                    # Check bottom right
        bottomright = 0
        for i in range(1, 5):
            if (0 <= row + i <= 18) and (0 <= column + i <= 18):
                if self.is_claimed(player, row + i, column + i):
                    bottomright += 1
                else:
                    break

                    # Check if won
        if ((topleft + bottomright + 1) >= 5):
            return True

            # Check diagonal (2)

        # Check top right
        topright = 0
        for i in range(1, 5):
            if (0 <= row + i <= 18) and (0 <= column + i <= 18):
                if self.is_claimed(player, row - i, column + i):
                    topright += 1
                else:
                    break

                    # Check bottom left
        bottomleft = 0
        for i in range(1, 5):
            if (0 <= row + i <= 18) and (0 <= column + i <= 18):
                if self.is_claimed(player, row + i, column - i):
                    bottomleft += 1
                else:
                    break

                    # Check if won
        if ((topright + bottomleft + 1) >= 5):
            return True

        return False
