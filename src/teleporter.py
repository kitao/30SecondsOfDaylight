
from entity import Entity

class Teleporter(Entity):
    def __init__(self, tile_x, tile_y, to_tile_x, to_tile_y, to_map_name):
        super().__init__("Teleporter", 0, 32, 0, tile_x, tile_y)
        
        self.type = self.TYPE_TELEPORTER
        self.to_tile_x = to_tile_x
        self.to_tile_y = to_tile_y
        self.to_map_name = to_map_name
        
    def update(self, map):
        pass
        
    def draw(self, cam):
        pass
        