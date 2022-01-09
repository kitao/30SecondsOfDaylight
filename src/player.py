
from entity import Entity
from input import *
import combat
import map_loader
import trigger

class Player(Entity):
    # name/key, attack, img_x, img_y
    WEAPONS = {
        "None": [1, 32, 56, 2],
        "Club": [3, 64, 32, 3],
        "Sword": [6, 48, 32, 5],
        "Axe": [9, 56, 32, 10]
    }
    
    # name/key, defence, img_x, img_y
    SHIELDS = {
        "None": [2, 32, 56],
        "Wood": [6, 72, 72],
        "Bronze": [12, 72, 56],
        "Steel": [18, 72, 48]
    }
    
    MAX_XP = 99
    MAX_LEVEL = 20
    
    XP_LEVELS = []
    for i in range(1, MAX_LEVEL+1):
        XP_LEVELS.append(round(0.04 * (i ^ 3) + 0.8 * (i ^ 2) + 2 * i))
     
    #for i in range(len(XP_LEVELS)):
    #    print("XP for level " + str(i+1) + " : " + str(XP_LEVELS[i]))
        
# XP for level 1 : 0
# XP for level 2 : 4
# XP for level 3 : 7
# XP for level 4 : 13
# XP for level 5 : 16
# XP for level 6 : 15
# XP for level 7 : 18
# XP for level 8 : 24
# XP for level 9 : 27
# XP for level 10 : 27
# XP for level 11 : 30
# XP for level 12 : 36
# XP for level 13 : 39
# XP for level 14 : 38
# XP for level 15 : 41
# XP for level 16 : 47
# XP for level 17 : 50
# XP for level 18 : 49
# XP for level 19 : 52
# XP for level 20 : 59

    def __init__(self):
        super().__init__("Player", 0, 32, 0, 0, 0)
        
        self.type = self.TYPE_PLAYER
        self.hp = 10
        self.max_hp = 10
        self.attack = 1
        self.defence = 1
        self.level = 0
        self.xp = 0
        
        self.weapon = "None"
        self.shield = "None"
        self.attack_delay = 0
        
        self.has_castle_key = False
        
    def add_xp(self, world, n):
        if self.level < self.MAX_LEVEL-1:
            next_level_xp = self.XP_LEVELS[self.level+1]
            self.xp = min(self.MAX_XP, self.xp + n)
            if self.xp >= next_level_xp:
                self.level += 1
                world.journal.push_new_line("Level up! (" + str(self.level+1) + ")", 9)
                self.xp = 0
                self.max_hp += 1
                self.attack += 1
                self.defence += 1
                #self.hp = self.max_hp
                
                # for i in range(self.MAX_LEVEL-1, -1, -1):
                    # #print(str(self.XP_LEVELS[i]))
                    # if self.xp >= self.XP_LEVELS[i]:
                        # self.level = i
                        # self.xp = 0
                        # break
                            
    def update(self, inputs, map):
        if self.attack_delay > 0:
            self.attack_delay -= 1;
    
        if Input.CONFIRM in inputs:
            if Input.UP in inputs:
                self.do_attack(0, -1, map)
            elif Input.DOWN in inputs:
                self.do_attack(0, 1, map)
            elif Input.LEFT in inputs:
                self.do_attack(-1, 0, map)
            elif Input.RIGHT in inputs:
                self.do_attack(1, 0, map)
        else:
            if Input.UP in inputs:
                self.move(0, -1, map)
            elif Input.DOWN in inputs:
                self.move(0, 1, map)
            elif Input.LEFT in inputs:
                self.move(-1, 0, map)
            elif Input.RIGHT in inputs:
                self.move(1, 0, map)
                
        if Input.CANCEL in inputs:
            self.do_pickup(map)
            
    def do_attack(self, dir_x, dir_y, map):
        if self.attack_delay == 0:
            enemy = map.tile_get_any_enemy(self.tile_x + dir_x, self.tile_y + dir_y)
            if enemy is not None:
                #map.entities.remove(enemy)
                self.attack_delay = self.WEAPONS[self.weapon][3];
                combat.player_attacked_enemy(map.world, self, enemy)
                
    def do_pickup(self, map):
        item = map.tile_get_any_item(self.tile_x, self.tile_y)
        if item != None:
            if item.type == item.TYPE_WEAPON:
                self.weapon = item.name
                map.world.journal.push_new_line(\
                    "You got the " + self.weapon + "!", 12)
                map.entities.remove(item)
            elif item.type == item.TYPE_SHIELD:
                self.shield = item.name
                map.world.journal.push_new_line(\
                    "You got the " + self.shield + " shield!", 12)
                map.entities.remove(item)
            elif item.type == item.TYPE_POTION:
                item.drink(self)
                map.world.journal.push_new_line(\
                    "You drank the " + item.name + " potion!", 14)
                map.entities.remove(item)
            
    def move(self, move_x, move_y, map):
        item = map.tile_get_any_item(self.tile_x + move_x, self.tile_y + move_y)
        if item != None:
            if item.type == item.TYPE_TELEPORTER:
                map_loader.enter_map(map.world, item.to_map_name, self,\
                    item.to_tile_x, item.to_tile_y)
                return
            elif item.type == item.TYPE_TRIGGER:
                if item.trigger_type == item.TYPE_CASTLE_DOOR:
                    if self.has_castle_key:
                        map.world.journal.push_new_line(\
                        "You open the doors! Well done!", 7)
                        map.world.set_game_over()
                    else:
                        map.world.journal.push_new_line(\
                        "Find the key to open the doors!", 7)
                elif item.trigger_type == item.TYPE_CASTLE_KEY:
                    self.has_castle_key = True
                    map.world.journal.push_new_line(\
                        "You found the CASTLE KEY!", 7)
                    map.entities.remove(item)
    
        if map.is_tile_free(self.tile_x + move_x, self.tile_y + move_y):
            if move_x != 0:
                self.tile_x = max(0, min(map.tm_w-1, self.tile_x + move_x))
                map.update_cam = True
            elif move_y != 0:
                self.tile_y = max(0, min(map.tm_h-1, self.tile_y + move_y))
                map.update_cam = True
        #else:
        #    pass
            #play(ch, snd, loop=False)
            #if pyxel.play_pos(3) == -1:
            #    pyxel.play(3, 0)
     
    def draw(self, cam):
        if self.hp == 0:
            return
        super().draw(cam)
        