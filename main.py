import pygame, sys
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updatables_group = pygame.sprite.Group()
    drawables_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids_group, updatables_group, drawables_group)
    Shot.containers = (shots_group, updatables_group, drawables_group)
    Player.containers = (updatables_group, drawables_group) 
    AsteroidField.containers = (updatables_group,)  
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, drawables_group, updatables_group, shots_group)
    

    
    
    print("Starting asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for drawable in drawables_group:
            drawable.draw(screen)
            shots_group.draw(screen)
        
        for updatable in updatables_group:
            updatable.update(dt)

        for asteroid in asteroids_group:
            for shot in shots_group:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()



            
        for asteroid in asteroids_group:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    
    main()