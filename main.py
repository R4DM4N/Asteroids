import pygame
from constants import *

def main():
    # inintialize pygame and game components
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    #print("Screen width: ", SCREEN_WIDTH)
    #print("Screen height: ", SCREEN_HEIGHT)	
     
    # begin infinite game loop    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    screen.fill(BLACK)
    pygame.display.flip() 
        

if __name__ == "__main__":
    main()
