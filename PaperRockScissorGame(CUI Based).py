from random import *
opt=["paper","rock","scissor"]
userscore = 0
compscore = 0

def game(userscore,compscore):
    print(f"The option choosed by you is {uchoosed} and computer choosed {compchoice}")
    if compchoice == uchoosed:
        userscore +=1
        compscore +=1
        print("The match between you and computer is tied")
        print(f"User score {userscore} \tComputer Score {compscore}")
    elif (uchoosed == "paper" and compchoice == "rock") or (uchoosed == "rock" and compchoice == "scissor") or (uchoosed == "scissor" and compchoice == "paper"):
        userscore +=1
        print("You Won")
        print(f"User score {userscore} \tComputer Score {compscore}")
    else:
        compscore +=1
        print("Computer Won")
        print(f"User score {userscore} \tComputer Score {compscore}")
    return userscore,compscore

while True:
    user_input=eval(input('''
                    Game Start.....
                    1 Yes! To Play 5 Round.
                    2 No! For Exit From The Game.
                                '''))
    if user_input == 1:
        for round in range(5):
            print("\n"f"The {round+1} round",end="")
            userchoice=eval(input('''
                            Choose only one option via menu number mentioned below:
                            1 Paper
                            2 Scissor
                            3 Rock
                                '''))
            if userchoice == 1:
                    uchoosed = "paper"
            elif userchoice == 2:
                    uchoosed = "scissor"
            elif userchoice == 3:
                    uchoosed = "rock"
            else:
                print("Invalid Choice! Select Again.")                
                # round -=1
                continue     
            compchoice=choice(opt)
            # game(uchoosed,compchoice)
            # def game(userscore,compscore):
            # return userscore,compscore
            print(f"The option choosed by you is {uchoosed} and computer choosed {compchoice} in {round+1} round")
            if compchoice == uchoosed:
                userscore +=1
                compscore +=1
                print("The match between you and computer is tied")
                print(f"User score {userscore} \tComputer Score {compscore}")
            elif (uchoosed == "paper" and compchoice == "rock") or (uchoosed == "rock" and compchoice == "scissor") or (uchoosed == "scissor" and compchoice == "paper"):
                userscore +=1
                print("You Won")
                print(f"User score {userscore} \tComputer Score {compscore}")
            else:
                compscore +=1
                print("Computer Won")
                print(f"User score {userscore} \tComputer Score {compscore}")
        print("\n"f"The final score of match after 5 rounds is: Your score {userscore} & Computer score {compscore}")
        if userscore == compscore:
            print("The match between you and computer are drawn")
        elif userscore > compscore:
            print("The User Won The Match")
        else:
            print("The Computer Won The Match")
    elif user_input == 2:
        break
    else:
        print("Invalid Choice! Select Valid Value")