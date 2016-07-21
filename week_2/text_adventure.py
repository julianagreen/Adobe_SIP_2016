print ("You wake up one morning and find that you are not in your bed, you are not even in your room! You are in the middle of a giant maze. There is a hallway to your right and to your left. Last thing: you can only leave through the marked exit")


forward_back = input("Type 'backward' to go turn back or 'forward' to go ahead. ")

while (forward_back != "backward" and forward_back != "forward"):
    print(" ")
    print("try again. Please type either forward or back")
    forward_back = input("Type 'backward' to go turn back or 'forward' to go ahead. ")


if forward_back == "backward":
    print(" ")
    print("You are a coward, you loose")

elif forward_back == "forward":
    print(" ")
    print("Onward! You survived the first task")
    left_right = input("You encounter a fork, left or right? ")

    while (left_right != "left" and left_right != "right"):
        print(" ")
        print("try again. Please type either left or right")
        left_right = input("You encounter a fork, left or right? ")

    if left_right == "left":
        up_down = input("there is a ladder going into a hole in the ground and up out of the maze, would you like to go up or down? ")
        
        while (up_down != "up" and up_down != "down"):
            print(" ")
            print("please try again, type either up or down")
            up_down = input("there is a ladder going into a hole in the ground and up out of the maze, would you like to go up or down? ")

        if up_down == "up":
            print(" ")
            print("You climb up to see whe whole maze to look for the exit")
            print(" ")
            print("THAT IS CHEATING - YOU LOOSE. Read the instructions next time")
        elif up_down == "down":
            print(" ")
            print("you find yourself in an underground chamber. There is a guy who tries to show you a trick")
            stop_ignore = input("Would you like to 'stop and talk' or 'ignore'? ")

            while (stop_ignore != "stop and talk" and stop_ignore != "ignore"):
                print(" ")
                print("please try again, type either stop and talk or ignore")
                stop_ignore = input("Would you like to 'stop and talk' or 'ignore'? ")

            if stop_ignore == "ignore":
                print(" ")
                print("Wow, he feels hurt and lonely, as you walk away, he shoots you")
            elif stop_ignore == "stop and talk":
                head_tail = input("he flips a coin and asks you heads or tails? ")

                while (head_tail != "heads" and head_tail != "tails"):
                    print(" ")
                    print("please try again, type either heads or tails")
                    head_tail = input("he flips a coin and asks you heads or tails? ")


                if head_tail == "heads":
                    print(" ")
                    print("the right answer is ALWAYS tails, you loose")
                elif head_tail == "tails":
                    print(" ")
                    print("Great, you win! The guy was a millionare and gives you his fifth home and a million dollars in exchange for being his friend, CONGRATS :) He also shows you the exit")
    elif left_right == "right":
        print(" ")
        print("you encounter a chicken with a power saw")
        fight_flight = input("fight or flight? ")

        while (fight_flight != "fight" and fight_flight != "flight"):
            print(" ")
            print("please try again, type either fight or flight")
            fight_flight = input("fight or flight? ")

        if fight_flight == "fight":
            print(" ")
            print("well that was dumb, obviously the chicken won")
        elif fight_flight == "flight":
            print(" ")
            print("YooHoo! You just barely escaped")
            relax_struggle = input("You run into a massive pool of quicksand-like vines, there is a sign above indicating this thing is devil's snare. It is very quickly restraining you and pulling you in, do you choose to struggle or relax? ")
            
            while (relax_struggle != "relax" and relax_struggle != "struggle"):
                print(" ")
                print("please try again, type either relax or struggle")
                relax_struggle = input("You run into a massive pool of quicksand-like vines, there is a sign above indicating this thing is devil's snare. It is very quickly restraining you and pulling you in, do you choose to struggle or relax? ")

            if relax_struggle == "struggle":
                print(" ")
                print("You need to brush up on your Harry Potter facts, nice try. YOU LOOSE")
            elif relax_struggle == "relax":
                print(" ")
                print("Great, you are a true Harry Potter fan (or a lucky guesser)")
                toward_away = input("You see the exit, but it is being guarded by a three-headed dog - type toward to move toward it or away to look for another way out ")
                
                while (toward_away != "toward" and toward_away != "away"):
                    print(" ")
                    print("please try again, type either toward or away")
                    toward_away = input("You see the exit, but it is being guarded by a three-headed dog. Type toward to move toward it or away to look for another way out ")

                if toward_away == "toward":
                    print(" ")
                    print("HI, is this working?")
                    sing_pet = input("how would you like to defeat the dog, sing to it, pet it, just type sing or pet ")
                    
                    while(sing_pet != "sing" and sing_pet != "pet"):
                        print(" ")
                        print("please try again, type either sing or pet")
                        sing_pet = input("how would you like to defeat the dog, sing to it, pet it (just type sing or pet)")

                    if sing_pet == "pet":
                        print(" ")
                        print("You loose, the dog ate your head off")
                    elif sing_pet == "sing":
                        print(" ")
                        print("good job, you made it out of the maze! :)")
                elif toward_away == "away":
                    print(" ")
                    print("you spent too much time in the maze and went crazy, you loose")

