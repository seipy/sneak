# -*- coding: utf-8 -*-

import curses
import math

import config
import terminal


class TerminalTooSmallError(Exception):
    pass


class Stage:

    size = None
    width = None
    height = None
    padding = None
    boundaries = None
    chosen_theme = None

    def __init__(self, options={}):

        available_size = (width, height) = terminal.get_terminal_size()

        chosen_size = config.game_sizes[options.get('size', 'm')]

        if options.get('fullscreen', False):
            width = available_size[0] / 2 - 2
            height = available_size[1]
        else:
            if chosen_size[0] > available_size[0] / 2:
                width = available_size[0] / 2
            else:
                width = chosen_size[0]

            if chosen_size[1] > available_size[1]:
                height = available_size[1]
            else:
                height = chosen_size[1]

        self.size = (width, height)
        self.chosen_size = chosen_size
        self.width = width
        self.height = height

        padding_x = int(math.floor(available_size[0] - width) / 4)
        padding_y = int(math.floor(available_size[1] - height) / 2)

        self.padding = (padding_y, padding_x, padding_y, padding_x)

        self.boundaries = {
            'bottom': int(math.floor(height / 2)),
            'left': int(math.floor(-width / 2)),
            'right': int(math.floor(width / 2)),
            'top': int(math.floor(-height / 2)),
        }

        self.chosen_theme = {
            'colors': {
                'default': (curses.COLOR_WHITE, curses.COLOR_BLACK),
                'bg': (curses.COLOR_WHITE, curses.COLOR_WHITE),
                'snake': (curses.COLOR_RED, curses.COLOR_GREEN),
                'apple': (curses.COLOR_RED, curses.COLOR_RED),
                'border': (curses.COLOR_WHITE, curses.COLOR_YELLOW),
                'lives': (curses.COLOR_RED, curses.COLOR_RED),
                'text': (curses.COLOR_BLACK, curses.COLOR_WHITE),
            },
            'tiles': {
            }
        }

    def validate(self):
        """
        Validates that the selected game size will fit
        inside the available space of the terminal window

        Raises `TerminalTooSmallError` error on validation failure.
        """
        if self.chosen_size[0] > self.width or \
            self.chosen_size[1] > self.height:
            raise TerminalTooSmallError('Chose a smaller size or increase terminal window.')

    @property
    def size(self):
        return self.size

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @property
    def padding(self):
        return self.padding

    @property
    def boundaries(self):
        return self.boundaries

    @property
    def chosen_theme(self):
        return self.chosen_theme
