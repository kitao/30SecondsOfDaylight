import pyxel

from world import World
from hud import Hud
from journal import Journal
from main_menu import MainMenu


class Game:
    STATE_MAIN_MENU = 0
    STATE_MAP = 1

    def __init__(self):
        self.state = self.STATE_MAIN_MENU
        self.main_menu = MainMenu(self)
        self.world = None
        self.hud = None

        # self.new_game()

    def new_game(self):
        pyxel.stop()
        pyxel.playm(1, loop=False)
        self.main_menu = None
        self.state = self.STATE_MAP
        self.world = World(self)
        self.hud = Hud(self.world)

    def game_over(self):
        self.state = self.STATE_MAIN_MENU
        self.main_menu = MainMenu(self)

    def update(self, inputs):
        if self.state is self.STATE_MAP:
            self.world.update(inputs)
            self.hud.update()
        elif self.state is self.STATE_MAIN_MENU:
            self.main_menu.update(inputs)

    def draw(self):
        if self.state is self.STATE_MAP:
            self.world.draw()
            self.hud.draw()
        elif self.state is self.STATE_MAIN_MENU:
            self.main_menu.draw()
