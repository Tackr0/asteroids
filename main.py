import pygame # type: ignore
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game updates every iteration
    while True:
        #Paint background of game black
        screen.fill("black")
        
        #Exit if user closes via x button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        pygame.display.flip()


#Supposedly runs only when file is run directly
if __name__ == "__main__":
    main()