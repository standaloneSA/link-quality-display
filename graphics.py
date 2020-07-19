#!/usr/bin/env python3
from config import Config
from rgbmatrix import graphics
import datetime
import time


class GraphicsTest(Config):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("fonts/tom-thumb.bdf")

        msgFont = graphics.Font()
        msgFont.LoadFont("fonts/clR6x12.bdf")

        #red = graphics.Color(255, 0, 0)
        #graphics.DrawLine(canvas, 5, 5, 22, 13, red)

        #green = graphics.Color(0, 255, 0)
        #graphics.DrawCircle(canvas, 15, 15, 10, green)

        blue = graphics.Color(0, 0, 255)
        red = graphics.Color(255,0,0)

        while True:
            graphics.DrawText(canvas, font, 4, 5, blue, str(datetime.datetime.now().strftime("%H:%M:%S")))
            graphics.DrawText(canvas, msgFont, 4, 20, red, "Line 2")
            time.sleep(0.5) 
            canvas.Clear()


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
