import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (shots_group, drawable_group, updateable_group)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  
    asteroidfield = AsteroidField()  
    py_clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.collision_check(player):
                print("GAME OVER!")
                sys.exit()
            for shot in shots_group:
                if asteroid.collision_check(shot):
                    asteroid.kill()
                    shot.kill()
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip() #THIS MUST ALWAYS BE LAST!!!!

        dt = py_clock.tick(60)/1000 #allowed to be past flip function


if __name__ == "__main__":
    main()
