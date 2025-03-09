import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()
colours = {"white":(255,255,255),"green":(188,227,199),
           "black":(0,0,0),"red":(255,0,0)}


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720
GAME_NAME = "Mr Philip's Snake Game"
GAME_ICON = "snake_icon.png"


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_icon(pygame.image.load(GAME_ICON))
pygame.display.set_caption(GAME_NAME)



def game_loop():
    quit_game = False
    snake_x = 200
    snake_y = 200
    food_x = round(random.randrange(20, SCREEN_WIDTH-20)/20)*20
    food_y = round(random.randrange(20, SCREEN_HEIGHT-20)/20)*20
    while quit_game == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
        screen.fill(colours["white"])
        pygame.draw.rect(screen, colours["black"], [snake_x, snake_y, 20, 20])
        pygame.draw.rect(screen, colours["red"], [food_x, food_y, 20, 20])
        pygame.display.update()

    

    pygame.quit()
    quit()

game_loop()
