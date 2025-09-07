import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number from 10 to 20,you have to guess the no.")
while playing:
    guess=input("guess your no.")
    if number==guess:
        print("you won the game")
        break
    else:
        print("you lost the game")