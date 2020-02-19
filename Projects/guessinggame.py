import random
def guessinggame():
    rand = random.randint(1,10)
    print(rand) 
    num = int(input("enter a number between 1-10 : "))
    if num == rand:
        print( "You won the game")
    else:
        a = input(("enter Y/y to try again or enter N/n to exit :"))
        #print(a)
        if a == "Y" or a == "y":
            guessinggame()
        elif a=="N" or a == "n":
            return "Thank you"

guessinggame()