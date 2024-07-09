dmg = 47
from enemies import current_enemy
def enemy_turn(damage):
    print(f'''It's {current_enemy["name"]}'s turn!''')
    if (ehit_rate * ran_num[x]) > (stats["acc"] / ran_num[x]): 
        print("Oh no, a hit!")
        print(f'''{current_enemy["name"]} did {damage} damage''')
        stats["hp"] =- dmg 
        if stats["hp"] <= 0:
            player_alive = False
        else:
            print("Time to strike back!")
    else:
        print("Aw yeah, they whiffed it!")
    print("Player turn message")
    break

enemy_turn
def player_turn(damage):

