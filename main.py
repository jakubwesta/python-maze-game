import pygame as pg
import sys
import time
from os import path
from settings import *
from sprites import *

LEVEL = 1
RESTARTED = 0

def draw_time(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    fill_rect_no = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    
    col = (200 - pct * 200, pct * 200, 0)
    
    pg.draw.rect(surf, WHITE, fill_rect_no)
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

def draw_points(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x + 100 + 2 * x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x + 100 + 2 * x, y, fill, BAR_HEIGHT)
    fill_rect_no = pg.Rect(x + 100 + 2 * x, y, BAR_LENGTH, BAR_HEIGHT)
    
    col = (0, 0, 255)
    
    pg.draw.rect(surf, WHITE, fill_rect_no)
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        global LEVEL
        self.level = LEVEL
        self.load_data()

    def __del__(self):
        initalize
        pass

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        self.score_value = 0
        with open(path.join(game_folder, 'map' + str(LEVEL) + '.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ghosts = pg.sprite.Group()
        self.points = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == '2':
                    Point(self, col, row)
                if tile == 'g':
                    Ghost(self, col, row, self.level)

    def run(self):
        self.playing = True
        self.level_settings()
        self.time_start = time.time()

        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.check_points()
            self.events()
            self.update()
            self.hits = pg.sprite.spritecollide(self.player, self.points, False)
            if self.hits:
                print("TEST")
                self.points.destroy_point
                
            self.draw()

    def level_settings(self):
        if self.level == 1:
            self.time_level = 25
            self.level_points_max = 15
        elif self.level == 2:
            self.time_level = 35
            self.level_points_max = 25
        elif self.level == 3:
            self.time_level = 35
            self.level_points_max = 25
        elif self.level == 4:
            self.time_level = 35
            self.level_points_max = 25
        elif self.level == 5:
            self.time_level = 35
            self.level_points_max = 25

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def check_points(self):
        if self.player.POINTS >= self.level_points_max:
            global LEVEL
            global LEVEL_AMOUNT
            LEVEL += 1
            if LEVEL > LEVEL_AMOUNT:
                self.game_finished()
            else:
                self.restart()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        #self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.time_end = time.time()
        self.time_current = self.time_end - self.time_start
        if (1 - self.time_current / self.time_level) >= 0:
            draw_time(self.screen, 5, 5, 1 - self.time_current / self.time_level)
            draw_points(self.screen, 5, 5, self.player.POINTS / self.level_points_max)
        else:
            if RESTARTED == 0:
                initalize_2()
            else:
                initalize()
        #print(self.time_end - self.time_start)
        #print(self.player.POINTS)
        #print(self.player.POINTS)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.restart()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def restart(self):
        if RESTARTED == 0:
            initalize_2()
        else:
            initalize()
        
    def game_finished(self):
        print("FINISHED")
        self.quit()
        pass   

def initalize_2():
    try:
        del g
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()
    except:
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()

def initalize():
    try:
        del g
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()
    except:
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()      



initalize()

