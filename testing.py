from sys import exit

def prompt(): # All keywords will be handled by the prompt and simplified for the enigine

## DECLARARTIONS ##
    #verbs = ["go", "walk", "move", "climb", "jump", "take", "sneak", "stab", "attack", "kill", "confront", "push", "break", "evade", "dodge", "look" , "check", "help", "quit", "exit", "leave"]
    special =["help", "look", "check"]
    exits = ["quit", "exit", "leave"]
    movement = ["go", "walk", "move", "climb", "jump"]
    attacks = ["attack", "stab", "hit", "kill", "confront"]
    dodge = ["dodge", "evade", "avoid"]
    actions = ["take", "push", "break"]
    modifier = ["sneak", "stealth"]
    compass_directions = ["north", 'n', "south", 's', "east", 'e', "west", 'w']
    verbal_dirctions = ["up", "down", "right", "forward", "back", "left"]

    sneak = False


## PRIVATE METHODS ##
    def whatDirection(list): # Will cycle through the inputed list and find if there is a direction, and what direction if so
        print("What Direction")
        i = 0
        try: # This method may return an IndexError
            while i < 5: # Instead of checking the entire list it will check up to 5 words ie go quickly out the left | door
                if list[i] in compass_directions: #
                    print("In compass Directions")
                    return True, list.pop(i)
                elif list[i] in verbal_dirctions:
                    print("In verbal_dirctions")
                    return True, list.pop(i)
                else:
                    i = i+1
            print("Invalid Direction")
            return False,""
        except IndexError: # If the command is < 5 the program will create an exception to checking by the length of the list
            for i in range(0, len(list)):
                if list[i] in compass_directions: #
                    print("In compass Directions")
                    return True, list.pop(i)
                elif list[i] in verbal_dirctions:
                    print("In verbal_dirctions")
                    return True, list.pop(i)
                else:
                    pass
            print("Invalid Direction")
            return False,""

    def createMove(direction): # Takes in a tupple from whatDirection to return a movement to main execution
        if direction[0]: # Returns a direction to move in
            movement = ["move"]
            movement.append(direction[1])
            return movement
        else: # No direction entered which leads to a new prompt.
            print("No Direction entered")
            return False

## EXECUTION OF CODE ##
    # Takes in the user input to check the action
    while True:
        action = input("> ")
        action = action.lower()
        action = action.split(" ")
        print(f"{action} was entered")
        if action[0] in modifier: # Checks to see if sneak is in sentance
            print
            sneak = True
            action.pop(0)
        else:
            pass

        try: # Will protect the program from crashing if sneak is the only word typed
            exception = action[0]
            del exception
        except IndexError:
            print("Had IndexError")
            action.append("") # Puts empty data into the list to continue the loop without crashing

        if action[0] in exits: # Will Exit the program
            print("Exiting Program")
            exit(0)
        elif action[0] in special:
            pass
        elif action[0] in movement: # Returns what room to move to
            action = (createMove(whatDirection(action)))
            if not action:
                pass
            else:
                print(action)

                return action
        elif action[0] in attacks: # Returns what to attack
            print(f"{action} in attacks")
            pass
        elif action[0] in dodge: # Returns what to evade
            print(f"{action} in dodge")
            pass
        elif action[0] in actions: # Returns what to break/push
            print(f"{action} in actions")
            pass
        else: # Will loop the prompt
            print("What?")


outcome = prompt()
print(f"{outcome} is returned by the prompt")
