import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # inintialize pygame and game components
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Group containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Create all play objects after this change
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)

    
    #SPAWN IN PLAY objects
    asteroidfield = AsteroidField() 
    
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)  
	
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
        
        #collistion detection
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("GAME OVER!")
                running = False
        
        for asteroid in asteroids:
            for shot in shots:
                print(asteroid)    
                if shot.collision(asteroid):
                    print("hit,")
                    asteroid.kill()
                    shot.kill()


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip() 
        
        # Cap the frame rate
        dt =clock.tick(60)/1000  # Limit to 60 frames per second


    # Quit Pygame
    pygame.quit()   

if __name__ == "__main__":
    main()
