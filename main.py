import pygame as pg

from random import randint
from food import Food
from snake import Snake
from game import Game
from index import *

pg.init()

pg.display.set_caption("Snake")

#fps
clock = pg.time.Clock()

#create menu
class Menu(Game):
    def __init__(self):
        Game.__init__(self)
        #define font
        self.menu_text = title_font.render(f"Menu", True, WHITE)
        self.start_btn = pg.transform.scale(start_img, (80, 80))
        self.exit_btn = pg.transform.scale(exit_img, (80, 80))

        #text rectangels
        self.menu_rect = self.menu_text.get_rect(center = (size / 2, size / 2 - 2 * cell_size))
        self.start_rect = self.start_btn.get_rect(center = (size / 2, size / 2 + 2 * cell_size))
        self.exit_rect = self.exit_btn.get_rect(center = (size / 2, size / 2 + 5 * cell_size))

        #background
    def update(self):
        #screen blit center for text
        screen.blit(self.menu_text, self.menu_rect)
        screen.blit(self.start_btn, self.start_rect)
        screen.blit(self.exit_btn, self.exit_rect)
    
    def is_clicked(self):
        pos = pg.mouse.get_pos()
        
        if self.start_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.running_menu = False
                # print("Clicked")

        if self.exit_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                pg.quit()
                sys.exit()



game = Game()
menu = Menu()

SNAKE_UPDATE = pg.USEREVENT
pg.time.set_timer(SNAKE_UPDATE, 200)

#game launch
while True:
    if menu.running_menu == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                
                menu.is_clicked()
                
        menu.update()
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

            #draw food + snake
            game.draw()

            #show score
            score = font.render(f"Score : {str(game.score)}", True, DARK_GREEN)
            screen.blit(score, (10, 10))

            pg.display.update()

            clock.tick(15)
