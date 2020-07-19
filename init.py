#!/usr/bin/env python

from rgbmatrix import RGBMatrixOptions

def get_options():
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.row_address_type = 0
    options.multiplexing = 0
    options.pwm_bits = 11
    options.brightness = 100
    options.pwm_lsb_nanoseconds = 130
    options.led_rgb_sequence = "RGB"
    options.pixel_mapper_config = ""
    options.panel_type = ""

    # optional
    #options.show_refresh_rate = 1
    options.gpio_slowdown = 3 # 1-4
    #options.disable_hardware_pulsing = False
    return options

