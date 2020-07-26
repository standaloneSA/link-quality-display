#!/usr/bin/env python3
import datetime
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import init
from color_names import *
import dash_modules
from netcheck import NetCheck

host = 'www.starlink.com'

options = init.get_options()
root_canvas = RGBMatrix(options=options)

canvas = root_canvas.CreateFrameCanvas()

clockFont = graphics.Font()
clockFont.LoadFont("fonts/tom-thumb.bdf")

msgFont = graphics.Font()
msgFont.LoadFont("fonts/clR6x12.bdf")

clock_label = dash_modules.label(33,0,63,6)
clock_label.color = dim_gray 

clock = dash_modules.clock(33,7,63,12)
status = dash_modules.current_status(0,0, 6, 6)

last_seen = dash_modules.label(25, 14, 63, 18)
last_seen.color = dim_gray

def clear_frame(canvas, color=black):
    canvas.Fill(0,0,0)

check_host = NetCheck(host=host)

check_host.update()
while True:
    clear_frame(canvas)
    
    clock_label.canvas = canvas
    #clock_label.show_box()
    clock_label.text("Current:")

    clock.canvas = canvas
    clock.color = dim_red
    clock.run()

    status.canvas = canvas
    status.set_status("OK")
    status.run()

    last_seen.canvas = canvas
    last_seen.text("Last seen:") 

    canvas = root_canvas.SwapOnVSync(canvas)



