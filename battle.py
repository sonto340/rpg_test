from char import stats
from char import name
from enemies import current_enemy
import time
import random
# Currently pulls dict from other files housing character and enemy stats
# enemies are all stored in the same file, with the value {current_enemy} being set elsewhere to determine which dict is pulled
#
# there is almost certainly a clearner solution but this works 
print(f"You encountered " + current_enemy["name"] + "!!")
print("Let's get ready for a fight!!")
input()
# Hit Chance is 65 A number is rolled to determine if it hits. 
# Right now that is simply the enemy's accuracy(ACC) subtracted from player's accuracy(ACC) 
# if the roll is higher than the hit chance, the attack is succesful
# ran_num is a list that modifies various factors such as hit rate, damage etc
# it is pulled from enemies.py in the "random" attribute from the dict of current_enemy
ran_num = [2, 2, 4, 5, 2, 1, 4, 5, 3, 2, 1, 4, 6, 1] 
player_alive = True
hit_chance = 65
in_combat = True
y = 0
# I define y as 0 here so no error occurs later when y is deifned in the same line it's called
while in_combat:
    random.shuffle(ran_num)
    print(ran_num)
    shuffle = y, x = current_enemy["random"], ran_num[int(y)]
    # defining shuffle here after "entering" combat but before any actual maths are done 
    print(f"x = {x}")
    print(f"{current_enemy["name"]} HP Remaining: {current_enemy["hp"]}")
    time.sleep(1)
    print(f"{name} HP Remaining: {stats["hp"]}")
    time.sleep(1)
    command = input('''What will you do?
        (F)ight
        (I)tems
        (R)un
        >''')
    if command.upper() == "F":
        roll = (stats["acc"] - current_enemy["acc"] - (x+1))
        random.shuffle(ran_num)
        shuffle
        print(ran_num)
        print(f"x = {x}")
        print(roll)
        if (hit_chance < roll):
            hit = True
        else:
            hit = False
        if hit == True:
            damage = stats["atk"] - current_enemy["def"] + x
            print(f"x={x}")
            random.shuffle(ran_num)
            print(ran_num)
            print("A Hit!")
            time.sleep(1)
            print(f"You did {damage} damage!")
            time.sleep(1)
            current_enemy["hp"] = current_enemy["hp"] - damage
            print(f'{current_enemy["name"]} remaining HP: {current_enemy["hp"]}')
            time.sleep(1)
        else:
            print("You missed!!")
            time.sleep(1)
            print("Time for a counterattack!!")
            input()
    if command.upper() == "I":
        print("I'm not good enough to program items yet 😬")
        time.sleep(1)
    if command.upper() == "R":
        print("you ran!")
        in_combat = False
        break
    if command.upper() == "*":
        print("Please enter a valid command")
# As of now enemy will always attack after any action, outside of running.
# Items ends the battle instantly
# In the future I will find a way to determine counterattacks on an action-based basis
    print(f'{current_enemy["name"]} attacks!')
    time.sleep(1)
    player_damage = (current_enemy["atk"] - stats["def"])
    print(f"{name} took {player_damage} damage!!")
    time.sleep(1)
    stats["hp"] = stats["hp"] - player_damage
    print(f'{name} remaining HP: {stats["hp"]}')
    time.sleep(1)
    if stats["hp"] <= 0:
        player_alive = False
# Debugging line
#         print(f"player_alive is currently set to {player_alive}")
        break
    else:
       print("Next turn Coming up...")
       time.sleep(3)
print("~Battle Over~")
# debugging line
# print(f"player_alive is currently set to {player_alive}")
if player_alive == False:
    print("You lose!")
else:
    print("You win!")

# messy messy messy, but functional
# currently "works" but needs rewritten form scratch with new knowledge 
# proud of the random number generation although it can certainly be done in less than 100 lines of code plus comments.