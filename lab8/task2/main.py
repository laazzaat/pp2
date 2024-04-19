import pygame
from snake import *
from food import Food

pygame.init()

# avergae initalization
bounds = (500, 300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

block_size = 10
snake = Snake(block_size, bounds)
food = Food(block_size,bounds)
antispeed = 100
LEVEL = 0

# font
font = pygame.font.Font(r'C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS8\\task2\\assets\\dogica.ttf',12)
next_level = pygame.USEREVENT + 1

n = 11 # every 10th fruit level is increased
while True:
    pygame.time.delay(antispeed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == next_level:
            antispeed -= 10
            LEVEL += 1
            print(True)

        keys = pygame.key.get_pressed() # keyboard control
        if keys[pygame.K_LEFT]:
            snake.steer(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            snake.steer(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            snake.steer(Direction.UP)
        elif keys[pygame.K_DOWN]:
            snake.steer(Direction.DOWN)    

    snake.move()
    window.fill((0,0,0))
    snake.draw(pygame, window)
    food.draw(pygame, window)
    snake.check_for_food(food)

    SCORE = Snake.get_score()
    scores = font.render(f'score: {str(SCORE)}', True, (255, 255, 255))
    window.blit(scores, (0,0))
    levels = font.render(f'level: {str(LEVEL)}', True, (255, 255, 255))
    window.blit(levels, (0, 20))

    # moves to next level every 10 fruits
    if (SCORE + 1) % n == 0:
        pygame.event.post(pygame.event.Event(next_level))
        print('event', SCORE)
        n += 10 # so event wont keep posting forever
    print(SCORE)
        

    # starts again if game overs
    if snake.check_bounds() == True or snake.check_tail_collision() == True:
        text = font.render('Game Over', True, (255,255,255))
        window.blit(text, (bounds[0]//2 - 50, bounds[1]//2))
        pygame.display.update()
        pygame.time.delay(1000)
        snake.respawn()
        food.respawn(snake_body=Snake.body)
        n = 11
        LEVEL = 0
        antispeed = 100

    pygame.display.update()
    clock.tick(60)
