import random
import string
def passwordConditions():
    #get user input
    while done != "done":
        done = input('Create password (or done)? ')
        letters = input('How many letters? ')
        numbers = input('How many numbers? ')
        characters = input('How many special characters? ')
        passwordGen(letters, numbers, characters)

def passwordGen(let, num, char):
    #get all randoms the add together
    sign  = ''.join(random.choice(string.ascii_letters) for i in range(int(let)))
    digit = ''.join(str(random.randint(1, 10)) for i in range(int(num)))
    symbol = ''.join(random.choice(["!","@","#","$","%","^","&","*","(",")","-","+"]) for i in range(int(char)))

    #string -> list -> newList -> string -> password
    passwordForm = sign + str(digit) + symbol
    passwordList = list(passwordForm)
    new_list = random.shuffle(passwordList)
    finalPassword = ''.join(passwordList)
    print(finalPassword)

passwordConditions()