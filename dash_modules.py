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
        draw_square(self.canvas, self.x1, self.y1, self.x2, self.y2, color)

    def run(self):
        """ Please Override Me """
        pass

class histogram(dash_widget):
    history = []
    def map(self, num):
        """ 
            Translates the given num (assumed to be % of 100) into
            an appropriate number for the height of the current 
            histogram. 
        """
        height = self.y2 - self.y1
        return height/(100/num)

    def run(self):
        base_point = (self.x2, self.y1)
        x = base_point[0]
        for item in self.history:
            print("Drawing line at %s, %s" % (x, base_point[1]))
            graphics.DrawLine(self.canvas, 
                x, base_point[1], 
                x, base_point[1] + self.map(item['value']), item['color'])
            x -= 1
        length = self.x2 - self.x1
        if len(self.history) > length:
            self.history.pop(0)

    def update_data(self, hist):
        self.history.append(hist)

class label(dash_widget):
    def text(self, text):
        graphics.DrawText(self.canvas, self.font, self.x1, self.y2, self.color, text)

class clock(dash_widget):

    def run(self):
        graphics.DrawText(self.canvas, self.font, self.x1, self.y2, self.color, str(datetime.now().strftime("%H:%M:%S")))

class current_status(dash_widget):
    color = dim_magenta

    def run(self):
        self.show_box(gray)
        fill_square(self.canvas, self.x1, self.y1, self.x2, self.y2, self.color)
        

    def set_status(self, status):
        if status == "OK":
            self.color = dim_green
        elif status == "WARN":
            self.color = dim_yellow
        elif status == "CRITICAL":
            self.color = red
        else:
            self.color = dim_magenta
