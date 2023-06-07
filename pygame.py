import pygame
import random
# initializaing pygame
pygame.init()

# colors
white = (255, 255, 255) # rgb format 
red = (255, 0, 0)
black = (0, 0, 0)

# creating window 
screen_width = 900
screen_height = 600
gameWiondow = pygame.distray.set_mode((secreen_widh, screen_height))

# game Title
pygame.distray.set_caption("codern home")
pygame.distray.update()
clock= pygame.time.clock()
font = pygame.distray.set_mode( (screen_width, screen_height))

def text_screen(text, color, x, y):
    screen_text = font.render(text, true, color)
    gameWindow.blit(screen_text, [X,Y])
    def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, ^[x, y, snake_size, snake_size])

# game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = B
    snk_list = []
    snk_length = 1

    food_x