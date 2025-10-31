import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.lifetime = SHOT_LIFETIME

    def draw(self, screen):
        # code taken from asteroid.py
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
