import pyxel

from map import Map
from daylight_control import DaylightControl
from player import Player
from journal import Journal
import map_loader


class World:
    MAX_GAME_OVER_WAIT_TICKS = 30  # 3 secs

    def __init__(self, game):
        self.game = game
        self.map_dict = {}
        self.current_map = None
        map_loader.load_all(self)

        self.daylight_control = DaylightControl()

        self.player = Player()

        map_loader.enter_map(self, "Courtyard", self.player, 7, 1)

        self.journal = Journal(self)

        self.game_over = False
        self.game_over_ticks = 0

    def set_game_over(self):
        self.game_over = True

    def update(self, inputs):
        if self.game_over:
            self.game_over_ticks += 1
            if self.game_over_ticks == self.MAX_GAME_OVER_WAIT_TICKS:
                self.game.game_over()
        else:
            self.daylight_control.update(self)
            self.current_map.update(inputs)

    def draw(self):
        self.current_map.draw(True, False, False)
        if self.daylight_control.is_night():
            pyxel.pal()
            self.current_map.draw(True, True, True)
        else:
            self.current_map.draw(False, True, False)

        self.journal.draw()
