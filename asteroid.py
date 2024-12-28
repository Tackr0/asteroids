import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #Calculate trajectories of children
        eject_angle = random.uniform(20, 50)
        child_1_velocity = self.velocity.rotate(eject_angle) * 1.2
        child_2_velocity = self.velocity.rotate(-1 * eject_angle) * 1.2

        #Calculate size of children
        child_radius = self.radius - ASTEROID_MIN_RADIUS

        #Create child asteroids
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = child_1_velocity

        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2.velocity = child_2_velocity

    def update(self, dt):
        self.position += self.velocity * dt