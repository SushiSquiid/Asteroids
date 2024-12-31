import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, drawables_group, updatables_group, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.drawables_group = drawables_group
        self.updatables_group = updatables_group
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        
    def shoot(self):    
        shot_position = pygame.Vector2(self.position.x, self.position.y)
        direction = pygame.Vector2(0, -1)
        direction = direction.rotate(self.rotation)
        shot_velocity = (direction * PLAYER_SHOOT_SPEED)
        
        shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS, shot_velocity)
        self.shots_group.add(shot)
        



    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.shoot()
            print("three")
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
            
    def shoot(self):
        print("five")
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.drawables_group.add(shot)
        self.updatables_group.add(shot)
        self.shots_group.add(shot)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt