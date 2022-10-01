
import pyxel

import game

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.select_y = 50
        pyxel.stop()
        pyxel.playm(0, loop=True)
        
    def update(self, input):
        if pyxel.btn(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.game.new_game()
        
    def draw(self):
        pyxel.text(40, 20, "30 Seconds of Daylight", 10)
        pyxel.text(30, 45, "Movement: Arrow or WASD keys", 13)
        pyxel.text(30, 55, "Attack  : Hold Z or N keys", 13)
        pyxel.text(30, 65, "Pickup  : X or M keys", 13)
        pyxel.text(52, 88, "Enter to Start", 12)
        pyxel.text(52, 100, "Escape to Exit", 9)
        
