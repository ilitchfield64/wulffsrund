"""
Last thing worked on, need to pop items in the list and compare them against the accepted values in master lists
list[index] in another_list returns an error
Must pop off list and check with a for loop?

define a listPopChecker(takeInList,  wanted index)
    pop off each and check against the master lists
    if not in list a move to next list until found
    create a string to return for further processing?

I need to write a method that will take in a list, compare that data to another list,
and then perform an action based on that comparison.
"""
from sys import exit
def prompt(): # All keywords will be handled by the prompt and simplified for the enigine

## DECLARARTIONS ##
    # The commented lists will be added when I learn how to check them in a easy to read manner
    special =["help", "look", "check"]
    exits = ["quit", "exit", "leave"]
    verbs = ["go", "walk", "move", "climb", "jump", "take", "sneak", "stab", "attack", "kill", "confront", "push", "break", "evade", "dodge", "look" , "check", "help", "quit", "exit"]
    #movement = ["go", "walk", "move", "climb", "jump"]
    #attacks = ["attack", "stab", "hit", "kill", "confront"]
    #dodge = ["dodge", "evade", "avoid"]
    #actions = ["take", "push","break"]
    #modifier = ["sneak", "stealth"]
    compass_directions = ["north","south","east","west"] # Ordered so the first letter of each direction may be used.
    verbal_dirctions = ["up", "down", "right", "forward", "back", "left"]



## PRIVATE METHODS ##
    def splitToList(string): # will split the user input to a list
        return string.split(" ")

    def checkIfVerb(list): # Checks to see if sentenece begins with a verb keyword
        if list[0] in verbs:
            return True
        else:
            return False
    def whatVerb(): # If is_verb is true it will figure what verb and simplify it to return to the room module
        if list[0] in exits:
            ifQuit()
        else:
            pass

    def whatDirection(list): # Will cycle through the inputed list and find if there is a direction, and what direction if so
        list = list
        for i in list:
            #list = splitToList(action)
            popped = list.pop(0)
            print(popped)
            if popped in compass_directions:
                print("In compass Directions")
            elif popped in verbal_dirctions:
                print("In verbal_dirctions")
            else:
                print("Not in directions")
    def ifQuit():
        print("Quitting")
        exit(0)
    #def
## EXECUTION OF CODE ##
    # Takes in the user input to check the action
    while True:
        action = input("> ")
        action = action.lower()
        action_list = action.split(" ")
        print(action_list[0])
        if checkIfVerb(splitToList(action)): # should return true if the first word typed is a keyword
            print("True test")
            whatVerb() # call to the what verb
        else: # If first word is not a verb, will prevent the prompt from returning to the room module
            print("Not in any list") # debugging
            pass


prompt()
