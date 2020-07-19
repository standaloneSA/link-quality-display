#!/usr/bin/env python3
import sys
from rgbmatrix import graphics
from color_names import *
from datetime import datetime
from draw_funcs import *

class dash_widget(object):
    x1 = None
    y1 = None

    x2 = None
    y2 = None

    canvas = None

    def __init__(self, x1, y1, x2, y2, canvas=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.font = graphics.Font()
        self.color = gray
        # displays are small. Lets default to this.
        self.font.LoadFont("fonts/tom-thumb.bdf")

    def set_font(self,name):
        try:
            self.font.LoadFont("fonts/%s.bdf" % name)
        except Exception as err:
            print("Error loading font: %" % str(err))
            sys.exit(1)

    def show_box(self, color=white):
        graphics.DrawLine(self.canvas, self.x1, self.y1, self.x2, self.y1, color)
        graphics.DrawLine(self.canvas, self.x2, self.y1, self.x2, self.y2, color)
        graphics.DrawLine(self.canvas, self.x2, self.y2, self.x1, self.y2, color)
        graphics.DrawLine(self.canvas, self.x1, self.y1, self.x1, self.y2, color)

    def run(self):
        """ Please Override Me """
        pass

class clock(dash_widget):

    def run(self, canvas):
        graphics.DrawText(self.canvas, self.font, self.x1, self.y2, self.color, str(datetime.now().strftime("%H:%M:%S")))

class current_status(dash_widget):
    color = dim_magenta

    def run(self):
        self.show_box(gray)
        fill_square(self.canvas, self.x1, self.y1, self.x2, self.y2, self.color)
        

    def set_status(self, status):
        if status == "OK":
            self.color = green
        elif status == "WARN":
            self.color = yellow
        elif status == "CRITICAL":
            self.color = red
        else:
            self.color = dim_magenta
   
class histogram(dash_widget):
    def run(self): 
        pass
