import pygame as pg
import sys
from pygame.math import Vector2
from random import randint
from index import *

class Food:
    def __init__(self):
        self.position = self.generate_random_position()

    def draw(self):
        food_rect = (self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)    
        screen.blit(food_surface, food_rect)
    
    def generate_random_position(self):
        x = randint(0, number_of_sizes - 1)
        y = randint(0, number_of_sizes - 1)
        position = Vector2(x, y)
        return position

    def reset(self):
        x = randint(0, number_of_sizes - 1)
        y = randint(0, number_of_sizes - 1)
        position = Vector2(x, y)
        return position