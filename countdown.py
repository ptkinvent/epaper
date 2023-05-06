#!/usr/bin/python

import sys
import json
import time
import datetime
from PIL import Image, ImageDraw, ImageFont

from lib.EinkScreen import EinkScreen


def draw_centered_text(drawer, y, text, font):
    screen_width, screen_height = drawer.im.size
    w, h = drawer.textsize(text, font)
    drawer.text(xy=(screen_width/2 - w/2, y), text=text, font=font, fill=0)


def main():
    with open(sys.argv[1]) as config:
        config = json.load(config)

    countdown_date = datetime.datetime.strptime(config['countdown_date'], '%m/%d/%Y').date()
    heading_text = config['heading']
    subheading_text = config['subheading']
    fontsize = config['fontsize']
    prev_delta = 0
    font_heading = ImageFont.truetype('fonts/SourceSansPro.ttf', fontsize)
    font_countdown = ImageFont.truetype('fonts/SourceSansPro.ttf', 144)
    screen = EinkScreen()

    while True:
        delta = (countdown_date - datetime.date.today()).days
        if prev_delta != delta:
            print(f'Updating, {delta} days remaining')

            black_image = Image.new(mode='1', size=(screen.width, screen.height), color=255)
            red_image = Image.new(mode='1', size=(screen.width, screen.height), color=255)

            black_image_drawer = ImageDraw.Draw(black_image)
            red_image_drawer = ImageDraw.Draw(red_image)

            if delta > 0:
                draw_centered_text(black_image_drawer, 50, heading_text, font_heading)
                draw_centered_text(red_image_drawer, 150, f"{delta}", font_countdown)
                draw_centered_text(black_image_drawer, 350, subheading_text, font_heading)
            elif delta == 0:
                draw_centered_text(black_image_drawer, 50, heading_text, font_heading)
                draw_centered_text(red_image_drawer, 150, f"{delta}", font_countdown)
                draw_centered_text(black_image_drawer, 350, subheading_text, font_heading)
            else:
                draw_centered_text(black_image_drawer, 50, heading_text, font_heading)
                draw_centered_text(red_image_drawer, 150, f"{-delta}", font_countdown)
                draw_centered_text(black_image_drawer, 350, subheading_text, font_heading)

            screen.draw(black_image, red_image)
            prev_delta = delta
        else:
            print('Not updating')


        time.sleep(3600)

main()
