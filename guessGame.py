import random

lower=int(input("Enter lower limit: "))
higher=int(input("Enter higher limit: "))

comGuess = random.randint(lower,higher)
while True:
    userGuess = int(input("Guess a number b/w " +str(lower)+"-" +str(higher)+" : "))
    if userGuess > comGuess:
        print("Guess lower!")
        higher = userGuess
    elif userGuess < comGuess:
        print("Guess higher!")
        lower = userGuess
    else:
        print("Congrats!, you won.")
        break;
