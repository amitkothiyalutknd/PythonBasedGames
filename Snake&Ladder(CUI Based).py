import random

class Steps():
    def __init__(self, playerScore = 0, computerScore = 0):
        self.playerScore = playerScore
        self.computerScore = computerScore
        
    def check(self, user):
        if user == 2:
            user += 21
            print("User Moves 21 Ladder's Steps Ahead.")
        elif user == 8:
            user += 4
            print("User Moves 4 Ladder's Steps Ahead.")
        elif user == 17:
            user += 76
            print("User Moves 76 Ladder's Steps Ahead.")
        elif user == 29:
            user += 25
            print("User Moves 25 Ladder's Steps Ahead.")
        elif user == 32:
            user += 19
            print("User Moves 19 Ladder's Steps Ahead.")
        elif user == 39:
            user += 41
            print("User Moves 42 Ladder's Steps Ahead.")
        elif user == 62:
            user += 16
            print("User Moves 16 Ladder's Steps Ahead.")
        elif user == 70:
            user += 19
            print("User Moves 19 Ladder's Steps Ahead.")
        elif user == 75:
            user += 21
            print("User Moves 21 Ladder's Steps Ahead.")
        elif user == 99:
            user -= 95
            print("User Falls 95 Steps Behind By Snake bite.")
        elif user == 92:
            user -= 16
            print("User Falls 16 Steps Behind By Snake bite.")
        elif user == 83:
            user -= 3
            print("User Falls 3 Steps Behind By Snake bite.")
        elif user == 67:
            user -= 17
            print("User Falls 17 Steps Behind By Snake bite.")
        elif user == 59:
            user -= 22
            print("User Falls 22 Steps Behind By Snake bite.")
        elif user == 41:
            user -= 21
            print("User Falls 21 Steps Behind By Snake bite.")
        elif user == 31:
            user -= 17
            print("User Falls 17 Steps Behind By Snake bite.")
        return user

    def game(self):
            userDice = random.randint(1, 6)
            computerDice = random.randint(1, 6)
            print(f"Player Dice Score is {userDice} And The computer Dice Score is {computerDice}.")

            if self.playerScore == 0 and userDice == 6:
                self.playerScore += 1
            elif self.playerScore != 0 or self.playerScore > 0:
                self.playerScore =  self.playerScore + userDice
                if self.playerScore >= 100:
                    print("The Player Scored 100 First. Congratulation! Player Has Won.")
                    exit()
                else:
                    self.playerScore = self.check(self.playerScore)
        
            if self.computerScore == 0 and computerDice == 6:
                self.computerScore += 1 
            elif self.computerScore != 0 or self.computerScore > 0:
                self.computerScore = self.computerScore + computerDice
                if self.computerScore >= 100:
                    print("The Computer Scored 100 First. Computer Won. Hard Luck. Try Once Again.")
                    exit()
                else:
                    self.computerScore = self.check(self.computerScore)   
        
            print(f"After {playTimes} Chance \nPlayer Score:{self.playerScore}  \tComputer Score:{self.computerScore}.")

if __name__ == "__main__":
    while True:
        user_input = int(input('''
                    --------------------Snakes & Ladders Game--------------------
                    1 Yes! To Play Snakes & Ladders Game With Computer.
                    2 No! For Exit From The Game.
                                '''))
        if user_input == 1:
            playTimes = 0
            print("The Initial Score Of Both Player And Computer is: 0")
            snakeLadder = Steps()
            while True:
                userchoice = (input('''
                            Press 'P' To Play Dice and 'S' To Stop The Games.'''))
                if userchoice.lower() == 'p':
                    playTimes +=1
                    snakeLadder.game()
                elif userchoice.lower() == 'e':
                    break
                else:
                    print("Invalid Choice! Select Valid Value. Press 'P' To Play Again & 'E' For Exit.")
                    continue
        elif user_input == 2:
            break
        else:
            print("Invalid Choice! Select Valid Value.")
            continue