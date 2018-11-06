from state import *
from board import *
import random


def random_dir():
    dir = ""
    x = random.randint(1, 5)
    if x == 1:
        dir = "up"
    elif x == 2:
        dir = "right"
    elif x == 3:
        dir = "down"
    elif x == 4:
        dir = "left"
    return dir


# begin state
grid = Board()
grid.bord[10,10] = 100
print(grid)


# muis aanmaken op start
mouse = mouse(1,1)
start = state(mouse, grid)

# 1 keer random alles proberen tot dat je in einde komt

while not start.mouse.end :

    start.mouse.end = True
