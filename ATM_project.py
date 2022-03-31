names = ["Xan", "Namisa", "Bryan", "Auzinea"]
#function to deposit money in account
def depositAction(key, value, dictionary):
    #add input to value
    quanity = input("How much? " )
    value += int(quanity)
    print(str(value) + " left in account")
    dictionary[key] = value

#function to withdraw money from account
def withdrawAction(key, value, dictionary):
    #subtract input from value
    quanity = input("How much? " )
    total = value - int(quanity)
    #conditional statement to prevent any number below 0
    if total < 0:
        print("Insufficient funds\n" + str(value) + " left in account")
    else:
        value = total
        print(str(value) + " left in account")
    dictionary[key] = value