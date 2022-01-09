
import pyxel

from player import Player

class Hud:
    def __init__(self, world):
        self.world = world
        
    def update(self):
        pass
        
    def draw(self):
        pyxel.pal()
        
        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(0, 0, 7, 0, 0, 160, 120, 15)
        
        map_title_w = len(self.world.current_map.name) * 4
        pyxel.rect(80 - ((map_title_w + 4) / 2), 0, map_title_w + 4, 8, 0)
        pyxel.text(80 - map_title_w / 2, 1, self.world.current_map.name, 7)
        
        # blt(x, y, img, u, v, w, h, [colkey])
        pyxel.text(9, 10, "You", 7)
        pyxel.blt(23, 8, 0, 32, 0, 8, 8) # man
        
        x = 8
        y = 20
        
        # health
        pyxel.blt(x, y, 0, 48, 48, 8, 8) # heart
        pyxel.text(x+2, y+8, str(self.world.current_map.player.hp) + "/" + str(self.world.current_map.player.max_hp), 7) # hp text
        
        y += 20
        
        p = self.world.current_map.player
        
        # attack
        attack = p.attack + Player.WEAPONS[p.weapon][0]
        ax = x
        if attack > 9:
            ax -= 6
        att_img = [Player.WEAPONS[p.weapon][1],Player.WEAPONS[p.weapon][2]]
        pyxel.blt(x, y, 0, att_img[0], att_img[1], 8, 8) # sword
        pyxel.text(ax+20, y, str(attack), 7)
        
        y += 8
        
        # defence
        defence = Player.SHIELDS[p.shield][0]
        dx = x
        if defence > 9:
            dx -= 6
        def_img = [Player.SHIELDS[p.shield][1],Player.SHIELDS[p.shield][2]]
        pyxel.blt(x, y, 0, def_img[0], def_img[1], 8, 8) # shield
        pyxel.text(dx+20, y, str(defence), 7)
        
        y += 14
        
        # xp needed for next level
        level = self.world.current_map.player.level
        next = 0
        xp = 0
        if level < Player.MAX_LEVEL-1:
            next = Player.XP_LEVELS[level+1]
            xp = next - self.world.current_map.player.xp
        xpx = x
        if xp > 9:
            xpx -= 6
        pyxel.blt(x, y, 0, 24, 48, 8, 8) 
        pyxel.text(xpx+20, y, str(xp), 7)
        
        y += 8
        
        # level
        lx = x
        if level+1 > 9:
            lx -= 6
        pyxel.text(x, y, "Lvl", 7)
        pyxel.text(lx+20, y, str(level+1), 7)
        
        y += 8
        
        # daylight info
        #secs = self.world.daylight_control.sec_cnt
        #pyxel.text(9, 81, str(secs), 0)
        #pyxel.text(8, 80, str(secs), 7)
    
        # text(x, y, s, col)
        # p = (self.world.current_map.player.tile_x*8, self.world.current_map.player.tile_y*8)
        # m = (pyxel.mouse_x - 40 + self.world.current_map.cam.x,\
            # pyxel.mouse_y - 8 + self.world.current_map.cam.y)
        # dist = distance(p, m)
        # pyxel.text(8, 100, str(dist), 7)
        
        # pyxel.text(90, 92, "p:" + str(self.world.current_map.player.tile_x*8) + "," + str(self.world.current_map.player.tile_y*8), 7)
        
        # pyxel.text(90, 100, "m:" + str(pyxel.mouse_x - 40 +self.world.current_map.cam.x) + "," + str(pyxel.mouse_y - 8 + self.world.current_map.cam.y), 7)
        