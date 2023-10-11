
# PONG
# Jason, Beer License
# 10/10/23

import pygame, time, random
from pygame.locals import *

pygame.init()

# Variables
ScreenWidth = 800
ScreenHeight = 600

BallX = random.randint(300,500)
BallY = random.randint(100,500)
BallLocation = (BallX, BallY)
BallSize = 10
BallHalf = BallSize/2
dx = random.choice([-3,3])
dy = random.choice([-3,3])

RPaddleX = 770
RPaddleY = 100
RPaddleW = 20
RPaddleH = 80
RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)
RPaddleUpOrDown = 0

LPaddleX = 10
LPaddleY = 100
LPaddleW = 20
LPaddleH = 80
LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)
LPaddleUpOrDown = 0

LeftScore = 0
RightScore = 0

# Constant
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
GRAY = (128,128,128)

# Create a Window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
MyFont = pygame.font.SysFont(None, 100)
MySmallFont = pygame.font.SysFont(None, 40)
Message = ''

CenterOfScreen = ScreenWidth / 2
NetWidth = 10
LeftSideOfNet = CenterOfScreen - (NetWidth / 2)
BottomofScreen = ScreenHeight - 10

BallStopped = False
NewGame = False

# Standard PyGame Game Loop (While, for and if)
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        # Keyboard Events
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                RPaddleUpOrDown = 3
            if event.key == K_UP:
                RPaddleUpOrDown = -3
            if event.key == K_SPACE:
                if BallStopped == True:
                    dx = random.choice([-3,3])
                    dy = random.choice([-3,3])
                    BallX = random.randint(300,500)
                    BallY = random.randint(100,500)
                    BallStopped = False
                    Message = ''
            if event.key == K_n:
                if BallStopped == True:
                    dx = random.choice([-3,3])
                    dy = random.choice([-3,3])
                    BallX = random.randint(300,500)
                    BallY = random.randint(100,500)
                    BallStopped = False
                    Message = ''
                    LeftScore = 0
                    RightScore = 0

        if event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_UP:
                RPaddleUpOrDown = 0

    BallX += dx
    BallY += dy
    BallLocation = (BallX, BallY)

    # Bounce Code
    if BallY > ScreenHeight - BallHalf or BallY < BallHalf:
         dy *= -1

    # Ball goes off right side.
    if BallX > ScreenWidth - BallHalf:
         RightScore += 1
         BallStopped = True

    # Ball goes off left side.
    if BallX < BallHalf:
         LeftScore += 1
         BallStopped = True

    if BallStopped == True: # Stops the ball.
         dx = 0
         dy = 0
         BallX = ScreenWidth/2
         BallY = ScreenHeight/2
         Message = 'Press SPACE to continue.'
         if RightScore == 10 or LeftScore == 10:
              Message = 'Game Over! Press N for new game.'

    # Collision Detection
    if BallX + BallHalf > RPaddleX and \
        BallY > RPaddleY and \
        BallY < RPaddleY + RPaddleH:
            dx *= -1

    if BallX - BallHalf < LPaddleX + LPaddleW and \
        BallY > LPaddleY and \
        BallY < LPaddleY + RPaddleH:
            dx *= -1

    screen.fill(GREEN)

    TextImg = MyFont.render(str(RightScore), True, BLUE, GREEN)
    screen.blit(TextImg, (430,10))
    TextImg = MyFont.render(str(LeftScore), True, RED, GREEN)
    screen.blit(TextImg, (290,10))

    pygame.draw.rect(screen, WHITE, (LeftSideOfNet, 0, NetWidth, ScreenHeight))
    pygame.draw.rect(screen, BLACK, (LeftSideOfNet, 0, NetWidth,10))
    pygame.draw.rect(screen, BLACK, (LeftSideOfNet, BottomofScreen, NetWidth,10))
    pygame.draw.rect(screen, BLUE, (RPaddle))
    pygame.draw.rect(screen, RED, (LPaddle))

    RPaddleY += RPaddleUpOrDown
    RPaddle = (RPaddleX, RPaddleY, RPaddleW, RPaddleH)

    if BallY > LPaddleY + LPaddleH/2:
        LPaddleY += random.randint(-1,5)
    else:
        LPaddleY -= random.randint(-1,5)

    LPaddle = (LPaddleX, LPaddleY, LPaddleW, LPaddleH)

    pygame.draw.circle(screen, YELLOW, BallLocation, BallSize, BallSize)

    TextImg = MySmallFont.render(Message, True, WHITE, GRAY)
    screen.blit(TextImg, (200,200))

    pygame.display.update()
    time.sleep(0.01)
# End of the While Loop
print("Game Over")
pygame.quit()