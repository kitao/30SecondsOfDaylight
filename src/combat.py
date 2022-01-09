
from random import randint

import pyxel

import world
from player import Player

def send_msg(world, msg, col):
    world.journal.push_new_line(msg, col)

def kill_enemy(world, enemy):
    world.current_map.entities.remove(enemy)

def player_attacked_enemy(world, player, enemy):
    enemy.hp = max(0, enemy.hp - (player.attack + Player.WEAPONS[player.weapon][0]))
    if enemy.hp == 0:
        send_msg(world, "You killed the " + enemy.name + \
            ". Got " + str(enemy.xp) + " XP!", 3)
        player.add_xp(world, enemy.xp)
        kill_enemy(world, enemy)
    else:
        send_msg(world, "You hit the " + enemy.name + ".", 11)
    
def enemy_attacked_player(world, enemy, player):
    shield_val = Player.SHIELDS[player.shield][0]
    #print(shield_val)
    if randint(1, 100) <= shield_val:
        send_msg(world, "You blocked the " + enemy.name + ".", 12)
    else:
        player.hp = max(0, player.hp - enemy.attack)
        if player.hp == 0:
            pyxel.stop()
            pyxel.playm(2, loop=False)
            send_msg(world, "You died.", 8)
            world.set_game_over()
        else:
            send_msg(world, "Got hit by " + enemy.name + ".", 8)
        