import pygame as pg
import sys
from pygame.math import Vector2
from random import randint
from index import *
from snake import *

class Food(Snake):
    def __init__(self):
        Snake.__init__(self)

        self.position = self.generate_random_position()

    def draw(self):
        food_rect = (self.position.x * cell_size + OFFSET, self.position.y * cell_size + OFFSET, cell_size, cell_size)    
        screen.blit(food_surface, food_rect)
    
    def generate_random_position(self):
        x = randint(0, number_of_sizes - 2)
        y = randint(0, number_of_sizes - 2)
        position = Vector2(x, y)
        return position

    def reset(self):
        x = randint(0, number_of_sizes - 2)
        y = randint(0, number_of_sizes - 2)
        position = Vector2(x, y)
        return position