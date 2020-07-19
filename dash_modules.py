#!/usr/bin/env python3
from rgbmatrix import graphics
import color_names


class dash_widget(object):
    x1 = None
    y1 = None

    x2 = None
    y2 = None

    def __init__(x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def run():
        """ Please Override Me """
        pass

class clock(dash_widget):
    color = 
    def run():
        
