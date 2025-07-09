import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
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
        for drawable in drawable_group:
            print(drawable)
            drawable.draw(screen)
        pygame.display.flip() #THIS MUST ALWAYS BE LAST!!!!

        dt = py_clock.tick(60)/1000 #allowed to be past flip function


if __name__ == "__main__":
    main()
