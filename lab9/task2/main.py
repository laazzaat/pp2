import pygame
from snake import *
from food import Food
from super_food import SFood

pygame.init()

# avergae initalization
bounds = (500, 300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

block_size = 10
snake = Snake(block_size, bounds)
food = Food(block_size,bounds)
sfood = SFood(block_size, bounds)
antispeed = 100
LEVEL = 0

# font
font = pygame.font.Font(r'C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS9\\task2\\assets\\dogica.ttf',12)
next_level = pygame.USEREVENT + 1
sf_disappear = pygame.USEREVENT + 2
sf_appear = pygame.USEREVENT + 3


n = 11 # every 10th fruit level is increased
isEvent = False
current_collected = 0

timer = 3000
pygame.time.set_timer(sf_disappear, timer)
isDisappeared = False
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == next_level:
            antispeed -= 10
            LEVEL += 1
            print(True)
        if event.type == sf_disappear:
            if isDisappeared == False:
                print('disappear!')
                sfood.spawn_outside_borders()
                isDisappeared = True
            else:
                print("appear!")
                sfood.respawn(snake_body=Snake.body)
                isDisappeared = False

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
    sfood.draw(pygame, window)  
    snake.check_for_food(food, 0) # 0 - small food
    snake.check_for_food(sfood, 1) # 1 - super food


    SCORE = Snake.get_score()
    COLLECTED = Snake.get_collected()
    scores = font.render(f'score: {str(SCORE)}', True, (255, 255, 255))
    window.blit(scores, (0,0))
    levels = font.render(f'level: {str(LEVEL)}', True, (255, 255, 255))
    window.blit(levels, (0, 20))
    fruits = font.render(f'collected: {str(COLLECTED)}', True, (255, 255, 255))
    window.blit(fruits, (0, 40))

    # moves to next level every 10 fruits
    if (COLLECTED + 1) % n == 0 and isEvent == False:
        pygame.event.post(pygame.event.Event(next_level))
        print('event', COLLECTED )
        isEvent = True
        current_collected = COLLECTED 

    if isEvent: # so event wont run forever
        if COLLECTED  > current_collected:
            isEvent = False
    # print(COLLECTED , current_collected, isEvent)



    # starts again if game overs
    if snake.check_bounds() == True or snake.check_tail_collision() == True:
        text = font.render('Game Over', True, (255,255,255))
        window.blit(text, (bounds[0]//2 - 50, bounds[1]//2))
        pygame.display.update()
        pygame.time.delay(1000)
        snake.respawn()
        food.respawn(snake_body=Snake.body)
        sfood.respawn(snake_body=Snake.body)
        n = 11
        LEVEL = 0
        antispeed = 100
        COLLECTED = 0

    pygame.display.update()
    clock.tick(60)
