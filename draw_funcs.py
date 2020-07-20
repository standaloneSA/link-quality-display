#!/usr/bin/env python3 
from rgbmatrix import graphics

def draw_square(canvas, x1, y1, x2, y2, color):
    graphics.DrawLine(canvas, x1, y1, x2, y1, color)
    graphics.DrawLine(canvas, x2, y1, x2, y2, color)
    graphics.DrawLine(canvas, x2, y2, x1, y2, color)
    graphics.DrawLine(canvas, x1, y1, x1, y2, color)

def fill_square(canvas, x1, y1, x2, y2, color):
    x = x1
    while x <= x2:
        graphics.DrawLine(canvas, x, y1, x, y2, color)
        x += 1
   
    
    
