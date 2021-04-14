# Write your code here :-)
# import circuit playground express board
from adafruit_circuitplayground import cp
import time

class NeoPixels:

    # set class variables
    pixels_off_state = [0, 0, 0]

    def __init__(self):
        # set instance variables here
        self.pixels_amount = len(cp.pixels)
        cp.pixels.brightness = 0.1
        print(NeoPixels.pixels_off_state)

    def flash(self, colour):
        cp.pixels.fill(colour)
        time.sleep(0.5)
        cp.pixels.fill(NeoPixels.pixels_off_state)
        time.sleep(0.5)

    def alternate_colour(self, colour_1, colour_2):
        for pixel in range(self.pixels_amount):
            if pixel % 2 == 0:
                cp.pixels[pixel] = colour_1
            else:
                cp.pixels[pixel] = colour_2
            time.sleep(0.5)
            cp.pixels[pixel] = NeoPixels.pixels_off_state

# ---------------------------------- -----

blue = [0, 0, 255]
red = [255, 0, 0]
magenta = [255, 0, 255]

neopixels_1 = NeoPixels()

# ----- loop forever
while True:
    neopixels_1.alternate_colour(blue, magenta)