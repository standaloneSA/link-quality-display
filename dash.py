#!/usr/bin/env python3
import datetime
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import init
from color_names import *
import dash_modules

options = init.get_options()
root_canvas = RGBMatrix(options=options)

canvas = root_canvas.CreateFrameCanvas()

clockFont = graphics.Font()
clockFont.LoadFont("fonts/tom-thumb.bdf")

msgFont = graphics.Font()
msgFont.LoadFont("fonts/clR6x12.bdf")

clock = dash_modules.clock(33,0,63,6)
status = dash_modules.current_status(0,0, 6, 6)

def clear_frame(canvas, color=black):
    canvas.Fill(0,0,0)

while True:
    clear_frame(canvas)

    clock.canvas = canvas
    clock.show_box()
    clock.color = dim_red
    clock.run(canvas)

    status.canvas = canvas
    status.set_status("OK")
    status.run()

    

    time.sleep(0.1) 
    canvas = root_canvas.SwapOnVSync(canvas)


