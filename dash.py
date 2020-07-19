#!/usr/bin/env python3
import datetime
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import init
from color_names import *

options = init.get_options()
canvas = RGBMatrix(options=options)

clockFont = graphics.Font()
clockFont.LoadFont("fonts/tom-thumb.bdf")

msgFont = graphics.Font()
msgFont.LoadFont("fonts/clR6x12.bdf")

while True:
    graphics.DrawText(canvas, clockFont, 4, 5, gray, str(datetime.datetime.now().strftime("%H:%M:%S")))
    graphics.DrawText(canvas, msgFont, 4, 20, dim_gray, "Line 2")
    time.sleep(0.1) 
    canvas.Clear()


