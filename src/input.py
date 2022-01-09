
import pyxel

class Input:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    CONFIRM = 4
    CANCEL = 5

    def __init__(self):
        self.inputs = []
        
    def update(self):
        self.inputs.clear()
    
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) or \
            pyxel.btn(pyxel.GAMEPAD_1_UP):
            self.inputs.append(self.UP)
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) or \
            pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.inputs.append(self.DOWN)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) or \
            pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.inputs.append(self.LEFT)
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) or \
            pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.inputs.append(self.RIGHT)
            
        if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_N) or \
            pyxel.btn(pyxel.GAMEPAD_1_A):
            self.inputs.append(self.CONFIRM)
        elif pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.KEY_M) or \
            pyxel.btn(pyxel.GAMEPAD_1_B):
            self.inputs.append(self.CANCEL)
        
        return self.inputs
        