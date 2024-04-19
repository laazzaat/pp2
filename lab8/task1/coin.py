import pygame
import random

SPEED = 3
SCREEN_WIDTH = 400

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        global COOLDOWN
        self.image = pygame.image.load(r"C:\\Users\\Admin\Desktop\\PP2_spring-main\\pp2\\TSIS8\\task1\\assets\\coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
            self.rect.move_ip(0, SPEED)
            if (self.rect.top > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)