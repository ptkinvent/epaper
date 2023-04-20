#!/usr/bin/python
# -*- coding:utf-8 -*-

from . import epd7in5b_V2
import logging


class EinkScreen:
    def __init__(self):
        """
        Initiates the e-ink screen
        """
        try:
            self.epd = epd7in5b_V2.EPD()
            self.width = self.epd.width
            self.height = self.epd.height
            self.epd.init()
            self.epd.Clear()
            logging.info('E-ink init')

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info('Canceled by ctrl+C')
            epd7in5b_V2.epdconfig.module_exit()
            exit()

    def draw(self, black_image, red_image):
        """
        Displays the given black and red images on the screen
        :param black_image: PIL Image type
        :param red_image: PIL Image type
        """
        try:
            self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(red_image))

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info('Canceled by ctrl+C')
            epd7in5b_V2.epdconfig.module_exit()
            exit()

    def __del__(self):
        """
        Shuts down the e-ink screen
        """
        try:
            self.epd.sleep()
            logging.info('E-ink shutdown')

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info('Canceled by ctrl+C')
            epd7in5b_V2.epdconfig.module_exit()
            exit()
