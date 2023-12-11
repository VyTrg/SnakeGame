import pygame as pg

from random import randint
from food import Food
from snake import Snake
from game import Game
from index import *

pg.init()

#display
#(widht, height)
pg.display.set_caption("Snake")

#fps
clock = pg.time.Clock()

def get_text_func(font_name, name):
    return {}.format(font_name).render(f"{name}", True, WHITE)

#create menu
class Menu(Game):
    def __init__(self):
        Game.__init__(self)
        #define font
        self.menu_text = title_font.render(f"Menu", True, WHITE)
        self.start_btn = pg.transform.scale(start_img, (80, 80))
        # self.play_text = font.render("Play", True, WHITE)
        # self.record_text = font.render("Record", True, WHITE)
        # self.quit_text = font.render("Quit", True, WHITE)

        #text rectangels
        self.menu_rect = self.menu_text.get_rect(center = (size / 2, size / 2 - 2 * cell_size))
        # self.play_rect = self.play_text.get_rect(center = (size / 2, size / 2 + 2 * cell_size))
        # self.record_rect = self.record_text.get_rect(center = (size / 2, size / 2 + 4 * cell_size))
        # self.quit_rect = self.quit_text.get_rect(center = (size / 2, size / 2 + 6 * cell_size))
        self.start_rect = self.start_btn.get_rect(center = (size / 2, size / 2 + 2 * cell_size))

        # self.rect = start_img.get_rect()
        #set up background
        # self.background = pg.image.load("Asset/Background.png")
    def update(self):
        #screen blit center for text
        screen.blit(self.menu_text, self.menu_rect)
        # screen.blit(self.play_text, self.play_rect)
        # screen.blit(self.record_text, self.record_rect)
        # screen.blit(self.quit_text, self.quit_rect)
        # self.background = pg.transform.scale(self.background, (size, size))
        screen.blit(self.start_btn, self.start_rect)
    
    def is_clicked(self):
        pos = pg.mouse.get_pos()
        
        if self.start_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.running_menu = False
                # print("Clicked")



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
            if event.type == pg.MOUSEMOTION:
                # x_mouse, y_mouse = pg.mouse.get_pos()
                menu.is_clicked()
                # print(pg.mouse.get_pos())
                
        # screen.fill(WHITE)
        menu.update()
        # screen.blit(menu.play_text, menu.play_rect)
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
            #                 (OFFSET - 10, OFFSET - 10, size, size))

            #draw food + snake
            game.draw()

            #show score
            score = font.render(f"Score : {str(game.score)}", True, DARK_GREEN)
            screen.blit(score, (10, 10))

            pg.display.update()

            clock.tick(15)
