import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        #self, radius, position, velocity
        if self.radius > ASTEROID_MIN_RADIUS:
            #deconstruct old Asteroid be sure to kill it when your done
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            velocity_tuple = tuple(self.velocity)
            rnd_rotation = random.randint(20,50)
            x = self.position.x
            y = self.position.y
            velocity_mult = 0
            # create new asteroid
            for x in range(1,3):
                rnd_rotation *= -1
                velocity_mult += 1.2
                asteroid = Asteroid(x, y, new_radius)
                # set velocity
                asteroid.velocity = pygame.Vector2(velocity_tuple) * velocity_mult
                velocity = velocity.rotate(rnd_rotation)
        # remove if too small or has been broken into two
        self.kill()   