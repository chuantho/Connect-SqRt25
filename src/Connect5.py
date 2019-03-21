# Define imports
import pygame
from pygame import *
import random

# Define helpers
from GameMenu import Menu
from GameModel import Model
from GameView import View
from GameController import Controller

               
if __name__ == "__main__":
    
    # Initialize pygame
    pygame.init()    
    
    # Initialize menu
    menu = Menu() 

    # Set number of players selected in menu
    num_players = menu.get_player_select()    
          
    # Initialize the player list      
    player_list = {}
    
    # Create the players
    for player in range(1, num_players + 1):
        # Assign a random color to each player
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    
        player_list[player] = color

    # Create a new game model with previous number of players and list of players
    model = Model(num_players, player_list)

    # Create a new game view with previous model
    view = View(model)
    
    # Create a new game controller with previous view
    controller = Controller(view)
    
    # Play the game
    controller.play()