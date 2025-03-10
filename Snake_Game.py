import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()
colour = {"white": (255, 255, 255), "green": (188, 227, 199),
           "black": (0, 0, 0), "red": (255, 0, 0), "blue": (166, 230, 255),
          "snake_body":(112, 79, 232), "snake_head":(84, 56, 186)}


SCR_WIDTH = 1000
SCR_HEIGHT = 720
GAME_NAME = "Mr Philip's Snake Game"
GAME_ICON = "snake_icon.png"
REFRESH_RATE = 10
FONT = pygame.font.SysFont("arialblack", 20)
WELCOME = "Welcome to Mr P's Snake Game. Press 'SPACEBAR' to start."
END_GAME = "You have died. Game Over."
PLAY_AGAIN = "Press 'SPACEBAR' to play again. Press 'ESC' to quit."

screen = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pygame.display.set_icon(pygame.image.load(GAME_ICON))
pygame.display.set_caption(GAME_NAME)

snake_list = []
snake_length = 1 

def high_score_file(set_new, score):
    if set_new == False:
        snake_high_score = open("snake_score.txt", 'r')
        record = snake_high_score.read()
        snake_high_score.close()
        return record
    if set_new == True:
        hi_score_file = open("snake_score.txt", 'w')
        hi_score_file.write(str(score))
        hi_score_file.close()

def message(msg, txt_colour, bkgd_colour, x_pos, y_pos):
    txt = FONT.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center = (x_pos, y_pos))
    screen.blit(txt, text_box)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, colour["snake_body"], [x[0], x[1], 20, 20])
        if x == snake_list[-1]:
            pygame.draw.rect(screen, colour["snake_head"], [x[0], x[1], 20, 20])
            
def food_loc(pos):
    coordinate = round(random.randrange(20, pos-20)/20)*20
    return coordinate

def draw_food(food_x, food_y):
    food = pygame.Rect(food_x, food_y, 20, 20)
    apple = pygame.image.load("apple_3.png").convert_alpha()
    resized_apple = pygame.transform.smoothscale(apple, [20, 20])
    screen.blit(resized_apple, food)
   
def game_loop():   
    quit_game = True
    snake_x = 200
    snake_y = 200
    snake_x_change = 0
    snake_y_change = 0
    score = 0
    high_score = high_score_file(False, score)
    food_x = food_loc(SCR_WIDTH)
    food_y = food_loc(SCR_HEIGHT)

    while quit_game == True:
        screen.fill(colour["green"])
        message(WELCOME, colour["black"], colour["green"],
                (SCR_WIDTH/2),(SCR_HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quit_game = False

    while quit_game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
                elif event.key == pygame.K_LEFT:
                    snake_x_change = -20
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = 20
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -20
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = 20
                    
        screen.fill(colour["white"])
        snake_x += snake_x_change
        snake_y += snake_y_change

        draw_food(food_x, food_y)

        if (snake_x >= SCR_WIDTH or snake_x < 0 or
        snake_y >= SCR_HEIGHT or snake_y < 0):
            screen.fill(colour["red"])
            message(END_GAME, colour["black"], colour["red"],
                (SCR_WIDTH/2),(SCR_HEIGHT/2))
            pygame.display.update()
            time.sleep(3)
            quit_game = True
        
        if snake_x == food_x and snake_y == food_y:
            snake_list.append(snake_head)
            food_x = food_loc(SCR_WIDTH)
            food_y = food_loc(SCR_HEIGHT)
            score += 1
            print(score)

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)   
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                quit_game= True
        draw_snake(snake_list)
        
        message("Score: " + str(score), colour["black"],colour["white"],50,20)
        message("High Score: " + str(high_score),
                colour["black"],colour["white"],(SCR_WIDTH-80),20)

        pygame.display.update()
        clock.tick(REFRESH_RATE)
        
    #End of While Loop. Start of End Game.

    if score > int(high_score):
        high_score_file(True, score)
        screen.fill(colour["blue"])
        message("New High Score: " + str(score),
                colour["black"],colour["blue"],(SCR_WIDTH/2),(SCR_HEIGHT/3))
        pygame.display.update()
        time.sleep(3)
        
    while quit_game == True:
        screen.fill(colour["green"])
        message(PLAY_AGAIN, colour["black"], colour["green"],
                (SCR_WIDTH/2),(SCR_HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
    
    
    

game_loop()

