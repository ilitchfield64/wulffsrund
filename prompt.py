from sys import exit

def prompt(player_inv): # All keywords will be handled by the prompt and simplified for the enigine

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


## PRIVATE METHODS ##
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
            print("Invalid Direction")
            return False,None

    def createMove(list, direction): # Takes in a tupple from whatDirection to return a movement to main execution
        print(list)
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
            exit(0)

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
                    return action # Will look at specific entities in room for a little more detail. action returned is room specific

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
                    exit(0)
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
                    exit(0)
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
                    return action
                except IndexError:
                    print("Evade what?")

        elif action[0] in actions:
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
                        else: # If nothing is found moce to the next x
                            pass

                else:
                    print("Item is not in Inventory")
            except IndexError:
                print("What item?")

        else: # Will loop the prompt
            print("What?")

inv = ["sword"]
while True:

    outcome = prompt(inv)
    print(f"{outcome} is returned by the prompt")
