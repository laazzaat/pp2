import pygame
import random

SPEED = 3
SCREEN_WIDTH = 400
WEIGHT = 1

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        global COOLDOWN
        self.image = pygame.image.load(r"C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS9\\task1\\assets\\coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
        global WEIGHT
        WEIGHT = random.randint(1, 6)
    
    def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        global WEIGHT
        WEIGHT = random.randint(0, 5)
         

    def move(self):
            self.rect.move_ip(0, SPEED)
            if (self.rect.top > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)