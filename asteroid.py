import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # boots solution pygame needs a tuple of ints.
        # it does work with this but this way we avoind breaking
        # changes should they update the pygame library
        #center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", self.centre(), int(self.radius), 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
