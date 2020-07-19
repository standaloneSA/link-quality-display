#!/usr/bin/env python3 
from rgbmatrix import graphics

def fill_square(canvas, x1, y1, x2, y2, color):
    x = x1
    while x <= x2:
        graphics.DrawLine(canvas, x, y1, x, y2, color)
        x += 1
   
    
    
