import pygame
from paddle import *
from ball import *
import time


pygame.init()
pg = pygame 
# this just makes it simpler.  Instead of writing pygame, we can just say pg

# declare global variables
# colours are made up of certain values for different colours: red green and blue.  The value can go up to 255

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = BLACK

#700 is a good size for our project
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
'''
this is a tuple - like a list, but you can't modify it - only read
most people use tuples when in pygame.  This is because you can't edit tuples.
if we were to use a list, we could accidentally change it.  
'''

#let's create our display and give it a caption

display = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Pong!")

#clock just because it will control our refresh rate
clock = pg.time.Clock()


# create the sprites
paddle = Paddle(WHITE, (50, 50))
paddle.x = (0.5 * SCREEN_HEIGHT) - (0.5 * paddle.width)
paddle.y = SCREEN_WIDTH - paddle.height

ball = Ball()


gameOver = False # <--- False is a Boolean value (named after British scientist George Boole)

score = 0

score_surface = pg.font.SysFont("Montserrat", 50)
score_surface_render = score_surface.render(f'score: {score}', True, WHITE)

#spot the boolean operator in the next line


def play():
    score = 0
    ticker = 60
    gameOver = False
    while not gameOver:
        # while is iteration - it's a loop
        # as long as gameOver is False, it will run the following code.
        
        keys = pg.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()


        for event in pg.event.get(): 
            if event.type == pg.QUIT: # if you click the x in the corner, then quit the game
                gameOver = True 
                pg.quit()       
        
        
        # set this colour at the top - we'll use black in this case
        display.fill(BACKGROUND_COLOR)
        display.blit(paddle.image, (paddle.x, paddle.y))
        


        #display.blit(score_surface_render, (50, 50))

        #ball collision checker
        collided = ball.checkCollision(paddle)
        if collided:
            ball.collide = True
            score += 1
            ball.velocity_y += 0.2
        else:
            ball.collide = False

        ball.move() 
        if ball.y >= SCREEN_HEIGHT:
            break
        
        


        display.blit(ball.image, (ball.x, ball.y))    

        clock.tick(60) # limit to 60 fps - we don't want more or it would be uncontrollable!
        pg.display.flip()
    return score

score = play()

lastscreen = True
time.sleep(1)

while lastscreen:
    paddle.x = (0.5 * SCREEN_HEIGHT) - (0.5 * paddle.width)
    paddle.y = SCREEN_WIDTH - paddle.height
    ball = Ball()

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        score = play()
        

    for event in pg.event.get(): 
        if event.type == pg.QUIT: # if you click the x in the corner, then quit the game
              pygame.quit()

    display.fill(BACKGROUND_COLOR)
    score_surface_render = score_surface.render(f'score: {score}', True, WHITE)


    gg = score_surface.render(f'Good game!', True, WHITE)
    gg_wh = (gg.get_width(), gg.get_height())
    gg_coords = (350 - gg_wh[0]//2, 350 - gg_wh[1]//2)

    display.blit(score_surface_render, (0, 0))
    display.blit(gg, gg_coords)

    clock.tick(60)
    pg.display.flip()

pygame.quit()
