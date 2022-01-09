
import map
import weapon
import shield
import potion
import teleporter
import trigger

def load_all(world):
    _load(world, "Courtyard")
    _load(world, "Outer Gate")
    _load(world, "East Wall")
    _load(world, "West Wall")
    _load(world, "Rear Ward")
    _load(world, "Secret Gardens")

def _load(world, map_name):
    new_map = None
    
    if map_name == "Courtyard":
        new_map = map.Map(map_name, 0, 0, 0, 16, 16, world)
    elif map_name == "Outer Gate":
        new_map = map.Map(map_name, 0, 48, 16, 16, 16, world)
    elif map_name == "East Wall":
        new_map = map.Map(map_name, 0, 0, 16, 24, 16, world)
    elif map_name == "West Wall":
        new_map = map.Map(map_name, 0, 24, 16, 24, 16, world)
    elif map_name == "Rear Ward":
        new_map = map.Map(map_name, 0, 16, 0, 48, 16, world)
    elif map_name == "Secret Gardens":
        new_map = map.Map(map_name, 0, 64, 0, 24, 16, world)
        
    if new_map != None:
        world.map_dict[map_name] = new_map
        
def enter_map(world, map_name, player, enter_tile_x, enter_tile_y):
    new_map = None
    new_map = world.map_dict[map_name]
    if new_map != None:
        world.current_map = world.map_dict[map_name]
        new_map.enter(enter_tile_x, enter_tile_y, player)
    if map_name == "Courtyard":
        new_map.add_entity(teleporter.Teleporter(7, 15, 55, 17, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(8, 15, 56, 17, "Outer Gate"))
        new_map.add_entity(trigger.Trigger(7, 1, trigger.Trigger.TYPE_CASTLE_DOOR))
        new_map.add_entity(trigger.Trigger(8, 1, trigger.Trigger.TYPE_CASTLE_DOOR))
        
    elif map_name == "Outer Gate":
        new_map.add_entity(teleporter.Teleporter(55, 16, 7, 14, "Courtyard"))
        new_map.add_entity(teleporter.Teleporter(56, 16, 8, 14, "Courtyard"))
        new_map.add_entity(teleporter.Teleporter(48, 27, 22, 27, "East Wall"))
        new_map.add_entity(teleporter.Teleporter(48, 28, 22, 28, "East Wall"))
        new_map.add_entity(teleporter.Teleporter(63, 27, 25, 27, "West Wall"))
        new_map.add_entity(teleporter.Teleporter(63, 28, 25, 28, "West Wall"))
        
    elif map_name == "East Wall":
        new_map.add_entity(teleporter.Teleporter(23, 27, 49, 27, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(23, 28, 49, 28, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(8, 16, 24, 14, "Rear Ward"))
        
    elif map_name == "West Wall":
        new_map.add_entity(teleporter.Teleporter(24, 27, 62, 27, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(24, 28, 62, 28, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(45, 16, 61, 14, "Rear Ward"))
        
    elif map_name == "Rear Ward":
        new_map.add_entity(teleporter.Teleporter(24, 15, 8, 17, "East Wall"))
        new_map.add_entity(teleporter.Teleporter(61, 15, 45, 17, "West Wall"))
        new_map.add_entity(teleporter.Teleporter(39, 0, 76, 14, "Secret Gardens"))
        new_map.add_entity(teleporter.Teleporter(40, 0, 77, 14, "Secret Gardens"))
        
    elif map_name == "Secret Gardens":
        new_map.add_entity(teleporter.Teleporter(76, 15, 39, 1, "Rear Ward"))
        new_map.add_entity(teleporter.Teleporter(77, 15, 40, 1, "Rear Ward"))
        new_map.add_entity(trigger.Trigger(74, 1, trigger.Trigger.TYPE_CASTLE_KEY))
        
            