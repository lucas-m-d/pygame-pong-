import pygame as pg

WHITE = (255, 255, 255)
# paddle is the thing which the player moves

class Paddle(pg.sprite.Sprite):
    def __init__(self, colour, size):

        pg.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.width = 150
        self.height = 10
        self.image = pg.Surface([self.width, self.height])
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        self.image.fill(colour)
        

    def move_left(self):        
        if self.x == 0:
            self.x = 700
        else:
            self.x -= 10
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))

    def move_right(self):
        self.x += 10
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))

    # after adding score
    def update(self):
        self.image = pg.Surface([self.width, self.height])
    