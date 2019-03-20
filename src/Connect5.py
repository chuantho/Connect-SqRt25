import pygame
from pygame import *
import sys
import os
import time
import random


# Define some base colors

# Board colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player colors
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
    
    def is_claimed(self, player, row, column):
        """Check if a given tile is claimed by the given palyer"""
        
        if self.board[row][column] == player:
            return True
        else:
            return False
        
                   
    def is_won(self, player, row, column):
        """Check if a given player has won the game"""
        
    # Check if player won horizontally
        
        # Check left
        left = 0
        
        for i in range(1, 5):
            if (0 <= column - i <= 18):
                if self.is_claimed(player, row, column - i):
                    left += 1
                else:
                    break                
            
        #//print("left:", left)
            
        # Check right
        right = 0
        
        for i in range(1, 5):
            if (0 <= column + i < 18):
                if self.is_claimed(player, row, column + i):
                    right += 1
                else:
                    break                
            
        #//print("right:", right)
        
        # Check if won
        print("Horizontal:" + str(left + right))

        if ((left + right + 1) >= 5):
            print("Player", str(player), " won the game!\n")
            return True
            
    # Check if player won vertically
            
        # Check top    
        top = 0
            
        for i in range(1, 5):
            if (0 <= row - i <= 18):
                if self.is_claimed(player, row - i, column):
                    top += 1
                else:
                    break                
            
        #//print("top:", top)
        
        # Check bottom
        bottom = 0    
        
        for i in range(1, 5):
            if (0 <= row + i <= 18):
                if self.is_claimed(player, row + i, column):
                    bottom += 1
                else:
                    break
            
        #//print("bottom:", bottom)
        
        # Check if won  
        print("Vertical:" + str(top + bottom))
                    
        if ((top + bottom + 1) >= 5):
            print("Player", str(player), " won the game!\n")
            return True

    # Check if player won diagonally (1)
            
        # Check top left
        topleft = 0
        
        for i in range(1, 5):
            if (0 <= row - i <= 18) and (0 <= column - i <= 18):
                if self.is_claimed(player, row - i, column - i):
                    topleft += 1
                else:
                    break                
            
        #//print("topleft:", topleft)
            
        # Check bottom right    
        bottomright = 0
        
        for i in range(1, 5):
            if (0 <= row + i <= 18) and (0 <= column + i <= 18):
                if self.is_claimed(player, row + i, column + i):
                    bottomright += 1
                else:
                    break                
            
        #//print("bottomright", bottomright)
        
        # Check if won
        print("Diagonal (1):" + str(topleft + bottomright))
                
        if ((topleft + bottomright + 1) >= 5):
            print("Player", str(player), " won the game!\n")  
            return True 
                    
    # Check if player won diagonally (2)
            
        # Check topright
        topright = 0
        
        for i in range(1, 5):
            if (0 <= row + i <= 18) and (0 <= column + i <= 18):
                if self.is_claimed(player, row - i, column + i):
                    topright += 1
                else:
                    break                

        #//print("topright:", topright)
        
        # Check bottomleft
        bottomleft = 0
            
        for i in range(1, 5):
            if (0 <= row + i <= 18) and (0 <= column + i <= 18):
                if self.is_claimed(player, row + i, column - i):
                    bottomleft += 1
                else:
                    break                
            
        #//print("bottomleft:", bottomleft)
        
        # Check if won
        print("Diagonal (2):" + str(topright + bottomleft))
                
        if ((topright + bottomleft + 1) >= 5):
            print("Player", str(player), " won the game!\n") 
            return True
        
        print("\n")
        
        return False

class MainMenuView:
    """Class responsible for visually representing the main menu """
    
    def __init__(self):
        #Initalize a graphical representation of the main menu
        
        font = pygame.font.SysFont("tahoma", 25)
        titlefont = pygame.font.SysFont("tahoma", 35)
        window = [575,575]
        pygame.display.set_caption ("Connect5")        
        background = pygame.image.load("assets/gomuku.jpg")
        background= pygame.transform.scale(background, (575,575))
        screen = pygame.display.set_mode(window)
        screen.blit(background, (0,0))
        #Sets values for each player    
        player_one = 1
        player_two = 2
        player_three = 3
        player_four = 4
        player_five = 5
        
        #Sets the color to black
        black_col = (0,0,0)
        
        title = titlefont.render("Connect Five", 1, black_col )
        player_one = font.render("One Player", 1, black_col )
        player_two = font.render("Two Player", 1, black_col )
        player_three = font.render("Three Player", 1, black_col )
        player_four = font.render("Four Player", 1, black_col )
        player_five = font.render("Five Player", 1, black_col )
        
        #Default player mode is set to 1
        player_mode = 1

        #Display the labels based off the x and y coordinate respectively
        screen.blit(title, (200,0))
        screen.blit(player_one, (200,100))
        screen.blit(player_two, (200,150))
        screen.blit(player_three, (200,200))
        screen.blit(player_four, (200,250))
        screen.blit(player_five, (200,300))
        pygame.display.flip()

        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    # Get the co-ordinates of the mouse click
                    x, y = pygame.mouse.get_pos()
                    # Set the player mode based off the click co-ordinates 
                    if(x >= 198 and x <= 320) and (y >= 105 and y <= 129):
                        self.set_player_mode(1)
                        return
                        
                    elif(x >= 200 and x <= 320) and (y >= 155 and y <= 179):
                        self.set_player_mode(2)
                        return 
                        
                    elif(x >= 200 and x <= 320) and (y >= 205 and y <= 228):
                        self.set_player_mode(3)
                        return
     
                    elif(x >= 200 and x <= 320) and (y >= 252 and y <= 280):
                        self.set_player_mode(4)
                        return
                    
                    elif(x >= 200 and x <= 320) and (y >= 302 and y <= 329):
                        self.set_player_mode(4)
                        return                    
                    
                elif event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()                    

    def set_player_mode(self, player_mode):
        """Set the number of players"""
        self.player_mode = player_mode 
        
    def get_player_mode(self):
        """Get the number of players"""
        return self.player_mode  
        
        
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
                    
                else :   
                    for player in range(1, num_players + 1):
                        if self.model.get_board()[row][column] == player:
                            color = player_list.get(player)
                
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
         
    # Multiplayer Setup
    font = pygame.font.SysFont("arialblack", 25)  
    main_menu_view = MainMenuView() 
    num_players = main_menu_view.get_player_mode()
          
    # Initialize the player list      
    player_list = {}
    
    for player in range(1, num_players + 1):
        # Assign a color to every player
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)    
        
        player_list[player] = color
        print(player, player_list[player])
        
    
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
                    
                    # Claim tile
                    board[row][column] = player
                    print("Tile" + "[" + str(row) + "][" + str(column) + "] " + "claimed by Player " + str(player))
                    
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
                          "[" + str(column) + "] " 
                          + "already claimed by Player " 
                          + str(board[row][column]))                
                
        
            elif event.type == pygame.QUIT:
                # Exit loop and terminate game
                is_done = True
                
    # Terminate pygame
    pygame.quit()
    
    # Pause game view before terminating
    time.sleep(3)    
