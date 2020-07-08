
#a bunch of imports
import pygame
import time
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

#sets up the screen
screen_x, screen_y = 800, 600
screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))

mouseX, mouseY = pygame.mouse.get_pos()

#sets up the ball's dimensions and pos
circle_x, circle_y = 100, 100
rad = 20

#sets up the paddle's dimensions and pos
rect_width = 160
rect_x = mouseX - rect_width/2
rect_y = 500
rect_height = 10

#sets up the game variables
speed_x, speed_y = 1, 1
hit_num_sec = 0
total_time = 0
sleep_time = 0.0001

while True:

    hit_num_sec = 0
    for i in range(100):

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        #updates numerous values from previous iteration
        mouseX, mouseY = pygame.mouse.get_pos()
        rect_x = mouseX - rect_width/2

        screen.fill((200, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        #draws the ball and paddle
        pygame.draw.circle(screen, (255, 0, 0),(circle_x, circle_y), rad)#ball
        pygame.draw.rect(screen,(0, 0, 0), Rect((rect_x, rect_y), (rect_width, rect_height)))#paddle

            
        #checks if the ball bounces anywhere
        if rect_y - rad <= circle_y  <= rect_y +rad and rect_x <= circle_x <= rect_x + rect_width:#bounces on paddle
            speed_y *= -1
            hit_num_sec += 1
        elif circle_x < rad or circle_x > screen_x - rad:#bounces on a wall
            speed_x *= -1
            
        elif circle_y > screen_y - rad:#bounces on bottom
            speed_y *= -1

            #exits the game
            
            exit()
        elif circle_y < rad:#bounces on top
            speed_y *= -1
            

            

        
            
        
            
        circle_x += speed_x
        circle_y += speed_y
        
        

        time.sleep(sleep_time)
        

        pygame.display.update()
    sleep_time*= 0.99
    total_time += 1
    

    
                     

