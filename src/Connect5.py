import pygame
from pygame import *
import sys
import os
import time
import random


# Define colors
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
BLACK = (0, 0, 0)


class BoardModel:
    """Class responsible for storing the game state."""
    
    
    def __init__(self, num_rows, num_columns):
        """Initialize an empty game board with given rows and columns."""
        
        self.rows = num_rows
        self.columns = num_columns
        self.board = []
        
        for row in range(num_rows):
            self.board.append([])
            for column in range(num_columns):
                # Set every cell to value 0 to represent an empty tile
                self.board[row].append(0)  
    
        
    def get_board(self):
        """Return the current board state."""
        return self.board
    
    
    def get_rows(self):
        """Return the number of rows of the game board."""
        return self.rows
    
        
    def get_columns(self):
        """Return the number of columns of the game board."""
        return self.columns
    
    def is_claimed(self, player, row, column):
        """Check if a given tile is claimed by the given player."""
        
        if self.board[row][column] == player:
            return True
        else:
            return False
          
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
            print("Player", str(player), " won the game!\n")
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
            print("Player", str(player), " won the game!\n")
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
            print("Player", str(player), " won the game!\n")  
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
            print("Player", str(player), " won the game!\n") 
            return True

        return False
    
    
class MenuView:
    """Class responsible for visually representing the main menu."""
    
    
    def __init__(self):
        """Initalize a graphical representation of the main menu."""       
        
        # Define fonts
        TITLE_FONT = pygame.font.SysFont("arial", 65)
        NORMAL_FONT = pygame.font.SysFont("arial", 25)
        
        
        # Initialize menu window
        window = [420,750]
        pygame.display.set_caption ("Connect Sqrt(25)")  
        screen = pygame.display.set_mode(window)
        
        
        # Import background image
        background = pygame.image.load("assets/gomuku.jpg")
        background= pygame.transform.scale(background, (420,750))
        
        # Display background image
        screen.blit(background, (0,0))
        
        
        # Create title label
        title_label = TITLE_FONT.render("Connect Sqrt(25)", 1, BLACK)
        
        # Display title label
        screen.blit(title_label, (35,40))        


        # Create slider box
        pygame.draw.rect(screen, GREY, Rect(125, 600, 220, 40))
        
        # Create slider
        pygame.draw.rect(screen, BLACK, Rect(125, 600, 10, 40))
        
        # Create slider indicators for player selection
        for p in range(0,8):
            separator = 125 + (i * 30)
            pygame.draw.rect(screen, GREY, Rect(separator, 640, 10, 5))
            screen.blit(NORMAL_FONT.render(str(p + 1), 1, BLACK), (x, 650))


        # Initialize player selection to 1
        self.set_player_select(1) 
        
        # Display player selection
        screen.blit(TITLE_FONT.render(str(self.player_select), 1, BLACK), (365, 600))    
        
        
        # Create play button
        pygame.draw.rect(screen, BLACK, Rect(115, 695, 210, 35))
        pygame.draw.rect(screen, GREY, Rect(120, 700, 200, 25))
        
        # Display play button
        screen.blit(NORMAL_FONT.render("START PLAYING", 1, BLACK), (150, 705))
        
        
        # Update menu view
        pygame.display.flip()        

        menu = True
        drag = False
        
        while menu:
            
            for event in pygame.event.get():
                
                x, y = pygame.mouse.get_pos()
                
                # Slider
                if (x >= 125 and x <= 345) and (y >= 600 and y <= 640):
                
                    # Start drag
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        drag = True
                      
                    #  Drag
                    elif (event.type == pygame.MOUSEMOTION) and (drag == True):
                        
                        pygame.draw.rect(screen, GREY, Rect(125, 600, 220, 40))
                        
                        if (x >= 125 and x <= 130):
                            pygame.draw.rect(screen, BLACK, Rect(x, 600, 10, 40))                             
                        elif (x <= 345 and x >= 340):
                            pygame.draw.rect(screen, BLACK, Rect(x - 10, 600, 10, 40))    
                         
                        else:
                            pygame.draw.rect(screen, BLACK, Rect(x - 5, 600, 10, 40))    
                            
                        # Update player selection
                        self.player_select = ((x - 125) // 30) + 1 
                        
                        # Update player selection label
                        pygame.draw.rect(screen, WHITE, Rect(365, 600, 80, 80))
                        screen.blit(TITLE_FONT.render(
                            str(self.get_player_select()), 
                            1, BLACK), (365, 600)) 
                        
                        pygame.display.flip()
                
                    # End drag
                    elif (event.type == pygame.MOUSEBUTTONUP) and (drag == True):
                        drag = False
                
                # Start button      
                elif (x >= 115 and x <= 325) and (y >= 695 and y <= 730):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu = False
                        pygame.display.quit()
                          
                else :
                    if event.type == pygame.QUIT:
                        sys.exit()     


    def set_player_select(self, player_select):
        """Set the number of players."""
        self.player_select = player_select 
        
        
    def get_player_select(self):
        """Get the number of players"""
        return self.player_select 
                
                
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
                    
                else :   
                    for player in range(1, num_players + 1):
                        if self.model.get_board()[row][column] == player:
                            color = player_list.get(player)
                
                # Find the x coordinate of the tile
                x_coord = self.tile_margin + ((self.tile_size + self.tile_margin) * column)
                
                # Find the y coordinate of the tile
                y_coord = self.tile_margin + ((self.tile_size + self.tile_margin) * row)
                
                # Draw square tiles
                pygame.draw.rect(screen, color, 
                                 [x_coord, y_coord, self.tile_size, self.tile_size])
         
        # Update pygame display
        pygame.display.flip()
        
        
# Controller        
if __name__ == "__main__":
    
    # Initialize pygame
    pygame.init()    
    
    menu_view = MenuView() 

    # Create a window
    window = [575, 575]    
    
    # Set the pygame screen to be displayed in window
    screen = pygame.display.set_mode(window)    
         
    # Multiplayer Setup
    font = pygame.font.SysFont("arialblack", 25)  
    num_players = menu_view.get_player_select()
          
    # Initialize the player list      
    player_list = {}
    
    for player in range(1, num_players + 1):
        # Assign a random color to every player
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)    
        
        player_list[player] = color
        print(player, player_list[player])
        
    
    # Change the title of the window
    pygame.display.set_caption ("Connect Sqrt(25)") 

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
                    
                    # Claim tile
                    board[row][column] = player
                    print("Tile" + 
                          "[" + str(row) + "]" + 
                          "[" + str(column) + "] " + 
                          "claimed by Player " + 
                          str(player))
                    
                    #Update board
                    view.update()
                    
                    # Check if winning move
                    if model.is_won(player, row, column):
                        is_done = True
                        
                    # Switch players
                    player += 1
                    
                    if player > num_players:
                        player = 1
                    
                # If tile is claimed   
                else:
                    print("Tile" + 
                          "[" + str(row) + "]" + 
                          "[" + str(column) + "] " +
                          "already claimed by Player " +
                          str(board[row][column]))                
                
        
            elif event.type == pygame.QUIT:
                # Exit loop and terminate game
                sys.exit()
                
    # Terminate pygame
    pygame.quit()
    
    # Pause game view before terminating
    time.sleep(3)    
