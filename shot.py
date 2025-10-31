import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        # code taken from asteroid.py
        pygame.draw.circle(screen, "white", self.position, int(self.radius), 2)
    
    def update(self, dt):
        self.position += self.velocity * dt