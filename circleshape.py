import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def centre(self):
        # I know Boots wanted this case to INT() but pygame uses floats for vectors
        return ((self.position.x),(self.position.y))

    def distance(self, other):
        return self.position.distance_to(other.position)    
    
    def collision(self, other):
        colission_radius = self.radius + other.radius
        return self.distance(other) < colission_radius