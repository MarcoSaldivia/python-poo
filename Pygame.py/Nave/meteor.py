import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, METEOR_SPEED

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((30,30))
        pygame.draw.circle(self.image,(255,0,0),(15,15),15)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # Aparece aleatoriamnete en la parte superior
        self.rect.y = -self.rect.height  # Simular q aparece afuera

    def update(self):
        self.rect.y += METEOR_SPEED
        # Si el meterorito sale en patalla, lo eliminamos
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
            
