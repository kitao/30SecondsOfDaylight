from random import randint, choice

from entity import Entity
import combat


class Enemy(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)

        self.type = self.TYPE_ENEMY

        self.hp = 5
        self.max_hp = 5
        self.attack = 1
        self.defence = 1
        self.xp = 1

        self.max_move_delay = 10  # frames
        self.move_delay = 0  # frames

    def update(self, map):
        self.move_delay += 1
        if self.move_delay == self.max_move_delay:
            self.move_delay = 0

            if not self.try_attack(map):
                if choice([0, 1]) == 0:
                    self.move(choice([-1, 1]), 0, map)
                else:
                    self.move(0, choice([-1, 1]), map)

    def try_attack(self, map):
        p_tile_x = map.player.tile_x
        p_tile_y = map.player.tile_y
        if (self.tile_x == p_tile_x and (abs(self.tile_y - p_tile_y) == 1)) or (
            self.tile_y == p_tile_y and (abs(self.tile_x - p_tile_x) == 1)
        ):
            combat.enemy_attacked_player(map.world, self, map.player)

    def move(self, move_x, move_y, map):
        if map.is_tile_free_for_enemy(self.tile_x + move_x, self.tile_y + move_y):
            if move_x != 0:
                self.tile_x = max(0, min(map.tm_w - 1, self.tile_x + move_x))
            elif move_y != 0:
                self.tile_y = max(0, min(map.tm_h - 1, self.tile_y + move_y))

    def draw(self, cam):
        super().draw(cam)


def create(name, tile_x, tile_y):
    e = None
    if name == "Rat":
        e = Rat(tile_x, tile_y)
    elif name == "Scorpion":
        e = Scorpion(tile_x, tile_y)
    elif name == "Guard":
        e = Guard(tile_x, tile_y)
    elif name == "Strongman":
        e = Strongman(tile_x, tile_y)
    elif name == "Ghost":
        e = Ghost(tile_x, tile_y)
    elif name == "Skeleton":
        e = Skeleton(tile_x, tile_y)
    elif name == "Zombie":
        e = Zombie(tile_x, tile_y)
    elif name == "Serpent":
        e = Serpent(tile_x, tile_y)
    elif name == "Witch":
        e = Witch(tile_x, tile_y)

    return e


class Rat(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Rat", 0, 48, 8, tile_x, tile_y)

        self.hp = 1
        self.max_hp = 1
        self.attack = 1
        self.defence = 1
        self.xp = 1

        self.max_move_delay = 20  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Scorpion(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Scorpion", 0, 56, 8, tile_x, tile_y)

        self.hp = 3
        self.max_hp = 3
        self.attack = 3
        self.defence = 3
        self.xp = 2

        self.max_move_delay = 15  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Guard(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Guard", 0, 40, 0, tile_x, tile_y)

        self.hp = 8
        self.max_hp = 8
        self.attack = 8
        self.defence = 8
        self.xp = 3

        self.max_move_delay = 15  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Strongman(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Strongman", 0, 48, 0, tile_x, tile_y)

        self.hp = 14
        self.max_hp = 14
        self.attack = 14
        self.defence = 14
        self.xp = 3

        self.max_move_delay = 12  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Ghost(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Ghost", 0, 72, 8, tile_x, tile_y)

        self.hp = 2
        self.max_hp = 2
        self.attack = 2
        self.defence = 2
        self.xp = 4

        self.max_move_delay = 5  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Skeleton(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Skeleton", 0, 64, 0, tile_x, tile_y)

        self.hp = 6
        self.max_hp = 6
        self.attack = 6
        self.defence = 6
        self.xp = 5

        self.max_move_delay = 15  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Zombie(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Zombie", 0, 72, 0, tile_x, tile_y)

        self.hp = 16
        self.max_hp = 16
        self.attack = 16
        self.defence = 16
        self.xp = 6

        self.max_move_delay = 20  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Serpent(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Serpent", 0, 32, 8, tile_x, tile_y)

        self.hp = 20
        self.max_hp = 20
        self.attack = 20
        self.defence = 20
        self.xp = 8

        self.max_move_delay = 20  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames


class Witch(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Witch", 0, 56, 0, tile_x, tile_y)

        self.hp = 25
        self.max_hp = 25
        self.attack = 25
        self.defence = 25
        self.xp = 40

        self.max_move_delay = 18  # frames
        self.move_delay = randint(1, self.max_move_delay - 1)  # frames
