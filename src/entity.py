
import pyxel

class Entity:
    TYPE_NONE = -1
    TYPE_PLAYER = 0
    TYPE_ENEMY = 1
    TYPE_WEAPON = 2
    TYPE_SHIELD = 3
    TYPE_POTION = 4
    TYPE_TELEPORTER = 5
    TYPE_TRIGGER = 6

    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        self.name = name
        self.img = img
        self.img_x = img_x
        self.img_y = img_y
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.type = -1
        
    def update(self, map):
        raise NotImplementedError
        
    def draw(self, cam):
        if self.tile_x*8 + 8 < cam.x or self.tile_x >= cam.x + cam.w or\
            self.tile_y*8 <= cam.y - 8 or self.tile_y*8 >= cam.y + cam.h:
            return
        # blt(x, y, img, u, v, w, h, [colkey])
        pyxel.blt(40 + self.tile_x*8 - cam.x, \
            8 + self.tile_y*8 - cam.y, \
            self.img, \
            self.img_x, \
            self.img_y, \
            8, 8)
            