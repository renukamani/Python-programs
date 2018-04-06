import random
while True :
    no_1 = random.randint(1,10)
    no_2 = input("Guess a number")
    try:
        no_2 = int(no_2)
    except:
        print("bye")
        break
    if (no_1 > no_2) :
        print("number guessed is too less")
    elif (no_1 < no_2) :
        print("number guessed is too big")
    else :
        print("correct")
