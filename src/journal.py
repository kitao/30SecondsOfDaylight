
import pyxel

class Journal:
    MAX_LINES = 3

    def __init__(self, world):
        self.x = 8
        self.y = 88
        self.lines = []
        self.world = world
        
    def push_new_line(self, line, col):
        if len(self.lines) == self.MAX_LINES:
            self.lines.pop(0)
        self.lines.append([line, col])
        
    def draw(self):
        # text(x, y, s, col)
        for i in range(len(self.lines)):
            pyxel.text(self.x, self.y + i * 8, self.lines[i][0], self.lines[i][1])
            