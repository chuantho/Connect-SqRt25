# Define imports
import pygame
from pygame import *
import time

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class View:
    """Class responsible for graphically representing the game state stored in Model."""
    
    def __init__(self, model):
        """Initialize a graphical representation of the given game board stored in Model."""
        
        # Initialize pygame
        pygame.init()        
        
        # Create a window
        window = [575, 575]       

        # Set the pygame screen to be displayed in window
        self.screen = pygame.display.set_mode(window)         
                     
        self.model = model
        self.tile_size = 25     # Default tile side length
        self.tile_margin = 5    # Default space between tiles
        
        self.player_list = model.get_player_list()
        self.num_players = model.get_num_players()
        
        # Initialize the graphical interace
        self.update()           
        
    def get_tile_size(self):
        """Return the size of a tile on the graphical interface"""
        return self.tile_size
    
    def get_tile_margin(self):
        """Return the size between tiles on the graphical interface"""
        return self.tile_margin
    
    def get_model(self):
        """Return the GameModel used by GameView for graphical representation."""
        return self.model
    
    def update(self):
        """Update the graphical representation of the game."""
        
        # Reset the screen
        self.screen.fill(BLACK)
        
        for row in range(19):
            for column in range(19):
                
                # Check if empty tile
                if self.model.get_board()[row][column] == 0:
                    color = WHITE
                
                # Check if claimed tile    
                else :   
                    for player in range(1, self.num_players + 1):
                        # Find which player claimed the tile
                        if self.model.get_board()[row][column] == player:
                            # Convert tile from player number to color using player_list
                            color = self.player_list.get(player)
                
                # Find the x coordinate of the tile
                x_coord = self.tile_margin + (
                    (self.tile_size + self.tile_margin) * column)
                
                # Find the y coordinate of the tile
                y_coord = self.tile_margin + (
                    (self.tile_size + self.tile_margin) * row)
                
                # Draw tiles
                pygame.draw.rect(self.screen, color, 
                    [x_coord, y_coord, self.tile_size, self.tile_size])
         
        # Update graphical interface
        pygame.display.flip()
        
    def win_animation(self, winning_player):
        """Display a special animation when a player wins the game."""
        
        # Reset the screen
        self.screen.fill(BLACK)
        
        for row in range(19):
            for column in range(19):
                
                # Replace empty tiles with winning player's color
                if self.model.get_board()[row][column] == 0:
                    color = self.player_list.get(winning_player)
                  
                # Replace winning player's tiles with black tiles  
                elif self.model.get_board()[row][column] == winning_player:
                    color = BLACK
                  
                # Leave other players' tiles unchanged  
                else:
                    for player in range(1, self.num_players + 1):
                        if self.model.get_board()[row][column] == player:
                            color = self.player_list.get(player)
                
                # Find the x coordinate of the tile
                x_coord = self.tile_margin + (
                    (self.tile_size + self.tile_margin) * column)
                
                # Find the y coordinate of the tile
                y_coord = self.tile_margin + (
                    (self.tile_size + self.tile_margin) * row)
                
                # Draw tiles
                pygame.draw.rect(self.screen, color, 
                    [x_coord, y_coord, self.tile_size, self.tile_size])
         
        # Update graphical interface
        pygame.display.flip()   
