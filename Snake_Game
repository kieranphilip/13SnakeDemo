import pygame
import time

pygame.init()
clock = pygame.time.Clock()
colours = {"white":(255,255,255),"green":(188,227,199),
           "black":(0,0,0),"red":(255,0,0)}

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720
GAME_NAME = "Mr Philip's Snake Game"
GAME_ICON = "snake_icon.png"

quit_game = False

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game_icon = pygame.image.load(GAME_ICON)
pygame.display.set_icon(game_icon)
pygame.display.set_caption(GAME_NAME)
screen.fill(colours["white"])
pygame.display.update()

while quit_game == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_game = True

    


    

pygame.quit()
quit()

