#Define imports
import pygame
from pygame import *
import sys
import time
import GameModel


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

        # Play until a player wins
        is_won = False
        count = 2
        while not is_won and count >= 0:
            # The player has no more time if count == 0
            if count == 0:
                int_list = GameModel.Model.randomize(self.model)
                row = int_list[0]
                column = int_list[1]
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

                    # Stop playing
                    is_won = True
                # Loop through mouse clicks
                count = 2
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Find board tile from click coordinates
                    click = pygame.mouse.get_pos()
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

                            # Stop playing
                            is_won = True

                        # Continue game if no winning move
                        else:

                            # Switch players
                            current_player += 1
                            if current_player > self.num_players:
                                current_player = 1

                            # Display next player's turn message
                            pygame.display.set_caption("Player {}'s turn".format(current_player))

                        # reset the turn timer for the next player
                        count = 2

                # If player quits
                elif event.type == pygame.QUIT:
                    # Terminate program
                    sys.exit()
            # Used to create time delay
            time.sleep(1)
            # print timer to inform player
            print(count)
            count -= 1

        # Terminate pygame
        pygame.quit()

        # Pause game view before terminating
        time.sleep(5)
