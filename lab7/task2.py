import pygame
import random

pygame.init()
# Songs below are made by me :D
# Used Fl Studio 20 for production, first one uses BeepBox

path = r"C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS7\\audio"

songs = [path+r"\raining oranges.mp3", 
         path+r"\smth tropical.mp3",
         path+r"\Spider theme pluto remix.mp3", 
         path+r"\Raindrops.mp3",
         path+r"\Planet theme.mp3", 
         path+r"\Snowcats.mp3",
         path+r"\when muffins sleep.mp3",
         path+r"\ruska 8bit.mp3",
         path+r"\stardust.mp3"
         ]
i = random.randint(0, len(songs)-1)
pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()


WIDTH = 200
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fPaused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            # pause
            if event.key == pygame.K_SPACE and not fPaused:
                pygame.mixer.music.pause()
                fPaused = True
            elif event.key == pygame.K_SPACE and fPaused:
                pygame.mixer.music.unpause()
                fPaused = False
            
            # previous
            if event.key == pygame.K_LEFT:
                    i -= 1
                    pygame.mixer.music.load(songs[i%len(songs)])
                    pygame.mixer.music.play()
            # next
            if event.key == pygame.K_RIGHT:
                    i += 1
                    pygame.mixer.music.load(songs[i%len(songs)])
                    pygame.mixer.music.play()

            

    screen.fill((0, 0, 0))
    pygame.display.update()
