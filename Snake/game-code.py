# It's a good idea to learn how to use pygame to create a game
# https://www.pygame.org/wiki/about

# The game is a simple snake game, where the snake has to eat the food and grow

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    row = 0
    w = 0  
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)) -> None:
        pass
    def move(self, dirnx, dirny) -> None:
        pass
    def draw(self, surface, eyes=False) -> None:
        pass

class snake(object):
    def __init__(self, color, pos) -> None:
        pass

    def move(self) -> None:
        pass

    def reset(self, pos) -> None:
        pass
    def addCube(self) -> None:
        pass

    def draw(self, surface) -> None:
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass    

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    height = 500
    rows = 20 # this should be 500 divisible. Make it smaller to make the game harder
    win = pygame.display.set_mode((width, height))

    s = snake((255,0,0), (10,10))
    flag = True

    # COOL STUFF
    #this makes sure our game runs at 10 frames per second
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)# lower this for a faster game
        clock.tick(10) # lower this for a slower game
        redrawWindow(win)

# I guess the next line is the most important line in the code because it starts the game
        
main()
