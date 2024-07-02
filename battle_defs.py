dmg = 47
from enemies import current_enemy
def enemy_turn(damage):
    print(f'''It's {current_enemy["name"]}'s turn!''')
    print(f'''{current_enemy["name"]} did {damage} damage''')
    stats["hp"] =- dmg 
    
    if stats["hp"] <= 0:
        player_alive = False
    else:
        print("Player turn message")
        break
