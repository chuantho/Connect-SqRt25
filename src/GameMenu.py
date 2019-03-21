# Define imports
import pygame
from pygame import *
import sys

# Define menu colors
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
BLACK = (0, 0, 0)


class Menu:
    """Class responsible for showing the menu and starting the game."""
    
    
    def __init__(self):
        """Initalize a graphical representation of the menu."""       
    
        # Initialize pygame
        pygame.init()
        
        # Define fonts
        TITLE_FONT = pygame.font.SysFont("arial", 65)
        NORMAL_FONT = pygame.font.SysFont("arial", 25)
        
        
        # Initialize menu window
        window = [420,750]
        screen = pygame.display.set_mode(window)
        
        # Display instructions
        pygame.display.set_caption ("Pick a number of players and click 'START PLAYING'")  
        
        
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
            x = 125 + (p * 30)
            pygame.draw.rect(screen, GREY, Rect(x, 640, 10, 5))
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

        start = False
        drag = False
        
        while not start:
            
            for event in pygame.event.get():
                
                x, y = pygame.mouse.get_pos()
                
                # Slider
                if (x >= 125 and x <= 345) and (y >= 600 and y <= 640):
                
                    # Start drag
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        drag = True
                      
                    #  Drag
                    elif (event.type == pygame.MOUSEMOTION) and (drag == True):
                        
                        # Update slider box
                        pygame.draw.rect(screen, GREY, Rect(125, 600, 220, 40))
                        
                        # Move slider
                        if (x >= 125 and x <= 130):
                            pygame.draw.rect(screen, BLACK, Rect(x, 600, 10, 40))                             
                        elif (x <= 345 and x >= 340):
                            # Add padding to prevent slider from going outside slider box
                            pygame.draw.rect(screen, BLACK, Rect(x - 10, 600, 10, 40))    
                        else:
                            # Add padding to prevent slider from going outside slider box
                            pygame.draw.rect(screen, BLACK, Rect(x - 5, 600, 10, 40))    
                            
                        # Update player selection
                        self.player_select = ((x - 125) // 30) + 1 
                        
                        # Update player selection label
                        pygame.draw.rect(screen, WHITE, Rect(365, 600, 80, 80))
                        screen.blit(TITLE_FONT.render(
                            str(self.get_player_select()), 
                            1, BLACK), (365, 600)) 
                        
                        # Update menu view
                        pygame.display.flip()
                
                    # End drag
                    elif (event.type == pygame.MOUSEBUTTONUP) and (drag == True):
                        drag = False
                
                # Start button      
                elif (x >= 115 and x <= 325) and (y >= 695 and y <= 730):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start = True
                        pygame.display.quit()
                
                # If user quits before starting game       
                else:
                    if event.type == pygame.QUIT:
                        # Terminate program
                        sys.exit() 

    def set_player_select(self, player_select):
        """Set the number of players selected."""
        self.player_select = player_select 
        
        
    def get_player_select(self):
        """Get the number of players selected."""
        return self.player_select 