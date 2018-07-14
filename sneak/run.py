# -*- coding: utf-8 -*-

import graphics
import theme
import gameloop
import parser
import stage


def exit():
    graphics.exit()
    print 'Thank you, come again!'


def run():
    try:
        parser.init()
        stage.init()
        graphics.init()
        theme.init()
        gameloop.start()

    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    run()
