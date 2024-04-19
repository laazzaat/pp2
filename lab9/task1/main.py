#Imports
import pygame, sys
from pygame.locals import *
import random
import time
import enemy
import player
import coin
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

COLLECTED = 0 # coins collected

#Creating colors
YELLOW = (255,255,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r"C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS9\\task1\\assets\\road.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

                   
#Setting up Sprites        
P1 = player.Player()
E1 = enemy.Enemy()
C1 = coin.Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group(C1)
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
 
SCORE = 0 # Sum of the collected coins' weight
n = 10 # every 10th coin speed increases

#Game Loop
while True:

    ENEMIES_PASSED = enemy.SCORE
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              enemy.SPEED += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
 
    DISPLAYSURF.blit(background, (0,0))
    passed = font_small.render(f'Enemies passed: {ENEMIES_PASSED}', True, WHITE)
    collected = font_small.render(f'Coins collected: {COLLECTED}', True, YELLOW)
    score = font_small.render(f'Score: {SCORE}', True, RED)
    DISPLAYSURF.blit(passed, (10,10))
    DISPLAYSURF.blit(collected, (10, 30)) # shows coins collected amount
    DISPLAYSURF.blit(score, (10,50))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r'C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS9\\task1\\assets\\crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 

          time.sleep(2)
          pygame.quit()
          sys.exit()      
    # If player collides with coin, coin sprites from top again and again
    if pygame.sprite.spritecollideany(P1, coins):
            COLLECTED += 1
            SCORE += coin.WEIGHT
            coin.Coin.respawn(C1)
            # print(coin.WEIGHT)
         
    # increases speed everytime we collect 10 coins
    if (COLLECTED + 1) % n == 0:
        pygame.event.post(pygame.event.Event(INC_SPEED))
        n += 10 # so event wont keep posting forever
        print('inc_speed')

    pygame.display.update()
    FramePerSec.tick(FPS)