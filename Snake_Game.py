"""This file is a simple snake game.

Similar to what used to be found on the old Nokia phones.
Snake needs to eat apple to get bigger and score higher.
"""

import pygame
import time
import random

# Set up game constants and settings
pygame.init()
clock = pygame.time.Clock()
color = {"white": (255, 255, 255), "green": (188, 227, 199),
         "black": (0, 0, 0), "red": (255, 0, 0), "blue": (166, 230, 255),
         "body": (112, 79, 232), "head": (84, 56, 186)}

SCR_WIDTH = 1000
SCR_HEIGHT = 720
GAME_NAME = "Mr Philip's Snake Game"
GAME_ICON = "snake_icon.png"
REFRESH_RATE = 10
FONT = pygame.font.SysFont("arialblack", 20)
WELCOME = "Welcome to Mr P's Snake Game. Press 'SPACEBAR' to start."
END_GAME = "You have died. Game Over."
PLAY_AGAIN = "Press 'SPACEBAR' to play again. Press 'ESC' to quit."
DELAY = 3

screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_icon(pygame.image.load(GAME_ICON))
pygame.display.set_caption(GAME_NAME)

snake_list = []
snake_length = 1


def high_score_file(set_new, score):
    """Read and write to the file storage for high score."""
    if set_new is False:  # Check file for high score
        snake_high_score = open("snake_score.txt", 'r')
        record = snake_high_score.read()
        snake_high_score.close()
        return record
    if set_new is True:  # Write new high score to file
        hi_score_file = open("snake_score.txt", 'w')
        hi_score_file.write(str(score))
        hi_score_file.close()


def message(msg, txt_color, bkgd_color, x_pos, y_pos):
    """Create new messages to show on the screen."""
    txt = FONT.render(msg, True, txt_color, bkgd_color)
    text_box = txt.get_rect(center=(x_pos, y_pos))
    screen.blit(txt, text_box)


def draw_snake(snake_list):
    """Iterate through the list to create a chain of rectangles for snake."""
    for x in snake_list:
        pygame.draw.rect(screen, color["body"], [x[0], x[1], 20, 20])
        if x == snake_list[-1]:  # Change color of last item to make head
            pygame.draw.rect(screen, color["head"], [x[0], x[1], 20, 20])


def food_loc(pos):
    """Generate random numbers for x and y axis."""
    coordinate = round(random.randrange(20, pos-20)/20)*20
    return coordinate


def draw_food(food_x, food_y):
    """Create rectangle and layer image of food over it."""
    food = pygame.Rect(food_x, food_y, 20, 20)
    apple = pygame.image.load("apple_3.png").convert_alpha()
    resized_apple = pygame.transform.smoothscale(apple, [20, 20])
    screen.blit(resized_apple, food)


def game_loop():
    """Set up game for replay."""
    quit_game = True

    # Set basics such as snake location and movement
    snake_x = 200
    snake_y = 200
    snake_x_change = 0
    snake_y_change = 0
    score = 0
    high_score = high_score_file(False, score)  # Get high score from file
    food_x = food_loc(SCR_WIDTH)
    food_y = food_loc(SCR_HEIGHT)

    while quit_game is True:
        # Screen to hold player at until they are ready
        screen.fill(color["green"])
        message(WELCOME, color["black"], color["green"],
                (SCR_WIDTH/2), (SCR_HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quit_game = False

    while quit_game is False:
        # Main game loop to run, loop speed based of clock.ticks rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Checks for player input using keys
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

        screen.fill(color["white"])
        snake_x += snake_x_change  # Moves snake based off keys
        snake_y += snake_y_change

        draw_food(food_x, food_y)  # Uses function to make food show

        if SCR_WIDTH >= snake_x < 0 or SCR_HEIGHT >= snake_y < 0:
            # Checks bounds of game and if snake within them.
            print("Out of bounds")  # Check functioning in console.
            screen.fill(color["red"])
            message(END_GAME, color["black"], color["red"],
                    (SCR_WIDTH/2), (SCR_HEIGHT/2))
            pygame.display.update()
            time.sleep(3)
            quit_game = True

        # If location of snake and food match, snake eats food
        # Snake list gets longer. New food made.
        if snake_x == food_x and snake_y == food_y:
            snake_list.append(snake_head)
            food_x = food_loc(SCR_WIDTH)
            food_y = food_loc(SCR_HEIGHT)
            score += 1
            print("Food eaten")  # Check functioning in console.

        # Sets coordinates for snake pieces in snake_list list
        # Checks whether snake location is in list. If yes, hits itself.
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                quit_game = True
        draw_snake(snake_list)

        # Displays score and high score up top of game.
        message("Score: " + str(score), color["black"], color["white"], 50, 20)
        message("High Score: " + str(high_score),
                color["black"], color["white"], (SCR_WIDTH-80), 20)

        # Update the screen. Start loop again.
        pygame.display.update()
        clock.tick(REFRESH_RATE)

    # End of loop. Checks score against high score.
    if score > int(high_score):
        high_score_file(True, score)  # Update score on file if new one larger.
        screen.fill(color["blue"])
        message("New High Score: " + str(score),
                color["black"], color["blue"], (SCR_WIDTH/2), (SCR_HEIGHT/3))
        pygame.display.update()
        time.sleep(3)

    while quit_game is True:
        # Give user choice to play again or quit game.
        screen.fill(color["green"])
        message(PLAY_AGAIN, color["black"], color["green"],
                (SCR_WIDTH/2), (SCR_HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


# Initiates main game loop
game_loop()
