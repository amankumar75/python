import random 
number = random.randint(1,10)

guess = int(input("Guess the number between 1 to 10"))


if guess == number :
    print("YOU WON !!!")
else :
    print("YOU LOSE!!!!! ")
print("Computer choose",number)    
print("You choose",guess)
