import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
gg = True
dd = pygame.image.load('icon.png')
ddd = pygame.image.load('2icon.png')
xcor = 400
ycorr = 200
changex = 0
changey = 0
ex=random.randint(0, 750)
ey=random.randint(0, 550)


def player(x, y):
    screen.blit(dd, (xcor, ycorr))



def enemy(x,y):
    screen.blit(ddd,(ex,ey))


while gg:
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gg = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex = -.2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changex = .2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changey = -.2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                changey = .2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changex = 0
                changey = 0

    xcor += changex
    ycorr += changey
    if xcor <= 0:
        xcor = 0

    elif xcor >= 650:
        xcor = 650

    elif ycorr < 24:

        ycorr = 24
    elif ycorr >= 550:
        ycorr = 550

    enemy(ex,ey)
    player(xcor, ycorr)
    jj=ex-xcor
    kk=ey-ycorr
    distance=math.sqrt(math.pow(jj,2)+math.pow(kk,2))
    if distance<27:
       ex=random.randint(0, 650)
       ey=random.randint(0, 550)

    pygame.display.update()
