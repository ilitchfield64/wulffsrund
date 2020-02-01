from sys import exit
from os import system, name

def screen_clear():
    if name == "nt":
        _ = system("cls") # Detects is windows to use NT cls to clear screen
        pass
    else:
        _ = system("clear") # *nix OSes use clear
        pass
def prompt(): #The choices made throughout the program will be checked here to see if the nouns and verbs are allowed
    # KEYWORDS
    #     actions = ["go", "walk", "climb", "take", "sneak", "stab", "attack", "kill", "confront", "push", "break", "evade", "look", "jump"]
    #     directions = ["north", "n", "south", "s", "east", "e", "west", "w", "up", "down", "left", "right"]
    #     items = ["key","sword","medallion","flint","ivory"]
    input_wrong = True #This will keep prompt returning if input doesn't match keywords

    while input_wrong:
        choice = input("> ")
        choice = choice.lower() # takes input to lowercase for engine handling
        #choice = choice.split(" ") # It simply doesn't make sense to make the input a list
        print("")

        if "quit" in choice or "exit" in choice: # Will ask to quit program
            print("quit") #debug

# COMMENTED OUT FOR DEBUGGING #########################################################
            #print("Are you sure you wish to abandon your quest? Say YES if you are...")
            #quit = input(">!!: ")

            #if quit == "YES": # will instantly kill Character ending program
            dead("You abandon your quest by commiting suicide...","stabbed")
            #else: #
            #    print("That was close. Phew...")
            #    input_wrong = True

        elif choice== "help":
            print("____ is a simple game with only two rules. Have fun and type properly.")
            print("The prompt accepts full sentences, looking for certain keywords. The keywords")
            print("are go, walk, climb, take, sneak, stab, attack, kill, confront, push, break,")
            print("evade, look, jump. Some games allow synonyms however this one does not.")
            print("Please enter an action followed by a noun wherever needed. Look, and check")
            print("when typed alone will print the contents of the room again. If typed with")
            print("anything else, it may perform another action.")
            input_wrong = True

        elif choice == "clear":
            screen_clear()

        elif "go" in choice or "walk" in choice or "climb" in choice:
            #print("go") # debug
            if "north" or "south" or "east" or "west" or "up" or "down" or "left" or "right" in choice:
                    return choice
            else:
                    print("What direction?")
                    input_wrong = True

        elif "take" in choice or "use" in choice:
            #print(" Take") # debug
            if "key" in choice or "sword" in choice or "medallion" in choice or "flint" in choice or "ivory" in choice:
                    #print("take") #debug
                    return choice
            else:
                print("What Item?")

        elif "stab" in choice or "attack" in choice or "kill" in choice:
            #print("stab") # debug
            if "self" in choice:
                dead("You idiot you killed yourself...","stabbed")
            else:
                return choice
        elif "stand" in choice or "sneak" in choice or "confront" in choice or "push" in choice or "break" in choice or "evade" in choice or "look" in choice or "check" in choice or "jump" in choice:
            #print("other") #debug
            return choice
        else:
            #print("else") #debug
            return choice
    #    else:
    #        print("What?")
    #        input_wrong = True

    print("out of loop?") # debug

def starting_cell():
    action_made = False # This will be used to allow the program to rerun the room if an error is detected
    walked_into_wall = False
    print("There is a row of bars before you, behind the bars sits a guard. The guard is")
    print("facing the other way from you. He has not yet noticed you. To your left is an")
    print("an unsuspecting set of climbable rocks leads up towards the light shining in.")
    print("It appears you may fit through it. To your right is an wall that appears to")
    print("be crumbling away. Perhaps with enough force it may collapse quiet enough for\nyou to escape.")
    print("What do you wish to do?")

    while not action_made:
        action = prompt()
        if action == "look" or action == "check": #Will rerun the room to allow
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

            action = prompt()

            if ("evade" in action or "move" in action or "go" in action) and ("right" in action or "east" in action):
                print("")
                print("You have moved out of the way into a second cell...")
                action_made = True
                pass

            elif ("evade" or "move") in action and not "right" in action:
                print("You have evaded back towards the rocks....")
                dead("You have been crushed by the falling rocks.","crushed")

            else:
                print("You stand there, still in awe as the rocks come piling down.")
                dead("You have been crushed by the falling rocks.","crushed")

        elif "break" in action and not "wall" in action:
            print("Break what?")
        elif "push" in action and not "wall" in action:
            print("Push What?")
        elif ("go" in action or "walk" in action or "move" in action) and ("right" in action or "east" in action):
            if not walked_into_wall:
                print("You walked into against the wall, knowing you cannot pass through it.")
                print("Maybe you should ask it to dinner first")
                walked_into_wall = True
            else:
                print("Maybe you shouldn't PUSH it... The wall may get upset.")
        elif (("climb" in action) and ("rock" in action or "wall" in action or "up" in action)) or (("go" in action or "move" in action) and "up" in action):
            climbing = True
            print("You begin to climb upwards")
            print("Some rocks appear to be unstable, do you wish to continue up?")

            while climbing:
                action = prompt()
                if ("yes" in action or ("climb" in action) and ("rock" in action or "wall" in action or "up" in action)) or (("go" in action or "move" in action) and "up" in action):
                    print("You have gotten closer to the hole, however it is still a narrow passage and\nit is getting harder to climb.")
                    action = prompt()
                    if (("climb" in action or "go" in action or "move" in action) and "up" in action) or ("climb" in action and "rock" in action):
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

        elif "climb" in action and not ("up" in action or "rock" in action):
            print("Climb what?")

        else:
            print("What?")

def second_cell():
    print()
def prison():
    print()
def hall():
    print()
def sword_room():
    print()
def knights_blocked_hall():
    print()
def fallen_rock_hall():
    print()
def cave_entrance():
    print()
def path():
    print()
def fire_path():
    print()
def troll_woods():
    print()
def pitfall():
    print()
def troll_toll_booth():
    print()
def bridge():
    print()
def castle_gate():
    print()
def throne_room():
    print()
def dead(reason_failed, cause):
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


def main():

    running = True
    print("You awaken in a dark and dreary hole. There is a light coming from above you,")
    print("it appears to be dark as if it were some sort of cave. You climb out of the")
    print("shallow hole that seemed to fit your stature just a little to tight. A mild\ndiscomfort grows in your back.")

    starting_cell()
screen_clear()
main()
