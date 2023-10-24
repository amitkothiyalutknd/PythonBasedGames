import random
import time
import numpy as ny

class Ludo():
    def __init__(self, player = [], computer = [], playScore = {}, computerScore = {}):
        self.player, self.computer, self.initialValues  = [], [], [0 for initialvalue in range(4)]
        self.playerScore, self.computerScore = {}, {}
        self.playerToken, self.computerToken = globals(), globals()        
        for token in range(4):
            self.playerToken["PlyrToken%d" % (token+1)] = int()
            self.player.append("PlyrToken{0}".format(token+1))
            self.computerToken["CmptrToken%d" % (token+1)] = int()
            self.computer.append("CmptrToken{0}".format(token+1))
        for key, value in zip(self.player, self.initialValues):
            self.playerScore[key] = value
        for key, value in zip(self.computer, self.initialValues):
            self.computerScore[key] = value
        # print([val for val in self.player], [val for val in self.computer]) #MethodA
        # print(self.player, self.computer) #MethodB  (Method A & B are printing the same thing.)
        # print(self.playerScore, self.computerScore)
        self.playerTokenTrack, self.computerTokenTrack = globals(), globals()
        for arrayTrack in range(4):
            self.playerTokenTrack["plyrTokenTrack%d" % (arrayTrack+1)] = ny.array([''] * 52, dtype= object)
            self.computerTokenTrack["cmptrTokenTrack%d" % (arrayTrack+1)] = ny.array([''] * 52, dtype= object)
        self.playerWinTrack, self.computerWinTrack = globals(), globals()
        for winningTrack in range(4):
            self.playerWinTrack["plyrWinTrack%d" % (winningTrack+1)] = ny.array([''] * 6, dtype= object)
            self.computerWinTrack["cmptrWinTrack%d" % (winningTrack+1)] = ny.array([''] * 6, dtype= object)

    def playerTokensTrack(self, number,  userDice):
        if self.playerToken["PlyrToken%d" % number] == 0 and (userDice == 6 or userDice == 1):
            self.playerToken["PlyrToken%d" % number] = 1
            self.playerTokenTrack["plyrTokenTrack%d" % number][0] = self.playerToken["PlyrToken%d" % number]
        elif self.playerToken["PlyrToken%d" % number] != 0:
            if self.playerToken["PlyrToken%d" % number] + userDice < 52:
                self.playerTokenTrack["plyrTokenTrack%d" % number] = ny.roll(self.playerTokenTrack["plyrTokenTrack%d" % number], userDice)
                newIndex = ny.where(self.playerTokenTrack["plyrTokenTrack%d" % number] == self.playerToken["PlyrToken%d" % number])[0]
                self.playerTokenTrack["plyrTokenTrack%d" % number][newIndex] = self.playerToken["PlyrToken%d" % number] + userDice
                self.playerToken["PlyrToken%d" % number] = self.playerToken["PlyrToken%d" % number] + userDice
                if newIndex == 0 or newIndex == 8 or newIndex == 13 or newIndex == 21 or newIndex == 26 or newIndex == 34 or newIndex == 39 or newIndex == 47:
                    pass
                else:
                    totalCount = 0
                    for count in range(4):
                        if self.computerTokenTrack["cmptrTokenTrack%d" % (count+1)][newIndex] != '':
                            totalCount += 1
                    if totalCount == 1:
                        for count in range(4):
                            if self.computerTokenTrack["cmptrTokenTrack%d" % (count+1)][newIndex] != '':
                                self.computerTokenTrack["cmptrTokenTrack%d" % (count+1)][newIndex] = ''
                                self.computerToken["CmptrToken%d" % (count+1)] = 0
                                keys = list(self.computerScore.keys())
                                self.computerScore[keys[count]] = 0
                                print(f"The Player's {list(self.playerScore)[number - 1]} Has Blocked Computer's {list(self.computerScore)[count]} Once Again.")
            elif self.playerToken["PlyrToken%d" % number] + userDice > 51:
                if int not in [type(value) for value in list(self.playerWinTrack["plyrWinTrack%d" % number][:])]:
                    self.playerToken["PlyrToken%d" % number] = self.playerToken["PlyrToken%d" % number] + userDice
                    self.playerWinTrack["plyrWinTrack%d" % number][self.playerToken["PlyrToken%d" % number] - 52] = self.playerToken["PlyrToken%d" % number]
                    self.playerTokenTrack["plyrTokenTrack%d" % number][self.playerTokenTrack["plyrTokenTrack%d" % number] != 0] = ''
                elif self.playerToken["PlyrToken%d" % number] + userDice < 58:
                    self.playerWinTrack["plyrWinTrack%d" % number] = ny.roll(self.playerWinTrack["plyrWinTrack%d" % number], userDice)
                    newIndex = ny.where(self.playerWinTrack["plyrWinTrack%d" % number] == self.playerToken["PlyrToken%d" % number])[0]
                    self.playerWinTrack["plyrWinTrack%d" % number][newIndex] = self.playerToken["PlyrToken%d" % number] + userDice
                    self.playerToken["PlyrToken%d" % number] = self.playerToken["PlyrToken%d" % number] + userDice
                elif self.playerToken["PlyrToken%d" % number] + userDice >57:
                    print(f"You Got {userDice} Instead Of Requirement {57-self.playerToken["PlyrToken%d" % number]} To Win For {list(self.playerScore)[number-1]}. Chose Another Unblocked Token.")
                    pass
        print(f"The {list(self.playerScore)[number-1]} Status:\nOn Running Track {self.playerTokenTrack["plyrTokenTrack%d" % number]}\nOn Winning Track {self.playerWinTrack["plyrWinTrack%d" % number]}")
        # print(self.playerToken["PlyrToken%d" % number], type(self.playerToken["PlyrToken%d" % number]))

    def computerTokensTrack(self, number, computerDice):
        if self.computerToken["CmptrToken%d" % number] == 0 and (computerDice == 6 or computerDice == 1):
            self.computerToken["CmptrToken%d" % number] = 1
            self.computerTokenTrack["cmptrTokenTrack%d" % number][26] = self.computerToken["CmptrToken%d" % number]
        elif self.computerToken["CmptrToken%d" % number] != 0:
            if self.computerToken["CmptrToken%d" % number] + computerDice < 52:
                self.computerTokenTrack["cmptrTokenTrack%d" % number] = ny.roll(self.computerTokenTrack["cmptrTokenTrack%d" % number], computerDice)
                newIndex = ny.where(self.computerTokenTrack["cmptrTokenTrack%d" % number] == self.computerToken["CmptrToken%d" % number])[0]
                self.computerTokenTrack["cmptrTokenTrack%d" % number][newIndex] = self.computerToken["CmptrToken%d" % number] + computerDice
                self.computerToken["CmptrToken%d" % number] = self.computerToken["CmptrToken%d" % number] + computerDice
                if newIndex == 0 or newIndex == 8 or newIndex == 13 or newIndex == 21 or newIndex == 26 or newIndex == 34 or newIndex == 39 or newIndex == 47:
                    pass
                else:
                    totalCount = 0
                    for count in range(4):
                        if self.playerTokenTrack["plyrTokenTrack%d" % (count + 1)][newIndex] != '':
                            totalCount += 1
                    if totalCount == 1:
                        for count in range(4):
                            if self.playerTokenTrack["plyrTokenTrack%d" % (count + 1)][newIndex] != '':
                                self.playerTokenTrack["plyrTokenTrack%d" % (count + 1)][newIndex] = ''
                                self.playerToken["PlyrToken%d" % (count + 1)] = 0
                                keys = list(self.playerScore.keys())
                                self.playerScore[keys[count]] = 0
                                print(f"The Computer's {list(self.computerScore)[number-1]} Has Blocked Player's {list(self.playerScore)[count]} Once Again.")
            elif self.computerToken["CmptrToken%d" % number] + computerDice > 51:
                if int not in [type(value) for value in list(self.computerWinTrack["cmptrWinTrack%d" % (number)][:])]:
                    self.computerToken["CmptrToken%d" % number] = self.computerToken["CmptrToken%d" % number] + computerDice
                    self.computerWinTrack["cmptrWinTrack%d" % (number)][self.computerToken["CmptrToken%d" % number] - 52] = self.computerToken["CmptrToken%d" % number]                
                    self.computerTokenTrack["cmptrTokenTrack%d" % number][self.computerTokenTrack["cmptrTokenTrack%d" % number] != 0] = ''
                elif self.computerToken["CmptrToken%d" % number] + computerDice < 58:
                    self.computerWinTrack["cmptrWinTrack%d" % number] = ny.roll(self.computerWinTrack["cmptrWinTrack%d" % number], computerDice)
                    newIndex = ny.where(self.computerWinTrack["cmptrWinTrack%d" % number] == self.computerToken["CmptrToken%d" % number])[0]
                    self.computerWinTrack["cmptrWinTrack%d" % number][newIndex] = self.computerToken["CmptrToken%d" % number] + computerDice
                    self.computerToken["CmptrToken%d" % number] = self.computerToken["CmptrToken%d" % number] + computerDice
                elif self.computerToken["CmptrToken%d" % number] + computerDice >57:
                    print(f"You Got {computerDice} Instead Of Requirement {57-self.computerToken["CmptrToken%d" % number]} To Win For {list(self.computerScore)[number-1]}. Chose Another Unblocked Token.")
                    pass
        print(f"The {list(self.computerScore)[number-1]} Status:\nOn Running Track {self.computerTokenTrack["cmptrTokenTrack%d" % number]}\nOn Winning Track {self.computerWinTrack["cmptrWinTrack%d" % number]}")
        # print(self.playerToken["PlyrToken%d" % number], type(self.playerToken["PlyrToken%d" % number]))

    def statusCheck(self, board):
        Flag = False
        for iteration in board:
            if board[iteration] == 0:
                pass
            else:
                Flag = True
        return Flag

    def scoreBoard(self, playerBoard, computerBoard):
        print(f"After {Round} Round The ScoreBoard is:")
        print("Player: ", end='')
        for key, value in playerBoard.items():
            print(f"{key}: {value}     ", end="")
        print("\t\tComputer: ", end='')
        for key, value in computerBoard.items():
            print(f"{key}: {value}     ", end="")
        print(f"\nPlayerScore:{list(playerBoard.values())}  \t\t\t\t\t\t\t\t\tComputerScore:{list(computerBoard.values())}") 

    def game(self):
        while True:
            userDice = random.randint(1, 6)
            print(f"\nPlayer Dice Score is {userDice}.")
            if self.statusCheck(self.playerScore) == False and userDice != 6 and userDice != 1:
                pass
            else:
                while True:
                    try:
                        pTokens = int(input('''<---------------------Choose Among Your Tokens--------------------->
                        1 For PlyrToken1, 2 For PlyrToken2, 3 For PlyrToken3, 4 For PlyrToken4 
                        '''))
                        if pTokens == 1 or pTokens == 2 or pTokens == 3 or pTokens == 4:
                            if self.playerToken["PlyrToken%d" % pTokens] == 0 and userDice != 6 and userDice != 1:
                                print(f"The Token {list(self.playerScore)[pTokens-1]} Chose By You Is Blocked.\nTo Open This Token You Need Either 1 or 6 value. Chose Another Unblocked Token.")
                            elif self.playerScore["PlyrToken%d" % pTokens] == "W":
                                print(f"{list(self.playerScore)[pTokens-1]} Had Already Completed The Track & Won. Chose Another Unblocked Token.")
                            elif self.statusCheck(self.playerScore) == False and userDice != 6 and userDice != 1:
                                break
                            else:
                                self.playerTokensTrack(pTokens, userDice)
                                if self.playerToken["PlyrToken%d" % pTokens] == 57:
                                    self.playerScore["PlyrToken%d" % pTokens] = "W"
                                    print(f"{list(self.playerScore)[pTokens-1]} Has Completed The Track & Won.")
                                    break
                                else:
                                    self.playerScore["PlyrToken%d" % pTokens] = self.playerToken["PlyrToken%d" % pTokens]
                                    break
                        else:
                            print("Kindly! Choose The Valid Token Number Among 1, 2, 3 or 4.")
                    except Exception as error:
                        print(f"{error}. Kindly! Choose The Valid Token Number Among 1, 2, 3 or 4.")
            if userDice != 6:
                break

        if int in [type(value) for value in list(self.playerScore.values())]:
            pass
        else:
            self.scoreBoard(self.playerScore, self.computerScore)
            print("\nThe Player's All Tokens Have Finished The Track First. Congratulation! Player Has Won.")
            exit()

        self.scoreBoard(self.playerScore, self.computerScore)

        while True:
            print("\nComputer is playing.....  ", end="")
            time.sleep(1.5)
            computerDice = random.randint(1, 6)
            print(f"\nComputer Dice Score is {computerDice}.")
            if self.statusCheck(self.computerScore) == False and computerDice != 6 and computerDice != 1:
                pass
            else:
                while True:
                    try:
                        cTokens = int(input('''<---------------------Choose Among Your Tokens--------------------->
                        1 For CmptrToken1, 2 For CmptrToken2, 3 For CmptrToken3, 4 For CmptrToken4 
                        '''))
                        if cTokens == 1 or cTokens == 2 or cTokens == 3 or cTokens == 4:
                            if self.computerToken["CmptrToken%d" % cTokens] == 0 and computerDice != 6 and computerDice != 1:
                                print(f"The Token {list(self.computerScore)[cTokens-1]} Chose By You Is Blocked.\nTo Open This Token You Need Either 1 or 6 value. Chose Another Unblocked Token.") 
                            elif self.computerScore["CmptrToken%d" % cTokens] == "W":
                                print(f"{list(self.computerScore)[cTokens-1]} Had Already Completed The Track & Won. Chose Another Unblocked Token.")
                            elif self.statusCheck(self.computerScore) == False and computerDice != 6 and computerDice != 1:
                                break
                            else:
                                self.computerTokensTrack(cTokens, computerDice)
                                if self.computerToken["CmptrToken%d" % cTokens] == 57:
                                    self.computerScore["CmptrToken%d" % cTokens] = "W"
                                    print(f"{list(self.computerScore)[cTokens-1]} Has Completed The Track & Won.")
                                    break
                                else:
                                    self.computerScore["CmptrToken%d" % cTokens] = self.computerToken["CmptrToken%d" % cTokens]
                                    break
                        else:
                            print("Kindly! Choose The Valid Token Number Among 1, 2, 3 or 4.")
                    except Exception as error:
                        print(f"{error}. Kindly! Choose The Valid Token Number Among 1, 2, 3 or 4.")
            if computerDice != 6:
                break

        if int in [type(value) for value in list(self.computerScore.values())]:
            pass
        else:
            self.scoreBoard(self.playerScore, self.computerScore)
            print("\nThe Computer's All Tokens Have Finished The Track First. Hard Luck!. Try Again.")
            exit()

        self.scoreBoard(self.playerScore, self.computerScore)

if __name__ == "__main__":
    while True:
        try:
            userInput = int(input('''
                            <---------------------Ludo--------------------->
                                1 Yes! To Play Ludo With Game.
                                2 No! For Exit From The Game.
                                '''))
            if userInput == 1:
                Round = 0
                ludoBoard = Ludo()
                print("Both Players You and Computer Have To Assign 4 Tokens Having Score 0. The Player Whose All Tokens Win First Will Be Winner.\nThe Token Have To Score 57 To Win.")
                ludoBoard.scoreBoard(ludoBoard.playerScore, ludoBoard.computerScore)
                while True:
                    userChoice = input('''\n\nPress 'P' To Play Dice and 'S' To Stop The Game.''')
                    if userChoice.lower() == 'p':
                        Round += 1
                        ludoBoard.game()
                    elif userChoice.lower() == 's':
                        break
                    else:
                        print("Invalid Choice! Select Valid Value. Press 'P' To Play Again & 'S' For Stop The Game.")
                        continue
            elif userInput == 2:
                break
            else:
                print("Invalid Choice! Please, Select Valid Value.")
                continue
        except Exception as error:
            print(f"{error}. Kindly! Choose The Input.")