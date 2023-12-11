import pygame as pg
import sys
from pygame.math import Vector2

pg.init()

#RBG
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
WHITE = (255, 255, 255)

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
font = pg.font.Font("Asset/font.ttf", 40)

#button
start_img = pg.image.load("Asset/start_btn.png")

screen = pg.display.set_mode((size, size))

food_surface = pg.image.load("Asset/food.png")