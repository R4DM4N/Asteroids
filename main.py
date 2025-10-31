import pygame
from constants import *
from circleshape import *
from player import *

def main():
    # inintialize pygame and game components
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting Asteroids!")
    print("Screen width: ", SCREEN_WIDTH)
    print("Screen height: ", SCREEN_HEIGHT)

    # Group containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create all payer objects after this change
    Player.containers = (updatable, drawable)

    #SPAWN IN PLAYER
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2, PLAYER_RADIUS)  
	
    # Init delta time fps counter /1000 conrt to s
    dt = 0     

    # Begin infinite game loop
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen and set the screen background
        screen.fill("black")        

        # Update all sprites
        updatable.update(dt)

       
        # Draw objects
        #drawable.draw(screen) Works on sprites only not vectors
        for unit in drawable:
            unit.draw(screen)


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip() 
        
        # Cap the frame rate
        dt =clock.tick(60)/1000  # Limit to 60 frames per second


    # Quit Pygame
    pygame.quit()   

if __name__ == "__main__":
    main()
