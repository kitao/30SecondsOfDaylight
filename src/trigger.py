
from entity import Entity

class Trigger(Entity):
    TYPE_CASTLE_DOOR = 0
    TYPE_CASTLE_KEY = 1
    
    def __init__(self, tile_x, tile_y, type):
        super().__init__("Trigger", 0, 32, 0, tile_x, tile_y)
        
        self.type = self.TYPE_TRIGGER
        self.trigger_type = type
        
    def update(self, map):
        pass
        
    def draw(self, cam):
        pass
        