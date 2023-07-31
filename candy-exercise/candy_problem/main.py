'''
DIRECTIONS
==========

1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

2. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the candy_name parameter.

4. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. Starting with nominal cases, write tests for each of the functions below then 
write tests to handle edge cases.
'''

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

#1
def get_friends_favorite_candy_count(favorites):
    candy_count = {}

    for friends in favorites:
        candy_list = friends[1]

        for candy in candy_list:
            if candy not in candy_count:
                candy_count[candy] = 1

            elif candy in candy_count:
                candy_count[candy] += 1
    
    return candy_count

#2
def create_new_candy_data_structure(data):
    fav_candy_count = {}

    for friends in data:
        candy_list = data[1]

        for candy in candy_list:
            if candy not in fav_candy_count:
                fav_candy_count[candy] = []

#3
def get_friends_who_like_specific_candy(data, candy_name):
    pass

#4
def create_candy_set(data):
    pass 
