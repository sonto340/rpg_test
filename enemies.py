# various potential enemies included in here
# name is the name shown to the player
# hp is hit point
# atk is attack 
# def is defense 
# acc is accuracy determines hit rate
# random is a "random" number used to pull a value form a list to determine various elements
# such as damage values, hit rate calculation etc.
# exp is the experience given to the player upon defeat
#
#
goon = {
    "name": "Goon",
    "hp": 25,
    "atk": 13,
    "def": 7,
    "acc": 5,
    "random": 2,
    "exp": 7,
    "hit": 2
}

goon_captain = {
    "name": "Goon Captain",
    "hp": 75,
    "atk": 20,
    "def": 13,
    "acc": 9,
    "random": 3,
    "exp": 32 
}
# as of now the current enemy tag simply live here. in the future the current enemy tag 
# will be used to determine which enemy from this list is currently used in battle. 
current_enemy = goon