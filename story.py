def impersonate_route():
    print("\nAfter much thought you have went with choice 1. To impersonate the security guard.")
    print("You quietly step into the hallway and look for any possible way to steal a badge.")

    #pt 2 
    print ("\n You notice 1. a security guard room with no lock 2. a bathroom with lockers.")
    choice = input("Where will you go? (1 or 2): ")
    if choice == "1":
        print("\n You sneak into the bathroom and search the guards bags for their uniforms and security badges.")
        print("\n After searching multiple bags your able to find one bag that has an old slightly ripped security uniform and another bag with a locked phone ")
        print("\n You hear footsteps approaching")
    elif choice == "2":
        print("\n You sneak into the security guard room in hopes to find any possible badges, keys, or uniforms.")
        print("\n You search through the security room and find a security badge and see the CCTV someone is on the way.")
    else:
        print("\n Invalid choice. Please choose 1 or 2.")


    #pt 3
    print("\nWhat will you do now?")
    print("Choice 1: Hide and wait for the guards to leave")
    print ("Choice 2 : Try to leave before they get here")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("\n You hide in the security room and wait for the guards to leave.")
        print("\n After a few minutes the guards leave and you sneak out of the security room and into the hallway.")
    elif choice == "2":
        print("\n You quickly try to leave before the guards get here but they catch you and you are forced to hide in the security room.")
        print("\n After a few minutes the guards leave and you are able to sneak out of the security room and into the hallway.")
    else:
        print("\n Invalid choice. Please choose either 1 or 2.")


    #pt4 

    print("\nYour now going in hallway you eventually reach an employee gate near the end of the hall.")

    print("Two guards stand near the entrance checking employee badges.")
    print("You know this may be your only chance to leave the facility.\n")
    print("What will you do?")
    print("1. Try to swiftly and sneakily walk through the security checkpoint")
    print("2. Wait and listen to the guards conversation")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nYou try to sneakily walk through the security gate avoiding eye contact and you have your badge on.")
        print("One of the security guards looks at your badge before telling you \"your good\".")
        print("\nTHE END: You escape through the security gate disguised as staff and walk free.")

    elif choice == "2":
        print("\nYou wait nearby and hear the guards talking about more strict protocols. You decide you should put on your outfit before you go through the checkpoint ")
        print("While preparing, another security guard catches you redhanded...")




        print("\nENDING: You are caught before reaching the exit.")

    else:
        print("\nInvalid choice.")









def blackout_route():
    print("\nIn quick thought you decided to make a run for it into the dark hallway.")
    print("You quickly open the door and sprint into the hallway.")


def hacking_route():
    print("\nYou decide to go through the hacking route.")
    print("You notice a damaged security screen on the wall still powered on.")


def start_story():
    print("FLEE THE FACILITY!")
    print("Your eyes open and you find yourself in a room you've never been before. You're confused but you see there are guards outside the door. You need to find a way out of this place.")
    print("Your eyes wonder around and you see your in a room but it's unlocked you believe a guard forgot to lock it.")

    print("\nYou now have to make a choice on what to do next. Do you want to next...")
    print("1. Figure out a way to impersonate a security guard and sneak out?")
    print("2. Make a run for it into a dark hallway and hope to find an exit?")
    print("3. Figure out a way to access a terminal and override the security system to open the doors without an alert?")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            impersonate_route()
            break

        elif choice == "2":
            blackout_route()
            break

        elif choice == "3":
            hacking_route()
            break

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.")