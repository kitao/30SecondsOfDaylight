
import pyxel

import game

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.select_y = 50
        pyxel.stop()
        pyxel.playm(0, loop=True)
        
    def update(self, input):
        if pyxel.btn(pyxel.KEY_ENTER):
            self.game.new_game()
        
    def draw(self):
        pyxel.text(40, 20, "30 Seconds of Daylight", 10)
        pyxel.text(55, 50, "Enter to Start", 12)
        pyxel.text(55, 90, "Escape to Exit", 9)
        