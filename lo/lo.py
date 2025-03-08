import random
from math import sin, cos, pi, log
from tkinter import *
CANVAS_WIDTH = 840
CANVAS_HEIGHT = 680
CANVAS_CENTER_X = CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
IMAGE_ENLARGE = 11
HEART_COLOR = "aquamarine"

def heart_fuunction(t, shrink_ratio: float = IMAGE_ENLARGE):
    x=17 * (sin(t) ** 3 )
    y = -(16* cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(3 * t))
    