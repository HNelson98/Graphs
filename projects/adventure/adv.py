from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
revTravPath = []
maze = dict()
visited_rooms = set()
revTravDict = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}



def getRoomExits(room):
    #I want to make a dictionary and put the exits for the room in it.

    maze[room.id] = dict()
    roomExits = room.get_exits()

    for exit in roomExits: 
        maze[room.id][exit] = '0'

#lets depth first search to go through the map and build it
def buildMap(room, directions):
    lastRoom = player.current_room.id
    newDirection = directions.pop(0)

    player.travel(newDirection)

    newRoomId = player.current_room.id
    newRoom = player.current_room

    traversal_path.append(newDirection)

    revPath = revTravDict.get(newDirection)

    revTravPath.append(pathback)

    if newRoomId not in maze:
        getRoomExits(newRoom)
        maze[lastRoom][newDirection] = newRoomId
        maze[newRoomId][revPath] = lastRoom
    else:
        maze[prevRoom][newDirection] = newRoomId

def backTrack(room):
    for move in revTravPath[::-1]:
        player.travel(move)
        traversal_path.append(move)
        revTravPath.pop(-1)
        if "0" in maze[player.current_room.id].values():
            return




#now to actually run it while the length of maze is smaller than the number of rooms
while len(maze) < len(room_graph):
    unkownPath = []
    newRoom = player.current_room
    if newRoomId not in maze:
        getRoomExits(newRoom)

    for direction, room in maze[newRoomId].items():
        if room == "0":
            unkownPath.append(direction)
    if len(unkownPath) > 0:
        buildMap(newRoom, unkownPath)
    else:
        if len(revTravPath) > 0:
            backTrack(newRoom)
        else:
            exits = newRoom.get_exits()
            leave = random.choice(exits)
            player.travel(leave)

#TRAVERSAL TEST

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
