# Define imports
import pygame
from pygame import *
import sys


class Controller:
    """Class responsible for interacting with the Board, Model and View."""
    
    def __init__(self, view):
        """Initialize a controller taking input from the View."""
        
        self.model = view.get_model()
        self.board = self.model.get_board()
        self.num_players = self.model.get_num_players()
        self.player_list = self.model.get_player_list()
        
        self.view = view
        self.tile_size = self.view.get_tile_size()
        self.tile_margin = self.view.get_tile_margin()        
        
    def play(self):
        """Play the game until a player wins or quits."""
        
        # Initialize pygame
        pygame.init()
        
        # Start playing with Player 1
        player = 1
        game = True
        
        while game:
            
            for event in pygame.event.get():
            
                if event.type == pygame.MOUSEBUTTONDOWN:
    
                    click = pygame.mouse.get_pos()
                    
                    # Find board tile from click coordinates
                    row = (click[1] // (self.tile_size + self.tile_margin))
                    column = (click[0] // (self.tile_size + self.tile_margin))
                    
                    # If tile is unclaimed
                    if self.board[row][column] == 0:
                        
                        # Claim tile
                        self.board[row][column] = player
                        print("Tile" + 
                              "[" + str(row) + "]" + 
                              "[" + str(column) + "] " + 
                              "claimed by Player " + 
                              str(player))
                        
                        #Update board
                        self.view.update()
                        
                        # Check if winning move
                        if self.model.is_won(player, row, column):
                            game = False
                            
                        # Switch players
                        player += 1
                        if player > self.num_players:
                            player = 1
                        
                    # If tile is claimed   
                    else:
                        print("Tile" + 
                              "[" + str(row) + "]" + 
                              "[" + str(column) + "] " +
                              "already claimed by Player " +
                              str(self.board[row][column]))                
                
                # If player quits    
                elif event.type == pygame.QUIT:
                    # Terminate program
                    sys.exit()        

        # Terminate pygame
        pygame.quit()
        
        # Pause game view before terminating
        time.sleep(3)           