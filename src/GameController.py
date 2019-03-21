# Define imports
import pygame
from pygame import *
import sys
import time


class Controller:
    """Class responsible for interacting with the Model and View."""
    
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
        
        # Start with Player 1
        current_player = 1
        pygame.display.set_caption("Player {}'s turn".format(current_player))
        
        # Start playing
        is_won = False
        
        while not is_won:
            
            for event in pygame.event.get():
            
                if event.type == pygame.MOUSEBUTTONDOWN:
    
                    click = pygame.mouse.get_pos()
                    
                    # Find board tile from click coordinates
                    row = (click[1] // (self.tile_size + self.tile_margin))
                    column = (click[0] // (self.tile_size + self.tile_margin))
                    
                    # If tile is unclaimed
                    if self.board[row][column] == 0:
                        
                        # Claim tile
                        self.board[row][column] = current_player
                        
                        # Update board
                        self.view.update()
                        
                        # Check if winning move
                        if self.model.is_won(current_player, row, column):

                            # Display win message
                            pygame.display.set_caption("Player {} won the game!".format(current_player))                           
                            
                            # Display win animation
                            self.view.win_animation(current_player)

                            # Update win condition                  
                            is_won = True
  
                        # Continue game if no winning move
                        else:    
                            
                            # Switch players
                            current_player += 1
                            if current_player > self.num_players:
                                current_player = 1
                                
                            # Display next player's turn message
                            pygame.display.set_caption("Player {}'s turn".format(current_player))

                # If player quits    
                elif event.type == pygame.QUIT:
                    # Terminate program
                    sys.exit()        

        # Terminate pygame
        pygame.quit()
        
        # Pause game view before terminating
        time.sleep(5)           