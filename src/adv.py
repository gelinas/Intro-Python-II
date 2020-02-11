from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

choices = ["n", "s", "e", "w"]
current_room = room['outside']

print("\nWelcome, brave soul! Navigate the world by typing 'n', 's', 'e', 'w',\n    end your quest by typing 'q'")

#LOOP
while True:
    # PRINT
    print(f"\nLocation: {current_room.name}. {current_room.description}")
    # READ
    cmd = input("\n~~> ")
    # EVAL
    if cmd in choices:
        # print(cmd)
        if cmd == "n":
            try:
                current_room = current_room.n_to
            except:
                print("\nYou can't move north")
        if cmd == "s":
            try:
                current_room = current_room.s_to
            except:
                print("\nYou can't move south")
        if cmd == "e":
            try:
                current_room = current_room.e_to
            except:
                print("\nYou can't move east")
        if cmd == "w":
            try:
                current_room = current_room.w_to
            except:
                print("\nYou can't move west")
    elif cmd == "q":
        print("\nPlease return soon, intrepid adventurer!\n")
        break
    else:
        print("\nI did not understand that command. Please pick n, s, e, w or q.")
