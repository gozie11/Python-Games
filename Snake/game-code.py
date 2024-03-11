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
    pass
def redrawWindow(surface):
    pass