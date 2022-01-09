
from entity import Entity

class Weapon(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)
        
        self.type = self.TYPE_WEAPON
    
    def update(self, map):
        pass
        
class Club(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Club", 0, 64, 32, tile_x, tile_y)
        
class Sword(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Sword", 0, 48, 32, tile_x, tile_y)
        
class Axe(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Axe", 0, 56, 32, tile_x, tile_y)
        
