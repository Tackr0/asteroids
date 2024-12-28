import pygame # type: ignore

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Control game speed
    clock = pygame.time.Clock()
    dt = 0
    FRAMERATE = 60

    #Instantiates player in middle of screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Game updates every iteration
    while True:
        #Exit if user closes via x button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Paint elements on screen
        screen.fill("black")
        player.draw(screen)

        dt = clock.tick(FRAMERATE) /1000
        pygame.display.flip()


#Supposedly runs only when file is run directly
if __name__ == "__main__":
    main()