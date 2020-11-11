import pygame as pg
import random

WHITE = (255, 255, 255)
# ball - the ball :) 
# trickier to program as it needs vectors and collision logic

class Ball(pg.sprite.Sprite):
    def __init__(self):
        
        self.velocity_x = 5
        self.velocity_y = -5
        
        self.width = 10
        self.height = 10

        self.x = random.randint(0, 700)
        self.y = 10
        self.image = pg.Surface([self.width, self.height])
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))
        self.image.fill(WHITE)
        self.collide = False
    

    
    
    def move(self):
        if self.collide:
            self.velocity_x *= -1
            self.velocity_y *= -1

        if self.x <= 0 or self.x >= 700:
            self.velocity_x *= -1

        if self.y <= 0 or self.y >= 700:
            self.velocity_y *= -1
        


        self.x += self.velocity_x
        self.y += self.velocity_y
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))


    def checkCollision(self, other):
        collision = self.rect.colliderect(other.rect)
        if collision == True:
            chosen = random.choice([1, -1])
            if self.velocity_x < 0:
                self.velocity_x *= chosen
            else:
                self.velocity_x *= chosen
            return True
        else:
            return False