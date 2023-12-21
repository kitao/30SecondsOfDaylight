from random import choice, sample

import pyxel

import enemy
import potion
import shield
import weapon
from enemy import Enemy, Rat
from entity import Entity
from utils import *


class Map:
    LADDER_TILE = (6, 2)

    WALKABLE_TILES = [(1, 1), (4, 4), (5, 4), (4, 8), LADDER_TILE]

    def __init__(self, name, tm, tm_x, tm_y, tm_w, tm_h, world):
        self.name = name
        self.tm = tm
        self.tm_x = tm_x
        self.tm_y = tm_y
        self.tm_w = tm_w
        self.tm_h = tm_h
        self.cam = Rect(0, 0, 80, 72)
        self.update_cam = True
        self.world = world

        self.player = None
        self.entities = []

    def enter(self, p_tile_x, p_tile_y, player):
        self.update_cam = True
        self.player = player
        self.player.tile_x = p_tile_x
        self.player.tile_y = p_tile_y

        self.entities.clear()
        self.spawn_enemies()
        self.spawn_items()

        self.cam.x = max(
            0, min(self.tm_w * 8 - self.cam.w, self.player.tile_x * 8 - 40)
        )
        self.cam.y = max(
            0, min(self.tm_h * 8 - self.cam.h, self.player.tile_y * 8 - 32)
        )

    def spawn_enemies(self):
        open_tiles = []
        for y in range(self.tm_h):
            for x in range(self.tm_w):
                tile = pyxel.tilemaps[self.tm].pget(self.tm_x + x, self.tm_y + y)
                if (
                    (x != self.player.tile_x or y != self.player.tile_y)
                    and tile in self.WALKABLE_TILES
                    and distance((x, y), (self.player.tile_x, self.player.tile_y)) >= 4
                ):
                    open_tiles.append([self.tm_x + x, self.tm_y + y])

        # enemy chances
        lvl = self.player.level + 1
        chances = {
            "Rat": 0,
            "Scorpion": 0,
            "Guard": 0,
            "Strongman": 0,
            "Ghost": 0,
            "Skeleton": 0,
            "Zombie": 0,
            "Serpent": 0,
        }

        if lvl >= 15:
            chances["Rat"] = 10
            chances["Scorpion"] = 10
            chances["Guard"] = 10
            chances["Strongman"] = 20

            chances["Ghost"] = 10
            chances["Skeleton"] = 10
            chances["Zombie"] = 10
            chances["Serpent"] = 20
        elif lvl >= 10:
            chances["Rat"] = 20
            chances["Scorpion"] = 20
            chances["Guard"] = 10

            chances["Ghost"] = 20
            chances["Skeleton"] = 20
            chances["Zombie"] = 10
        elif lvl >= 5:
            chances["Rat"] = 50
            chances["Scorpion"] = 20

            chances["Ghost"] = 15
            chances["Skeleton"] = 15

        else:
            chances["Rat"] = 80

            chances["Ghost"] = 20

        en_list = []
        for key in chances:
            num = chances.get(key)
            for i in range(num):
                en_list.append(key)

        # print(en_list)

        num_to_gen = math.floor(len(open_tiles) * 0.15)

        # print(num_to_gen)

        random_open_tiles = sample(open_tiles, num_to_gen)
        for i in range(num_to_gen):
            self.add_entity(
                enemy.create(
                    choice(en_list), random_open_tiles[i][0], random_open_tiles[i][1]
                )
            )
            # self.add_entity(Rat(random_open_tiles[i][0], random_open_tiles[i][1]))

    def spawn_items(self):
        open_tiles = []
        for y in range(self.tm_h):
            for x in range(self.tm_w):
                tile = pyxel.tilemaps[self.tm].pget(self.tm_x + x, self.tm_y + y)
                if (
                    (x != self.player.tile_x or y != self.player.tile_y)
                    and tile in self.WALKABLE_TILES
                    and distance((x, y), (self.player.tile_x, self.player.tile_y)) >= 4
                ):
                    open_tiles.append([self.tm_x + x, self.tm_y + y])

        if self.player.hp < math.floor(self.player.max_hp * 0.75):
            tile = choice(open_tiles)
            self.add_entity(potion.Red(tile[0], tile[1]))
            open_tiles.remove(tile)

        if choice([0, 1]) == 0:
            if self.player.weapon == "None":
                tile = choice(open_tiles)
                self.add_entity(weapon.Club(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.weapon == "Club":
                tile = choice(open_tiles)
                self.add_entity(weapon.Sword(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.weapon == "Sword":
                tile = choice(open_tiles)
                self.add_entity(weapon.Axe(tile[0], tile[1]))
                open_tiles.remove(tile)
        else:
            if self.player.shield == "None":
                tile = choice(open_tiles)
                self.add_entity(shield.Wood(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.shield == "Wood":
                tile = choice(open_tiles)
                self.add_entity(shield.Bronze(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.shield == "Bronze":
                tile = choice(open_tiles)
                self.add_entity(shield.Steel(tile[0], tile[1]))
                open_tiles.remove(tile)

    def update(self, inputs):
        self.player.update(inputs, self)

        if self.update_cam:
            self.cam.x = max(
                0, min(self.tm_w * 8 - self.cam.w, self.player.tile_x * 8 - 40)
            )
            self.cam.y = max(
                0, min(self.tm_h * 8 - self.cam.h, self.player.tile_y * 8 - 32)
            )

        for e in self.entities:
            e.update(self)

        self.entities.sort(key=lambda x: x.type, reverse=True)

        self.update_cam = False

    def _is_tile_solid(self, tile_x, tile_y):
        tile = pyxel.tilemaps[self.tm].pget(self.tm_x + tile_x, self.tm_y + tile_y)
        if tile in self.WALKABLE_TILES:
            return False
        else:
            return True

    def _is_tile_occupied(self, tile_x, tile_y):
        for e in self.entities:
            if e.tile_x == tile_x and e.tile_y == tile_y:
                if e.type == e.TYPE_PLAYER or e.type == e.TYPE_ENEMY:
                    return True
        if tile_x == self.player.tile_x and tile_y == self.player.tile_y:
            return True
        return False

    def is_tile_free_for_enemy(self, tile_x, tile_y):
        if self.is_tile_free(tile_x, tile_y):
            tile = pyxel.tilemaps[self.tm].pget(self.tm_x + tile_x, self.tm_y + tile_y)
            if tile == self.LADDER_TILE:
                return False
            else:
                return True
        else:
            return False

    def is_tile_free(self, tile_x, tile_y):
        if tile_x < 0 or tile_x >= self.tm_w or tile_y < 0 or tile_y >= self.tm_h:
            return False

        if self._is_tile_solid(tile_x, tile_y) or self._is_tile_occupied(
            tile_x, tile_y
        ):
            return False
        else:
            return True

    def tile_get_any_enemy(self, tile_x, tile_y):
        for e in self.entities:
            if (
                self.tm_x + e.tile_x == self.tm_x + tile_x
                and self.tm_y + e.tile_y == self.tm_y + tile_y
                and e.type == Entity.TYPE_ENEMY
            ):
                return e
        return None

    def tile_get_any_item(self, tile_x, tile_y):
        for e in self.entities:
            if (
                self.tm_x + e.tile_x == self.tm_x + tile_x
                and self.tm_y + e.tile_y == self.tm_y + tile_y
            ) and (
                e.type == Entity.TYPE_WEAPON
                or e.type == Entity.TYPE_SHIELD
                or e.type == Entity.TYPE_POTION
                or e.type == Entity.TYPE_TELEPORTER
                or e.type == Entity.TYPE_TRIGGER
            ):
                return e
        return None

    # note: e tile values are from the texture, so need to be resized.
    def add_entity(self, e):
        e.tile_x -= self.tm_x
        e.tile_y -= self.tm_y
        if e.type == e.TYPE_TELEPORTER:
            to_map = self.world.map_dict[e.to_map_name]
            e.to_tile_x -= to_map.tm_x
            e.to_tile_y -= to_map.tm_y
        self.entities.append(e)

    def draw(self, draw_tilemap, draw_entities, night):
        if draw_tilemap:
            # bltm(x, y, tm, u, v, w, h, [colkey])
            if night:  # clip close around player
                # pyxel.blt(40 + self.tile_x*8 - cam.x, \
                # 8 + self.tile_y*8 - cam.y, \
                # self.img, \
                # self.img_x, \
                # self.img_y, \
                # 8, 8)

                clip_x = 40 + self.player.tile_x * 8 - self.cam.x - 8
                clip_y = 8 + self.player.tile_y * 8 - self.cam.y - 8

                pyxel.clip(clip_x, clip_y, 24, 24)
            else:  # clip normally to camera window
                pyxel.clip(40, 8, 80, 72)

            pyxel.bltm(
                40 - self.cam.x,
                8 - self.cam.y,
                self.tm,
                self.tm_x * 8,
                self.tm_y * 8,
                self.tm_w * 8,
                self.tm_h * 8,
            )

            # pyxel.rect(self.tm_x, self.tm_y, self.tm_w*8, self.tm_h*8, 7)

        if draw_entities:
            if night:
                for e in self.entities:
                    x_dist = e.tile_x - self.player.tile_x
                    y_dist = e.tile_y - self.player.tile_y
                    if x_dist >= -1 and x_dist <= 2 and y_dist >= -1 and y_dist <= 2:
                        e.draw(self.cam)
            else:
                for e in self.entities:
                    e.draw(self.cam)

        self.player.draw(self.cam)

        pyxel.clip()
