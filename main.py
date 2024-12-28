import pygame

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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
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
            
        #Paint elements on screen
        screen.fill("black")

        for item in updatable:
            item.update(dt)

        
        for asteroid in asteroids:

            #Exit game if asteroid collides with player
            if asteroid.is_collision(player):
                print("Game over!")
                exit()

            #Check collision with any bullet
            for shot in shots:
                if asteroid.is_collision(shot):
                    print("shot hit!")
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)
                


        for item in drawable:
            item.draw(screen)

        dt = clock.tick(FRAMERATE) /1000
        pygame.display.flip()


#Supposedly runs only when file is run directly
if __name__ == "__main__":
    main()