import pygame
import time
from ObserverPattern import Observable, Observer


# Define some base colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# M of MVC
class BoardModel(Observable):
    """Class responsible for storing the game state"""


    def __init__(self, num_rows, num_columns):
        """Initialize an empty game board with given rows and columns"""
        Observable.__init__(self)
        self.rows = num_rows
        self.columns = num_columns
        self.board = []

        for row in range(num_rows):
            self.board.append([])
            for column in range(num_columns):
                # Set every cell to value 0 to represent an empty tile
                self.board[row].append(0)


    def get_board(self):
        """Return the current board state"""
        return self.board


    def get_rows(self):
        """Return the number of rows of the game board"""
        return self.rows


    def is_won(self):
        """Return True iff a player wins the game"""
        pass

    def get_columns(self):
        """Return the number of columns of the game board"""
        return self.columns

# V of MVC
class BoardView(Observer):
    """Class responsible for visually representing the game state"""

    def __init__(self, model):
        """Initialize a graphical representation of the given game board"""
        Observer.__init__(self)
        self.model = model
        self.tile_size = 25     # Default tile size
        self.tile_margin = 5    # Default tile margin

        # Initialize the board with an empty grid
        screen.fill(BLACK)

        for row in range(self.model.get_rows()):
            for column in range(self.model.get_columns()):
                # Find the x coordinate of the tile
                x_coord = self.tile_margin + ((self.tile_size + self.tile_margin) * column)

                # Find the y coordinate of the tile
                y_coord = self.tile_margin + ((self.tile_size + self.tile_margin) * row)

                # Draw empty square tiles
                pygame.draw.rect(screen, WHITE, [x_coord, y_coord, self.tile_size, self.tile_size])

        # Update pygame display
        pygame.display.flip()

    def set_tile_size(self, size):
        """Set the size of a tile for graphical representation"""
        self.tile_size = size

    def set_tile_margin(self, margin):
        """Set the size between tiles for graphical representation"""
        self.tile_margin = margin

    def get_tile_size(self):
        """Return the size of a tile for graphical representation"""
        return self.tile_size

    def get_tile_margin(self):
        """Return the size between tiles for graphical representation"""
        return self.tile_margin

    def update(self):
        """Update the graphical representation of the game"""
        pass



if __name__ == "__main__":
    """Initialize the game"""
    # Initialize pygame
    pygame.init()

    # Create a window
    window = [575, 575]

    # Set the pygame screen to be displayed in window
    screen = pygame.display.set_mode(window)

    # Change the title of the window
    pygame.display.set_caption("Connect 5")

    # Create a new game model with a 19x19 grid
    model = BoardModel(19, 19)

    # Create a new game view with previous game model
    view = BoardView(model)

    model.attach(view)

    #model.notify_observers()

    run = True
    while(run):
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type != pygame.QUIT or not model.is_won():
                model.notify_observers()
            else:
                run = False
                pygame.quit()
                sys.exit()

    # Pause game view before terminating
    time.sleep(5)
