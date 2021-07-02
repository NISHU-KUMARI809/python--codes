# install pygame by using command pip install  pygame  and then import pygame to make your game
import pygame
import time
import random
#     initializing pygame .
pygame.init()
# creating window
game_width = 800
game_height = 600
# adding desired colors .
orange = (255,165,0)
black =(0,0,0)
blue = (0,0,255)
green = (0,128,0)
red = (255,0,0)
white = (255,255,255)
gameWindow = pygame.display.set_mode((game_width,game_height))
# adding caption in the program .
pygame.display.set_caption('snake game')
pygame.display.update()
# snake block ..
block = 20
# snake speed .......
FPS = 10
clk = pygame.time.Clock()
# to add font in   game screen after   game is  over  with the text  message you lost !!!!!!!.....
font = pygame.font.SysFont(None,35)
# to make snakes...
def snake(block,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameWindow,blue,[XnY[0],XnY[1],block,block])
 # to add message and color in game screen after game is over .....
def message_to_screen(msg,color):
    Screen_text = font.render(msg,True,color)
    # to set the position of font ...
    gameWindow.blit(Screen_text,[game_width/4,game_height/2])
# creating a function ....
def loop():
    gameClose = False
    gameOver = False
# to add food in game window at random ......
    rApplex = round(random.randrange(0,game_width-block)/20.0)*20.0
    rAppley = round(random.randrange(0,game_height-block)/20.0) *20.0
    start_x = game_width/2
    start_y = game_height/2
    update_x = 0
    update_y = 0
# to increase  length of snake ...
    snakeList = []
    snakeLength = 1
    while not gameClose:
        while gameOver == True:
 # to add color in screen after game is over ...
            gameWindow.fill(white)
 #  to add message on gameover screen and color of the message font  ...
            message_to_screen("You loose!!!,press 'r' to replay or press 'q' to quit", red)
            pygame.display.update()
 # adding events .....
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event .key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    update_x = -block
                    update_y = 0
                if event.key == pygame.K_RIGHT:
                    update_x = +block
                    update_y = 0

                if event.key == pygame.K_UP:
                    update_y = -block
                    update_x = 0

                if event.key ==pygame.K_DOWN:
                    update_y = +block
                    update_x = 0

            if start_x >= game_width or start_x < 0 or start_y >= game_height or start_y<0:
                gameOver = True

        start_x += update_x
        start_y += update_y
# to add color on game window .......
        gameWindow.fill(green)
# to add shape of your snake ......
        pygame.draw.rect(gameWindow,red,[rApplex,rAppley,block,block])
# to increase length of snake when they eat there food .....
        snakeHead = []
        snakeHead.append(start_x)
        snakeHead.append(start_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del(snakeList[0])
            for eachSegment in snakeList [:-1]:
                if eachSegment == snakeHead:
                    gameOver = True
            snake(block,snakeList)

        pygame.display.update()
        if start_x == rApplex and start_y == rAppley:
            rApplex = round(random.randrange(0,game_width-block)/20.0)*20.0
            rAppley = round(random.randrange(0,game_height-block)/20.0)*20.0
            snakeLength += 1
        clk.tick(FPS)

    pygame.quit()

    quit()

loop()
