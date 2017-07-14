from random import choice

cave_numbers = list(range(0,20))
caves = []
for i in cave_numbers:
    caves.append([])

unvisited_caves = list(range(0,20))
visited_caves = list([0])
unvisited_caves.remove(0)

while unvisited_caves != []:
    i = choice(visited_caves)
    if len(caves[i]) >= 3:
        continue
    
    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)
    
    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)
    
    for number in cave_numbers:
        print(number, ":", caves[number])
    print("--------")
    
for i in cave_numbers:
    while len(caves[i]) < 3:
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
    
    for number in cave_numbers:
        print(number, ":", caves[number])
    print("--------")

for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)

wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
       player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)

print ("Welcome to Hunt the Wumpus!")
print ("You can see", len(cave_numbers), "caves")
print ("To play, just type the number")
print ("of the cave you wish to enter next")

while True:
    print ("You are in cave", player_location)
    print ("From here, you can see caves:", caves[player_location])
    if wumpus_location in caves[player_location]:
        print ("I smell a wumpus!")
    if wumpus_friend_location in caves[player_location]:
        print ("I smell an even stinkier wumpus!")
    
    print("Which cave next?")
    player_input = input(">")
    if (not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print (player_input + "?")
        print ("That's not a direction that I can see!")
        continue
    
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print("Aargh! You got eaten by a wumpus!")
            break
        if player_location == wumpus_friend_location:
            print("Aargh! You got hugged by the wumpus' friend!")
            break