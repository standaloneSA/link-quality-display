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


status = dash_modules.current_status(0,0, 6, 6)

last_seen_label = dash_modules.label(28,0,63,6)
last_seen_label.color = dim_gray

last_seen_time = dash_modules.label(30,7,63,12)
last_seen_time.color = dim_red

ping_res = dash_modules.histogram(0,32,65,24)

def clear_frame(canvas, color=black):
    canvas.Fill(0,0,0)

check_host = NetCheck(host=host)



check_host.update()
while True:
    clear_frame(canvas)
    
    last_seen_label.canvas = canvas
    last_seen_label.text("Last seen:")

    last_seen_time.canvas = canvas
    last_seen_time.text(check_host.data["last_seen_alive"])

    ping_res.canvas = canvas

    if check_host.data['packet_loss'] < 5:
        hist_color = dim_green
    elif check_host.data['packet_loss'] < 25:
        hist_color = dim_yellow
    else:
        hist_color = dim_red

    ping_res.update_data({'value': check_host.data['link_quality'], 'color': hist_color})
    ping_res.run()

    if check_host.data['is_alive'] == True:
        status.set_status("OK")
    elif check_host.data['is_alive'] == 'unknown':
        status.set_status("UNKNOWN")
    elif check_host.data['is_alive'] == False:
        status.set_status("CRITICAL")
    status.canvas = canvas
    status.run()

    check_host.update()
    canvas = root_canvas.SwapOnVSync(canvas)



