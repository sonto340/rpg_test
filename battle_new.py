from char import stats
from char import name
from enemies import current_enemy
import time
import random
# basically required imports. maybe could be made from scratch but i doubt it
# utilize current_enemy["random"] for "random" number generation
in_battle = True
player_alive = True
ran_num = [1, 2, 3, 4, 5]
hit_rate = 66
roll = (stats["acc"] - current_enemy["acc"])
ehit_rate = current_enemy["acc"] 
x = current_enemy["random"]

print(ran_num)
print(ran_num[x])
shuffle = random.shuffle(ran_num)
print(ran_num)
print(ran_num[x])
print("You enounter " + current_enemy["name"] + "!!")
time.sleep(1)
print("Get ready for a fight!")
while in_battle:
    hp_count = f"{name}'s HP: {stats["hp"]} | {current_enemy["name"]}'s HP: {current_enemy["hp"]}"
    time.sleep(1)
    if player_alive:
        player_turn = True
        if player_turn:
            print("Alright, you're up!")
            print(hp_count)
            command = input('''
What will you do?
(F)ight
(I)tem
(R)un
> ''')
            print(command.upper)
            if command.upper == "F":
                shuffle
                if (roll - ran_num[x]) > hit_rate:
                    print("A Hit!!")
                    shuffle
                    damage = (stats["atk"] - current_enemy["def"]) + ran_num[x]
                    print(damage)
                    time.sleep(1)
                    print(f'You did {damage} damage!')
                    if damage == 69:
                        print("Very nice!~~")
                    else:
                        time.sleep(1)
                    current_enemy["hp"] =- damage
                    print(hp_count)

                else:
                    print("Oops, whiffed it...")
                    player_turn = False
        print(f"Alright, the enemy {current_enemy["name"]}'s turn to attack!")
        shuffle
        if ehit_rate * ran_num[x] > (stats["acc"] / ran_num[x]):
            print("Oh no they hit..")
            damage = (current_enemy["atk"] - stats["def"]) + ran_num[x]
            print(f'{name} took {damage} damage!')
            stats["hp"] =- damage
            if stats["hp"] <= 0:
                player_alive = False
            else:
                player_turn = True
        else:
            print("Aw, yeah! They whiffed!")
            player_turn = True

                
                

    else:
        print("YOU LOSE")
        in_battle = False
        break
