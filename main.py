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

def text_rect(title_rect, k):
    return title_rect.get_rect(center = (size / 2, size / 2 + k * cell_size))

#create menu
class Menu(Game):
    def __init__(self):
        Game.__init__(self)
        #define font
        self.menu_text = title_font.render(f"Menu", True, WHITE)
        self.start_btn = pg.transform.scale(start_img, (80, 80))
        self.exit_btn = pg.transform.scale(exit_img, (80, 80))

        #text rectangels
        self.menu_rect = text_rect(self.menu_text, -2)
        self.start_rect = text_rect(self.start_btn, 2)
        self.exit_rect = text_rect(self.exit_btn, 5)

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

class GameOver():
    def __init__(self):
        # Game.__init__(self)

        self.game_over_text = title_font.render(f"Game over", True, WHITE)
        self.game_over_rect = self.game_over_text.get_rect(center = (size / 2, size / 2 + OFFSET))

    def display(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            screen_over.fill(BLACK)
            screen_over.blit(self.game_over_text, self.game_over_rect)
            pg.display.update()

over = GameOver()
game = Game()
menu = Menu()

SNAKE_UPDATE = pg.USEREVENT
pg.time.set_timer(SNAKE_UPDATE, 200)

#game launch
while True:
    #menu
    if menu.running_menu == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                menu.is_clicked()
        screen.blit(background, (0, 0))
        menu.update()
        pg.display.update()
    #play screen
    else:   
        for event in pg.event.get():
            if event.type == SNAKE_UPDATE:
                game.update()
                if game.gameover == True:
                    over.display()
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

            pg.draw.rect(screen, DARK_GREEN, (OFFSET, OFFSET, size - OFFSET, size - OFFSET), 3)
            # pg.display.flip()

            #draw border

            #draw food + snake
            game.draw()

            #show score
            score = font.render(f"Score : {str(game.score)}", True, DARK_GREEN)
            screen.blit(score, (0,0))

            pg.display.update()

            clock.tick(15)
