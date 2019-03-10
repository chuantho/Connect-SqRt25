import pygame
import time
import random


# Define some base colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)




# M of MVC
class BoardModel:
    """Class responsible for storing the game state"""
    
    
    def __init__(self, num_rows, num_columns):
        """Initialize an empty game board with given rows and columns"""
        
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
    
        
    def get_columns(self):
        """Return the number of columns of the game board"""
        return self.columns
                   
               
               
# V of MVC                
class BoardView:
    """Class responsible for visually representing the game state"""
    
    def __init__(self, model): 
        """Initialize a graphical representation of the given game board"""
        self.model = model
        self.tile_size = 25     # Default tile size
        self.tile_margin = 5    # Default tile margin
        
        # Initialize the graphical representation
        self.update()           
    
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
        
        # Reset the screen
        screen.fill(BLACK)
        
        for row in range(self.model.get_rows()):
            for column in range(self.model.get_columns()):
                
                # Check if empty tile
                if self.model.get_board()[row][column] == 0:
                    color = WHITE
                    
                elif self.model.get_board()[row][column] == 1:
                    color = RED
                
                # Find the x coordinate of the tile
                x_coord = self.tile_margin + ((self.tile_size + self.tile_margin) * column)
                
                # Find the y coordinate of the tile
                y_coord = self.tile_margin + ((self.tile_size + self.tile_margin) * row)
                
                # Draw square tiles
                pygame.draw.rect(screen, color, [x_coord, y_coord, self.tile_size, self.tile_size])
         
        # Update pygame display
        pygame.display.flip()

        
        
# Controller        
if __name__ == "__main__":

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
    
    player = 1 # Placeholder for player
    is_done = False
    
    while not is_done:
        
        for event in pygame.event.get():
        
            if event.type == pygame.MOUSEBUTTONDOWN:

                click = pygame.mouse.get_pos()
                
                board = model.get_board()
                
                tile_size = view.get_tile_size()
                
                tile_margin = view.get_tile_margin()
                
                column = click[0] // (tile_size + tile_margin)
                
                row = click[1] // (tile_size + tile_margin)
                
                # If tile is unclaimed
                
                if board[row][column] == 0:
                    board[row][column] = player
                    print("Tile" + "[" + str(row) + "][" + str(column) + "] " + "claimed by Player " + str(player))
                    
                    #Update board
                    view.update()
                    
                # If tile is claimed   
                else:
                    print("Tile" + "[" + str(row) + "][" + str(column) + "] " + "already claimed by Player " + str(board[row][column]))                
                
        
            elif event.type == pygame.QUIT:
                # Exit loop and terminate game
                is_done = True
                
    # Terminate pygame
    pygame.quit()
    
    # Pause game view before terminating
    time.sleep(3)    
