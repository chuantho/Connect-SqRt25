class Rounds:
    """
    Creates a version of the game with rounds.

    Args:
        view (BoardView): the board view that is created in the main method
        num_of_rounds (int): the number of rounds to play
    """
    def __init__(self, view, num_of_rounds):
        self.view = view
        self.num_of_rounds = num_of_rounds

        # Starts running the game with the number of rounds specified
        self.run_rounds();

    def get_round_finished(self):
        """Return the boolean value of the is_won function."""
        return view.model.is_won()

    def run_rounds(self):
        """Runs the game the number of times specified."""
        count = 0

        while count < self.num_of_rounds:
            if self.get_round_finished():
                self.view.model = BoardModel(19, 19)
                self.view.update()
                count = count + 1

