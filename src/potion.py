
import entity
import player

class Potion(entity.Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)
        
        self.type = self.TYPE_POTION
    
    def update(self, map):
        pass
        
    def drink(self, player):
        raise NotImplementedError
        
class Red(Potion):
    def __init__(self, tile_x, tile_y):
        super().__init__("Red", 0, 56, 64, tile_x, tile_y)
        
    def drink(self, player):
        player.hp = player.max_hp
        