import pygame
import sys

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Control game speed
    clock = pygame.time.Clock()
    dt = 0
    FRAMERATE = 60

    #Groups
    updatable = pygame.sprite.Group() #Evolve with time
    drawable = pygame.sprite.Group() #Rendered
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    #Instantiate game objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    #Game updates every iteration
    while True:

        #Exit if user closes via x button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
 
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:

            #Exit game if asteroid collides with player
            if asteroid.is_collision(player):
                print("Game over!")
                sys.exit()

            #Check collision with any bullet
            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()
                    
        #Paint elements on screen
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FRAMERATE) /1000


#Supposedly runs only when file is run directly
if __name__ == "__main__":
    main()