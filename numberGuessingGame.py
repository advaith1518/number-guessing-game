import random
print('number Guessing game')
number = random.randint(1,9)
chances = 0
print('guess a number between 1 to 9')
while chances<5:
    guess = int(input("enter your guess"))
    if guess == number:
        print('congradulation you won')
        break
    elif guess<number:
        print("your number wass too low guess a number higher than that ",guess)
    else:
        print("your number was too high guess a lower number",guess)
    chances+=1
if not chances<5:
    print("you loose bye!!!")            
