#!/usr/bin/python

import sys

from PIL import Image, ImageDraw, ImageFont
from lib.EinkScreen import EinkScreen



def main():
    screen = EinkScreen()

    black_image = Image.new(mode='1', size=(screen.width, screen.height), color=255)  # 255: clear the frame
    red_image = Image.new(mode='1', size=(screen.width, screen.height), color=255)  # 255: clear the frame

    bmp = Image.open(sys.argv[1])
    black_image.paste(bmp, (0, 0))

    screen.draw(black_image, red_image)


main()
