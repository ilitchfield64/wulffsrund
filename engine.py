from sys import exit
from os import system, name
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

    def setPlayerPos(self, position): # This will change the room the player is currently in
        self.position = position

    def getPlayerPos(self): # This will return the player's position on the map
        return self.position

class Room: # This will construct the room's contents and maintain it's perminance

    def __init__(self, location, item): # Takes the location on the map, and if there is an item
        self.location = location # Will never need to change the location of the rooms
        self.item = item # Holds if an item is in the room
        player_has_entered = False # Checks to see if the room has been entered

        if "" == item: # Will check if any item is put into room. If "" i.e none, will not allow
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


def exampleRoomDialouge(room_pos, player_has_entered, ): # Example on how room dialouge should be made in conjunstion with a room's object
    # If player has not entered
        #print long dialouge
    # else print short dialouge
    pass
def start(room_location,player_has_entered):

    pass
def location(): # Will track the location of the player and what room's dialouge should be displayed
    pass

def prompt(): # All keywords will be handled by the prompt and simplified for the enigine
    verbs = ["go", "walk", "climb", "jump", "take", "sneak", "stab", "attack", "kill", "confront", "push", "break", "evade", "look" , "check"]
    compass_directions = ["north","south","east","west"] # Ordered so the first letter of each direction may be used.
    ### want to make it pop out articles (the, at, etc.) and return the data back to be processed?
    verbal_dirctions = ["up", "down", "right", "forward", "back", "left"]
def screen_clear(): # Clears the screen
    if name == "nt":
        _ = system("cls") # Detects is windows to use NT cls to clear screen
        pass
    else:
        _ = system("clear") # *nix OSes use clear
def main():
    screen_clear()
    starting_room = Room(0,"")
    player =Player()
    start = Room(0,"Wand")
    room1 = Room(1,"")
    print("taking item from room 1")
    player.putInInventory(start.takeItem())
    print("trying to take item a second time")
    player.putInInventory(start.takeItem())
    print("Checking Inventory")
    player.checkInventory()
    print("trying to put item from a room lacking an item")
    player.putInInventory(room1.takeItem())
    player.checkInventory()


main()
