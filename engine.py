from sys import exit
from os import system, name

#Declarations
# Classes
class Player: # This will control the data of the player's inventory, and position in the game

    def __init__(self):
        self.inventory = [] # Creates an empty inventory
        self.position = 0 # Sets the default starting position of the player

    def putInInventory(self, item): # item takes either False or a string

        if item == False: # Will not append iventory, had issue seeing null data put in as item
            print("No item to put in inventory")

        elif item == True: # No current functions should return, contingency to prevent a posible True from being appended to inventory
            pass

        else:
            self.inventory.append(item) # Will add value of item to player's Inventory
            print("Put into inventory")

    def checkInventory(self): # Used to print the contents of player's inventory
        print('\t', *self.inventory, sep = '\n\t') # Can't get this to not return line before printing first item in list?
        print('')
    def getInventory(self):
        return self.inventory
    def setPlayerPos(self, position): # This will change the room the player is currently in
        self.position = position

    def getPlayerPos(self): # This will return the player's position on the map
        return self.position

player = Player()

class Room: # This will construct the room's contents and maintain it's perminance

    def __init__(self, location, item): # Takes the location on the map, and if there is an item
        self.location = location # Will never need to change the location of the rooms
        self.item = item # Holds if an item is in the room
        player_has_entered = False # Checks to see if the room has been entered

        if None == item: # Will check if any item is put into room. If "" i.e none, will not allow
            self.has_item = False
            print('Room made without Item')

        else: # Will create room allowing an item to be taken if needed
            print('Room made with Item')
            self.has_item = True
            self.taken = False

    def getRoomPos(self): # This returns the room location on the map
        return self.location

    def getRoomEntered(self): # This will tell if room has been entered
        return self.player_has_entered

    def setRoomEntered(self): #This will mark the room entered
        self.player_has_entered = True

    def takeItem(self): #This will return an item to be put into the player's inv, and then prevent the item from being taken a second time

        if self.has_item and not self.taken: # If there is supposed to be an item in the room and it's yet to be added to inventory, add it and set it taken.
            self.taken = True
            print(f"{self.item} taken.")
            return self.item # Returns item to be handled by Player.putInInventory()

        elif self.has_item and self.taken: # If there was an item in the room and it's already been added to the inventory, return False preventing an append to inv
            print(f"{self.item} has already been taken.")
            return False # Returns False to prevent null data as an item name in inventory list

        else: # If there was never any item in the room
            print("This room doesn't have any items")
            return False # Returns False to prevent null data as an item name in inventory list

# Engine Methods
def screen_clear(): # Clears the screen
    if name == "nt":
        _ = system("cls") # Detects is windows to use NT cls to clear screen
        pass
    else:
        _ = system("clear") # *nix OSes use clear

def prompt(player_inv,quick_response): # All keywords will be handled by the prompt and simplified for the enigine ####################
    if quick_response:
        action = input("> ")
        return action
    else:
        ## DECLARARTIONS ## Most are self explanatory
        special =["help", "look", "check"]
        exits = ["quit", "exit", "leave"]
        movement = ["go", "move", "climb", "jump"]
        attacks = ["attack", "stab", "hit", "kill", "confront"]
        dodge = ["dodge", "evade", "avoid"]
        actions = ["take","get", "push", "break"]
        sneak = ["sneak", "stealth"]
        compass_directions = ["north", 'n', "south", 's', "east", 'e', "west", 'w']
        verbal_dirctions = ["up", "down", "right", "forward", "back", "left"]
        climbable = ["rock", "tree", "wall"]
        item_use = ["give", "use", "drop"]


        ## PRIVATE METHODS TO PROMPT ##
        def whatDirection(list): # Will cycle through the inputed list and find if there is a direction, and what direction if so
            i = 0
            try: # This method may return an IndexError
                while i < 5: # Instead of checking the entire list it will check up to 5 words ie go quickly out the left | door
                    if list[i] in compass_directions: # Searches for a match in compass_directions list and returns
                        return True,list[i]
                    elif list[i] in verbal_dirctions: # Searches in the verbal_dirctions list
                        return True,list[i]
                    elif list[0] == "climb" and list[i] in climbable:
                        return True, "up"
                    elif list[0] == "jump" and list[i] == "off":
                        return True, "down"
                    else:
                        i+=1
                return False,None
            except IndexError: # If the command is < 5 the program will create an exception to checking by the length of the list
                for i in range(0, len(list)):
                    if list[i] in compass_directions:
                        return True,list[i]
                    elif list[i] in verbal_dirctions:
                        return True, list[i]
                    elif list[0] == "climb" and list[i] in climbable:
                        return True, "up"
                    elif list[0] == "jump" and list[i] == "off":
                        return True, "down"
                    else:
                        pass
                return False,None

        def createMove(list, direction): # Takes in a tupple from whatDirection to return a movement to main execution
            if list[0] == "climb":
                if direction[0]:
                    return "climb", direction[1]
                else:
                    print("Climb What?")

            if list[0] == "jump":
                if direction[0]:
                    return "jump", direction[1]
                else:
                    print("Which direction?")
            else:
                if direction[0]:
                    return "go", direction[1]
                else:
                    print("Which Direction")

    ## EXECUTION OF CODE ##
    # Takes in the user input to check the action
        while True: # Prompt will run until data gets returned
            action = input("> ")
            action = action.lower()
            action = action.split(" ")
            if action[0] in sneak: # Checks to see if sneak is in sentance
                try:
                    except_ = action[1]
                    return action
                except IndexError:
                    print("Sneak?")
            elif action[0] in exits: # Will Exit the program
                print("Exiting Program")
                dead("You just dropped dead? Dammit not another one... wait, no?\nSomebody grab the bat, he's convulsing!",None)
            elif action[0] == "clear":
                screen_clear()
            elif action[0] in special:
                if action[0] == special[0]: # Prints a short help message for the prompt
                    print("Welcome to The World of Wulfmund, where all your greatest fantasies come true.")
                    print("Unless they don't... Wulfmund is a short game that I wrote to learn to code.")
                    print("The prompt accepts full sentences, looking for certain keywords. The keywords")
                    print("are go, climb, take, sneak, stab, attack, kill, confront, push, break, evade")
                    print("look, jump. Some synonyms are allowed such as move instead of go.")
                    print("Please enter an action followed by a noun wherever needed. Look, and check")
                    print("when typed alone will print the contents of the room again. Most commands are")
                    print("self explanatory. Experiment, but most important have fun!")
                else: # Will cause the room to reprint
                    if len(action) == 1: #
                        print(action)
                        return "look",False # Returns 'look' if false it will reprint room
                    else:
                        print(action)
                        action.pop(0)
                        return ["look"] + action # Will look at specific entities in room for a little more detail. action returned is room specific

            elif action[0] in movement: # Returns what room to move to
                action = (createMove(action, whatDirection(action)))
                if not action:
                    pass
                else:
                    return action

            elif action[0] in attacks: # Returns what to attack
                if "self" in action: # If atacking self creates new responses
                    if action[0] == "stab" and "sword" in player_inv:
                        print("You fumble around with your sword, you push it slowly into yourself.")
                        print("The writhing agony you experience makes you fall swiftly onto the sword.")
                        print("Thus ending your pathetic existence swiftly...")
                        dead("You Bled out quick?","stabbed")
                    elif action[0] == "stab" and not "sword" in player_inv:
                        print("You have no sword to stab with")
                    elif "confront" == action[0]:
                        print("There is no mirror nearby to confront yourself in...")
                    elif "hit" == action[0]:
                        print("Look at yourself, you got a welt now...")
                    elif action[0] == "kill":
                        print("If you say so?")
                        print("You stumble around a bit when an ogre pops out of nowhere. You fall, knees weak,")
                        print("arms are heavy. Vomit on your armour alrea...\n\n")
                        print("The ogre bashed that thought out of your skull, along with your brain.")
                        dead("Next time don't think of any references, ogres don't like that.",None)
                    else:
                        print("You attack yourself...\nYou tore your tunic, fairy boy...")


                else:
                    try: # Will attack if entity is typed
                        except_ = action[1]
                        return action
                    except IndexError: # if attack alone in list, will ask what to attack
                        print("Attack what?")

            elif action[0] in dodge: # Returns what to evade in room
                try:
                    except_ = action[1]
                    action.pop(0)
                    return ["evade"] + action
                except IndexError:
                    print("Evade what?")

            elif action[0] in actions: # Decides if player takes items or breaks an object in room
                if action[0] == "take" or action == "get": # Will put an item into from room
                    try:
                        except_ = action[1]
                        return action
                    except IndexError:
                        print("What item?")
                elif action[0] == "push": # Will push something in the room
                    try:
                        except_ = action[1]
                        return action
                    except IndexError:
                        print("Push what?")
                else:                     # Will break an oject in the room
                    try:
                        except_ = action[1]
                        return action
                    except IndexError:
                        print("Break what?")
            elif action[0] in item_use: # Will Consume or drop an item in a room
                try:
                    except_ = action[1]
                    for x in range(0, len(action)): # Used to search one list against another
                        # x Selects the item in input
                        for y in range(0, len(player_inv)): # y selects what to compare it to.
                            if action[x] == player_inv[y]:
                                return action[0], action[x]
                            else: # If nothing is found move to the next x
                                pass
                    else:
                        print("Item is not in Inventory")
                except IndexError:
                    print("What item?")

            elif action[0] == "inventory":
                player.checkInventory()

            elif action[0] == "yes" or action[0] == "no":
                return action

            else: # Will loop the prompt
                print("What?")

def dead(reason_failed, cause): # When the player dies will print a death message, Then exit
    print()
    cause = cause
    if cause == "fall":
        print("""
                .
                .
                .
                .
                .
                .
            .   .    .
              * V  *
            /\\/\\/\\/\\/\\
            \\ CRASH! /
        /\\/\\/\\/\\/\\/\\/\\/\\/\\
        """)
    elif cause == "crushed":
        print("""
            o    .      0
        * 0    *   .  o
      o     .             *
        *       .   o   .
     .     O        *       o.
       o       *       .
    0    .    o   O     *     .
       *            o        o
            /\\/\\/\\/\\/\\
            \\ CRASH! /
        /\\/\\/\\/\\/\\/\\/\\/\\/\\
        """)
    elif cause == "stabbed":
        print("""
   ___
 /     \\____ /_____________________________
 |  O  |    |   ___________________________\\
 \\ ___ /----|______________________________ /.
             \\                             . 0
                                            0
                                             0
        """)
    else:
        print()
    print(reason_failed)
    print("You have DIED, thus failing your quest...")
    exit(0)

    pass

def location(): # Will track the location of the player and what room's dialouge should be displayed
    pass
# Room data
def starting_cell(): # First room in game

    action_made = False # This will be used to allow the program to rerun the room if an error is detected
    walked_into_wall = False
    print("There is a row of bars before you, behind the bars sits a guard. The guard is")
    print("facing the other way from you. He has not yet noticed you. To your left is an")
    print("an unsuspecting set of climbable rocks leads up towards the light shining in.")
    print("It appears you may fit through it. To your right is an wall that appears to")
    print("be crumbling away. Perhaps with enough force it may collapse quiet enough for\nyou to escape.")
    print("What do you wish to do?")

    while not action_made:
        action = prompt(player.getInventory,False)
        if action[0] == "look" and action[1] == False: #Will rerun the room to allow
            print("There is a row of bars before you, behind the bars sits a guard. The guard is")
            print("facing the other way from you. He has not yet noticed you. To your left is an")
            print("an unsuspecting set of climbable rocks leads up towards the light shining in.")
            print("It appears you may fit through it. To your right is an wall that appears to")
            print("be crumbling away. Perhaps with enough force it may collapse quiet enough for\nyou to escape.")
        #else: # If anything other than look or check it will move to the next step
            #action_made = True

        if ("break" in action or "push" in action) and ("wall" in action or "right" in action or "east" in action):
            print("Your lanky form manages to push the rubble out of the way you are standing in")
            print("awe at the action you have just did. The ceiling above you begins to crumble.")
            print("Too much is falling and may crush you if you don't move out of the way")

            action = prompt(player.getInventory(), True)

            if ("evade" in action or "move" in action or "go" in action or "dodge" in action) and ("right" in action or "east" in action):
                print("")
                print("You have moved out of the way into a second cell...")
                action_made = True
                return True

            elif ("evade" in action or "go") in action and not "right" in action:
                print("You have evaded back towards the rocks....")
                dead("You have been crushed by the falling rocks.","crushed")

            else:
                print("You stand there, still in awe as the rocks come piling down.")
                dead("You have been crushed by the falling rocks.","crushed")

        elif "break" in action and not "wall" in action:
            print("Break what?")
        elif "push" in action and not "wall" in action:
            print("Push What?")
        elif ("go" in action) and ("right" in action or "east" in action):
            if not walked_into_wall:
                print("You walked into against the wall, knowing you cannot pass through it.")
                print("Maybe you should ask it to dinner first")
                walked_into_wall = True
            else:
                print("Maybe you shouldn't PUSH it... The wall may get upset.")
        elif (("climb" in action) and ("up" in action)) or (("go" in action or "move" in action) and "up" in action):
            climbing = True
            print("You begin to climb upwards")
            print("Some rocks appear to be unstable, do you wish to continue up?")

            while climbing:
                action = prompt(player.getInventory(), False)
                if ("yes" in action or ("climb" in action and "up" in action)) or (("go" in action) and "up" in action):
                    print("You have gotten closer to the hole, however it is still a narrow passage and\nit is getting harder to climb.")
                    action = prompt(player.getInventory(), False)
                    if (("climb" in action or "go" in action) and "up" in action):
                        print("You attempt to climb further up however you have lost your footing on the tiny\nrocks close to the exit.")
                        dead("You Have fallen from a great hight.","fall")
                    elif "down" in action:
                        print("You climb safely down!")
                        climbing = False
                    else:
                        print("You cannot do that while climbing..")
                elif climbing == True and ("down" in action or "no" in action):
                    print("You climb safely down!")
                    climbing = False
                else:
                    print("What?")
                    climbing = True

        elif "climb" in action and not ("up" in action):
            print("Climb what?")

        else:
            if action[1] == False:
                pass
            else:
                print("What?")

def second_cell():
    pass
def prison():
    pass
def hall():
    pass
def sword_room():
    pass
def knights_blocked_hall():
    pass
def fallen_rock_hall():
    pass
def cave_entrance():
    pass
def path():
    pass
def fire_path():
    pass
def troll_woods():
    pass
def pitfall():
    pass
def troll_toll_booth():
    pass
def bridge():
    pass
def castle_gate():
    pass
def throne_room():
    pass

# Execution of Game
def main():
    while True:
        screen_clear()

        start = Room(1,None)
        starting_cell()




main()
