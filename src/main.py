# title: 30 Seconds of Daylight
# author: Adam
# desc: First Pyxel Jam-winning roguelike game
# site: https://github.com/kitao/30SecondsOfDaylight
# license: MIT
# version: 1.0

import math
from random import choice, randint, sample

import pyxel

from game import Game
from input import Input


class App:
    FPS = 10
    TITLE = "30 Seconds of Daylight"

    def __init__(self):
        pyxel.init(160, 120, title=self.TITLE, fps=self.FPS)

        pyxel.load("../res/rpg01.pyxres")

        self.input = Input()
        self.game = Game()

        # pyxel.mouse(visible=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.game.update(self.input.update())

    def draw(self):
        pyxel.cls(0)

        self.game.draw()


App()
