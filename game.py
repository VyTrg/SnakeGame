import pygame as pg

from random import randint
from food import Food
from snake import Snake
from index import *

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.state = "Running"
        self.score = 0
        self.running_menu = True

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        if self.state == "Running":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_wall()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.score = self.score + 1
            del self.food.position
            self.snake.body.insert(0, self.snake.body[0] + self.snake.direction)
            self.food.position = self.food.generate_random_position()
    
    def check_collision_with_wall(self):
        if self.snake.body[0].x >= number_of_sizes - 1 or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y >= number_of_sizes - 1 or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()       
        self.food.reset() 
        self.state = "Stopped"
        self.score = 0
        self.running_menu = True