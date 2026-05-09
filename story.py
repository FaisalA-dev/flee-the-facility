#1ST MAIN ROUTE 


from security import log_event, save_game
from inventory import add_item,show_inventory









def impersonate_route():
    print("\nAfter much thought you have went with choice 1. To impersonate the security guard.")
    print("You quietly step into the hallway and look for any possible way to steal a badge.")

    #pt 2 
    print ("\n You notice 1. a security guard room with no lock 2. a bathroom with lockers.")
    choice = input("Where will you go? (1 or 2): ")
    if choice == "1":
        print("\n You sneak into the bathroom and search the guards bags for their uniforms and security badges.")
        print("\n After searching multiple bags your able to find one bag that has an old slightly ripped security uniform and another bag with a locked phone ")
        add_item("Security Uniform")
        add_item("Locked Phone")
        print("\n You hear footsteps approaching")
    elif choice == "2":
        print("\n You sneak into the security guard room in hopes to find any possible badges, keys, or uniforms.")
        print("\n You search through the security room and find a security badge and see the CCTV someone is on the way.")
        add_item("Security Badge")
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



        show_inventory()
        print("\nENDING: You are caught before reaching the exit.")

    else:
        print("\nInvalid choice.")
        



















#2ND MAIN ROUTE
def blackout_route():
    print("\nIn quick thought you decided to make a run for it into the dark hallway.")
    print("You decide to open the door and jolt for it into the lightless hallway.")
    print("You made too much noice and an alarm started ringing.")

    #pt 2
    print("\nAs you run you see two paths to take:")
    print("1. Red flashing lights down the hallway")
    print('2. A dark hallway with no light and a "DO NOT ENTER" sign')

    choice = input("Which path will you take? (1 or 2): ")

    if choice == "1":
        print("\nYou take the emergency light path.")
        print("There are guards near that you can hear.")

    elif choice == "2":
        print("\nYou move through the dark hallway with no light and see not much.")
    else:
        print("\nInvalid choice. Please choose 1 or 2.")

    #pt 3
    print("\nWhat will you do now?")
    print("1. Continue moving forward carefully")
    print("2. Hide and wait")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nYou keep searching for any type of exit or just anywhere to leave where you are now.")
        print("successfully you finaly found something. a broken door nearby that seems like it wasn't used in awhile.")
        add_item("Flashlight")

    elif choice == "2":
        print("\nYou hide nearby and wait patiently.")
        print("You realize this plan won't work and they will just keep looking...")

    else:
        print("\nInvalid choice. Please choose 1 or 2.")

    #pt 4
    print("\nYou finally find what looks to be an old emergency exit.")

    print("The door is old and slightly damaged but still slightly open.")

    print("What will you do?")
    print("1. Go through the damaged exit door")
    print("2. Be patient and try to find another chance")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nCongrats!! you found a way out and you were able to escape the facility.")

        print("\nTHE END: You successfully made it out through the exit.")

    elif choice == "2":
        print("\nWhile hiding and trying to find another way a security guard with a guard dog eventually finds you.")
        print("the guard asks what you're doing...")

        print("\nWhat do you say?")
        print("1. tell them your part of maintenance")
        print("2. Explain the situation and how you did nothing wrong and you just want to leave")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nThe guard asks for your ID but you dont have one.")
            show_inventory()
            print("\nENDING: The guard realizes your lying and detains you.")

        elif choice == "2":
            print("\nYou begin stuttering and panicking while trying to explain yourself.")
            print("The guard loses any bit of trust.")
            show_inventory()
            print("\nENDING: You are detained by security.")
        else:
            print("\nInvalid choice.")
            show_inventory()





























#3RD MAIN ROUTE
def hacking_route():
    print("\nYou decide to go through the hacking route.")
    print("You see a damaged security screen on the wall still powered on for some odd reason.")
    print("You quickly move toward the terminal before anyone could catch you.")
    
    print("\nYou have two options to pick through:")
    print("1. Attempt to disable the security locks")
    print("2. Hack into the facility mainfraim and wipe your existence")

    choice = input("What will you do? (1 or 2): ")

    if choice == "1":
        print("\nYou try to disable the facility electronic security locks.")
        print("The terminal begins making loud fan noise.")

    elif choice == "2":
        print("\nYou search through the facility system files and try to specifically search for your name.")
        print("You somehow manage to find a set of files that are specific to you.")
        add_item("Personal Files")
    else:
        print("\nInvalid choice. Please choose 1 or 2.")
        
    print("\nYou can hear a security guard coming by...What will you do now?")
    print("1. Continue using the terminal")
    print("2. Leave all your hard work behind before security arrives")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nYou have unlocked the security locks and turned off any alarms that could be used.")
        print("Your now close to making an exit.")

    elif choice == "2":
        print("\nYou leave the terminal and attempt to escape before security arrives.")
        print("Unfortunately you dont finish in time...")

    else:
        print("\nInvalid choice. Please choose 1 or 2.")
    print("\nYou now see an emergency exit unlocked nearby.")

    print("What will you do?")
    print("1. Escape as soon as possible")
    print("2. Try erasing more files on yourself")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nYou quickly escape through the unlocked emergency exit.")

        print("\nTHE END: You successfully escape the facility with no one knowing, no alerts, no alarms. Congrats on escaping!.")

    elif choice == "2":
        print("\nWhile downloading files, a security guard sees you and walks up.")
        print("The security guard asks why your accessing restricted facility files...")

        print("\nWhat will you say?")
        print("1. Try to convince them your fixing something")
        print("2. Be honest and tell the truth on how you don't know why your here and you're trying to escape")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nThe guard asks for your credentials.")
            print("You can't provide any.")
            show_inventory()
            print("\nENDING: Security is alerted and you are detained.")
        elif choice == "2":
            print("\nThe guard instantly calls for backup after hearing your explanation.")
            show_inventory()
            print("\nENDING: You are detained before escaping.")

        else:
            print("\nInvalid choice.")

    else:
        print("\nInvalid choice.")
        show_inventory()
























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
            save_game("impersonate_route")
            log_event("CHOICE_IMPERSONATE")
            impersonate_route()
            break

        elif choice == "2":
            save_game("blackout_route")
            log_event("CHOICE_BLACKOUT")
            blackout_route()
            break

        elif choice == "3":
            save_game("hacking_route")
            log_event("CHOICE_HACKING")
            hacking_route()
            break

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.")