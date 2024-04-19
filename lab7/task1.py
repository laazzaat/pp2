import pygame
import math
import time

pygame.init()

# set up the window
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clock')

# define the clock center and radius
clock_center = (400, 400)
clock_radius = 150

# define the clock hands length and width
hour_hand_length = 120
hour_hand_width = 20
minute_hand_length = 180
minute_hand_width = 10
second_hand_length = 180
second_hand_width = 2

# define the colors
background_color = (255, 255, 255)
clock_hand_color = (0, 0, 0)

# image 
clock = pygame.image.load('C:\\Users\\Admin\\Desktop\\PP2_spring-main\\pp2\\TSIS7\\images\\mickeyclock.jpeg')
rect = clock.get_rect()
rect.center = clock_center

# draw clock hand
def drawHand(angle, center, width, length):
    hour_hand_end = (clock_center[0] + length * math.cos(angle),
                     clock_center[1] + length * math.sin(angle))
    pygame.draw.line(window, clock_hand_color, center, hour_hand_end, width)


# main loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # get the current time
    current_time = time.localtime()
    window.fill(background_color)
    window.blit(clock, rect)

    # - pi/2 so clock hand period ends exactly at 12, not 9
    hour_angle = (current_time.tm_hour % 12 + current_time.tm_min / 60) * math.pi / 6 - math.pi / 2
    drawHand(hour_angle, clock_center, hour_hand_width, hour_hand_length)

    minute_angle = current_time.tm_min * math.pi / 30 - math.pi / 2
    drawHand(minute_angle, clock_center, minute_hand_width, minute_hand_length)

    second_angle = current_time.tm_sec * 2.0 * math.pi / 60.0 - math.pi / 2
    drawHand(second_angle, clock_center, second_hand_width, second_hand_length)

    pygame.display.update()