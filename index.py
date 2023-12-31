import pygame as pg
import sys
from pygame.math import Vector2

pg.init()

#RBG
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#create grid
cell_size = 30
number_of_sizes = 20
size = cell_size * number_of_sizes

#input size
input_rect = pg.Rect(100, 100, 20, 20)

#ofFset
OFFSET = 30

#font
title_font = pg.font.Font("Asset/font.ttf", 60)
font = pg.font.Font("Asset/font.ttf", 20)

#button
start_img = pg.image.load("Asset/start_btn.png")
exit_img = pg.image.load("Asset/exit_btn.png")

# screen
screen = pg.display.set_mode((size + OFFSET, size + OFFSET))
screen_over = pg.display.set_mode((size + OFFSET, size + OFFSET))

# food
food_surface = pg.image.load("Asset/food.png")

# background
background = pg.image.load("Asset/Background.png")

#border
