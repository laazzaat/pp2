import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
image = pygame.image.load('C:\KBTU\\2nd semester\pp2\TSIS7\\tutorial\\foxy.png')

while not done:
        screen.fill("black")
        screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # pygame.draw.circle(screen, (0, 128, 255), (150, 150), 60)
        pygame.display.update()
        clock.tick(60)