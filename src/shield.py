from entity import Entity


class Shield(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)

        self.type = self.TYPE_SHIELD

    def update(self, map):
        pass


class Wood(Shield):
    def __init__(self, tile_x, tile_y):
        super().__init__("Wood", 0, 72, 72, tile_x, tile_y)


class Bronze(Shield):
    def __init__(self, tile_x, tile_y):
        super().__init__("Bronze", 0, 72, 56, tile_x, tile_y)


class Steel(Shield):
    def __init__(self, tile_x, tile_y):
        super().__init__("Steel", 0, 72, 48, tile_x, tile_y)
