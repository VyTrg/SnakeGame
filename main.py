import pygame as pg
import sys
from pygame.math import Vector2
from random import randint

pg.init()

#RBG
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
WHITE = (255, 255, 255)

#create grid
cell_size = 30
number_of_sizes = 20

#input size
input_rect = pg.Rect(100, 100, 20, 20)

#ofFset
OFFSET = 30

#display
screen = pg.display.set_mode((cell_size * number_of_sizes, 
                                cell_size * number_of_sizes))#(widht, height)
pg.display.set_caption("Snake")

#font
font = pg.font.Font(None, 30)


#fps
clock = pg.time.Clock()

#create FOOD
food_surface = pg.image.load("food.png")
class Food:
    def __init__(self):
        self.position = self.generate_random_position()

    def draw(self):
        food_rect = (self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        # pg.draw.rect(screen, DARK_GREEN, food_rect)
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

#create SNAKE
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)#Right

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pg.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)

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
        if self.snake.body[0].x >= number_of_sizes or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y >= number_of_sizes or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()       
        self.food.reset() 
        self.state = "Stopped"
        self.score = 0
        self.running_menu = True

class Menu(Game):
    def __init__(self):
        Game.__init__(self)

    

game = Game()
menu = Menu()
# food = Food()
# snake = Snake()

SNAKE_UPDATE = pg.USEREVENT
pg.time.set_timer(SNAKE_UPDATE, 200)

#game launch
while True:
    if menu.running_menu == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill(WHITE)
        pg.display.update()
    else:    
        for event in pg.event.get():
            if event.type == SNAKE_UPDATE:
                game.update()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and game.snake.direction != Vector2(0, 1):
                    game.snake.direction = Vector2(0, -1)
                elif event.key == pg.K_DOWN and game.snake.direction != Vector2(0, -1):    
                    game.snake.direction = Vector2(0, 1)
                elif event.key == pg.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                    game.snake.direction = Vector2(1, 0)
                elif event.key == pg.K_LEFT and game.snake.direction != Vector2(1, 0):
                    game.snake.direction = Vector2(-1, 0)
            
            screen.fill(GREEN)

            #draw border

            # pg.draw.rect(screen, DARK_GREEN, 
            #                 (OFFSET - 10, OFFSET - 10, cell_size * number_of_sizes, cell_size * number_of_sizes))

            #draw food + snake
            game.draw()

            #show score
            score = font.render(f"Score : {str(game.score)}", True, DARK_GREEN)
            screen.blit(score, (10, 10))

            pg.display.update()

            clock.tick(15)
