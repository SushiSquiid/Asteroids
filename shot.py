import pygame
from constants import *
from circleshape import *


class Shot(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, SHOT_RADIUS)

        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        
        self.rect = self.image.get_rect(center=(x, y))
        #self.position = pygame.Vector2(x, y)
        #self.velocity = velocity
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position