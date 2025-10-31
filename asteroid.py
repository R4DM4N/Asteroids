import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # sub-classes must override
        #pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH)
        
        # boots solution pygame needs a tuple of ints.
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, int(self.radius), ASTEROID_LINE_WIDTH)
    
    def update(self, dt):
        self.velocity += self.velocity * dt
