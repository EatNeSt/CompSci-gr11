# pygame template

from calendar import c
from distutils.spawn import spawn
from textwrap import fill
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables


circle_2_x = 100
circle_2_y = 60
circle_2_color = 255,215,0
circle_2_speed = 2

screen_red = 176
screen_yellow = 226
screen_blue = 253
screen_color_change_red = 1
screen_color_change_yellow = 1
screen_color_change_blue = 1

boat_1 = 650
boat_2 = 850
boat_3 = 800
boat_4 = 690
boat_mast = 725
boat_room = 785
boat_window_1 = 835
boat_window_2 = 800
boat_sail_1 = 735 
boat_sail_2 = 690
boat_sail_3 = 735

water_transparency = 130 

water = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
water_2 = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
cloud = pygame.Surface((WIDTH,200), flags=pygame.SRCALPHA)
#-----------------------------------------------------------------

# water
pygame.draw.rect(water, (0,191,255, 230), (0, 240, WIDTH, HEIGHT))

# Waves
pygame.draw.circle(water_2, (0,191,255, water_transparency), (660, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (640, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (630, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (610, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (600, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (590, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (570, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (556, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (540, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (530, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (510, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (490, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (490, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (479, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (460, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (445, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (430, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (420, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (400, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (385, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (370, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (360, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (340, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (319, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (310, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (300, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (290, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (260, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (245, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (230, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (205, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (200, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (182, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (170, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (152, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (140, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (132, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (110, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (102, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (80, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (53, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (50, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (34, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (20, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (0, 350),15)
pygame.draw.circle(water_2, (0,191,255, water_transparency), (-10, 350),15)
pygame.draw.rect(water_2, (0,191,255, water_transparency), (0, 350, WIDTH, HEIGHT))



# Cloud 1 - the one to the left
pygame.draw.circle(cloud, (255,255,255, 100), (80, 40),30)
pygame.draw.circle(cloud, (255,255,255, 100), (120, 40),30)
pygame.draw.circle(cloud, (255,255,255, 100), (65, 70),30)
pygame.draw.circle(cloud, (255,255,255, 100), (105, 70),30)
pygame.draw.circle(cloud, (255,255,255, 100), (135, 70),30)

# Cloud 2 - the one to the right
pygame.draw.circle(cloud, (255,255,255, 100), (480, 70),30)
pygame.draw.circle(cloud, (255,255,255, 100), (520, 70),30)
pygame.draw.circle(cloud, (255,255,255, 100), (550, 70),30)
pygame.draw.circle(cloud, (255,255,255, 100), (475, 100),30)
pygame.draw.circle(cloud, (255,255,255, 100), (505, 100),30)
pygame.draw.circle(cloud, (255,255,255, 100), (535, 100),30)
pygame.draw.circle(cloud, (255,255,255, 100), (555, 100),30)



#-----------------------------------------------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

#-----------------------------------------------------------------
    # GAME STATE UPDATES

    # The sky/background
    screen.fill((screen_red,screen_yellow,screen_blue))  # always the first drawing command
    
    # The hills
    pygame.draw.ellipse(screen, (102,129,50), (300, 0, 350, 480), 200) # hill in the very back
    pygame.draw.ellipse(screen, (202,209,30), (500, 85, 250, 300), 200) # hill to the left
    pygame.draw.ellipse(screen, (202,209,30), (230, 130, 400, 200), 100) # hill to the right

    # The sun
    pygame.draw.circle(screen, (circle_2_color), (circle_2_x, circle_2_y),30) 

    # The water
    screen.blit(water, (0, 0))

    # The clouds
    screen.blit(cloud, (0,0))

    # The boat
    pygame.draw.polygon(screen, (139,69,0),[(boat_1, 310), (boat_2, 310), (boat_3, 350),(boat_4, 350)])
    pygame.draw.rect(screen,(139,69,0), (boat_mast, 250, 10 , 80))
    pygame.draw.rect(screen,(139,69,0), (boat_room, 280, 65 , 30))
    pygame.draw.circle(screen, (152,245,255), (boat_window_1, 294), 10)
    pygame.draw.circle(screen, (152,245,255), (boat_window_2, 294), 10)
    pygame.draw.polygon(screen, (250,250,250), [(boat_sail_1,220), (boat_sail_2,290),(boat_sail_3,290)])
    
    #The waves
    screen.blit(water_2, (0, 0))

#-----------------------------------------------------------------

    # Code to change the place of the sun
    if circle_2_y > 300:
        circle_2_speed = circle_2_speed * -1
        if circle_2_color == (255,215,0):
            circle_2_color = 128,128,128
        else:
            circle_2_color = (255,215,0)
    elif circle_2_y < 60:
         circle_2_speed = circle_2_speed * -1

   
    # Code to change the color of the sky
    if screen_red < 1 :
       screen_color_change_red = 0.73
    elif screen_red > 176 :
        screen_color_change_red = -0.73
    if screen_blue < 78 :
       screen_color_change_blue = 0.73
    elif screen_blue > 253:
        screen_color_change_blue = -0.73
    if screen_yellow < 51:
       screen_color_change_yellow = 0.73
    elif screen_yellow > 226:
        screen_color_change_yellow = -0.73

    # Code to make the boat move
    if boat_3 < -50:
        boat_1 = 650
        boat_2 = 850
        boat_3 = 800
        boat_4 = 690
        boat_mast = 725
        boat_room = 785
        boat_window_1 = 835
        boat_window_2 = 800
        boat_sail_1 = 735 
        boat_sail_2 = 690
        boat_sail_3 = 735

    # This part always repeats 
    circle_2_y += circle_2_speed   
    screen_red += screen_color_change_red 
    screen_yellow += screen_color_change_yellow
    screen_blue += screen_color_change_blue
    boat_1 += -1
    boat_2 += -1
    boat_3 += -1
    boat_4 += -1
    boat_mast += -1
    boat_room += -1
    boat_window_1 += -1
    boat_window_2 += -1
    boat_sail_1 += -1 
    boat_sail_2 += -1
    boat_sail_3 += -1

    

    

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
    
    

    

    





pygame.quit()
