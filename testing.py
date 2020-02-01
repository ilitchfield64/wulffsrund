def prompt(): # All keywords will be handled by the prompt and simplified for the enigine
    special =["help", "look", "check"]
    verbs = ["go", "walk", "move", "climb", "jump", "take", "sneak", "stab", "attack", "kill", "confront", "push", "break", "evade", "dodge", "look" , "check", "help"]
    movement = ["go", "walk", "move", "climb", "jump"]
    attacks = ["attack", "stab", "hit", "kill", "confront"]
    dodge = ["dodge", "evade", "avoid"]
    actions = []
    modifier = []
    compass_directions = ["north","south","east","west"] # Ordered so the first letter of each direction may be used.
    verbal_dirctions = ["up", "down", "right", "forward", "back", "left"]

    choice = input("> ")
    choice = choice.lower()


    def splitChoice(string):
        return string.split(" ")

    def checkVerb(list): # Checks to see if sentenece begins with a verb keyword
        if list[0] in verbs:
            return True
        else:
            return False
    if checkVerb(splitChoice(choice)):
        print("True test")
        list = splitChoice(choice)
        for i in splitChoice(choice):
            #list = splitChoice(choice)
            popped = list.pop(0)
            print(popped)
            if popped in compass_directions:
                print("In compass Directions")
            elif popped in verbal_dirctions:
                print("In verbal_dirctions")
            else:
                print("Not in directions")
    else:
        print("Not in list")


prompt()
