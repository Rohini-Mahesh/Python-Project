import random
rand1 = random.randint(1,100)
win = 0
score =0
while win==0:
    guess = input("Enter a number between 1 and 100 ")
    score +=1
    if rand1==int(guess):
        print("You won!")
        print("Your score is: ",score)
        win == 1
        break
    else:
     if rand1>int(guess):
        print("Guess was low, Please enter a higher number")
     else:
        print("guess was high, please enter a lower number")