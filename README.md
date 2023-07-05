# e-Paper Display #
This is a catch-all project to collect scripts for my e-Paper project. The hardware setup is a very low-power solution for displaying slowly-updating monochrome text and images. It consists of a Raspberry Pi Zero W connected to a 7.5-inch e-ink display.

The folders in the `lib/` folder are taken from https://github.com/waveshare/e-Paper.

## Setup ##
  - [7.5 inch E-Ink Display](https://www.amazon.com/7-5inch-HAT-Three-color-consumption-Resolution/dp/B075YP81JR/ref=sr_1_4)
  - [Raspberry Pi Zero W](https://www.amazon.com/Raspberry-Pi-Zero-Wireless-model/dp/B06XFZC3BX/)

## Config ##
For `countdown.py`, use a config file like the following:
```
{
    "name": "Birthday",
    "comment": "",
    "version": "1.0",

    "countdown_date": "07/03/2023",
    "fontsize": 60,

    "title_before": "Days until birthday:",
    "subtitle_before": "Happy July!",

    "title_during": "Days until birthday:",
    "subtitle_during": "Happy birthday!",

    "title_after": "Days since birthday:",
    "subtitle_after": "Happy July!"
}
```
