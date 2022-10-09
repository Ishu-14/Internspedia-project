# NUMBER GUSSING GAME
import math
import random

print("-------------------------------------------")
print("********LETS PLAY THE GAME OF GUESSING********")
print("-------------------------------------------")

lower_range=int(input("Enter the lower range : "))
upper_range=int(input("Enter the upper range : "))

num=random.randint(lower_range,upper_range)
print("\n\tYou've only ",round(math.log(upper_range - lower_range + 1, 2))," chances to guess the integer!\n")

count = 0
 

while count < math.log(upper_range - lower_range + 1, 2):
    
    count += 1
    guess_num = int(input("Please guess a number :- "))
 
    
    if num == guess_num:
        print("Congratulations you did it in  ",count, " Go/Go's")
        break
    elif num > guess_num:
        print("You Guessed a very Small number!")
    elif num < guess_num:
        print("You Guessed a very High number!")

if count >= math.log(upper_range - lower_range + 1, 2):
    print("-------------------------------------------")
    print("\nThe number needed to guess was : %d" % num)
    print("\tBetter Luck Next time!!")
