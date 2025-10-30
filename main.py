import pygame
from constants import *
from circleshape import CircleShape

def main():
    # inintialize pygame and game components
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    #print("Screen width: ", SCREEN_WIDTH)
    #print("Screen height: ", SCREEN_HEIGHT)	
    # init delta time fps counter /1000 conrt to s
    dt = 0     

    # begin infinite game loop
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.flip() 
        
        # Cap the frame rate
        dt =clock.tick(60)/1000  # Limit to 60 frames per second


    # Quit Pygame
    pygame.quit()   

if __name__ == "__main__":
    main()
