import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False
color = (255, 0, 255)
x = 200
y = 200
radius = 20
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and y > radius: y -= 15
    if pressed[pygame.K_s] and y < 300 - radius: y += 15
    if pressed[pygame.K_a] and x > radius: x -= 15
    if pressed[pygame.K_d] and x < 300 - radius: x += 15

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (x,y), radius)
    pygame.display.flip()

    clock.tick(60)