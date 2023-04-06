from random import *

you=input("Your turn to choose between Gun or Snake or Water: ")

randno = randint(1,3)
if randno == 1:
    comp = 'gun'
elif randno == 2:
    comp = 'snake'
elif randno == 3:
    comp = 'water'

print(f"The Computer randomly choosed {comp} and your choice is {you}")

def game(comp,you):
    if comp == you:
        return None
    elif comp == 'gun' and you == 'snake':
        return False
    elif comp == 'gun' and you == 'water':
        return True
    elif comp == 'snake' and you == 'water':
        return False
    elif comp == 'snake' and you == 'gun':
        return True
    elif comp == 'water' and you == 'gun':
        return False
    elif comp == 'water' and you == 'snake':
        return True

result = game(comp,you)
if result == None:
    print("Match between you and computer is tied")
elif result:
    print("You Won")
else:
    print("Computer Won")

