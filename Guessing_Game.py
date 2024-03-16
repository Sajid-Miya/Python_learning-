import random

number = random.randint(1,10)

user_guess = int(input("Enter number from 1 to 10:"))

attempt = 0


if user_guess == number:
    print(f"Congratulations! You guessed the {number} in  {attempt+1} attempts.")
elif user_guess < number:
    print("The number is higher")
    attempt += 1
    user_guess=int(input("Try again: "))
    if user_guess == number:
        print(f"Congratulations! You guessed the {user_guess} in  {attempt+1} attempts.")
    else:
        print(f"Sorry, the number was {number} You took {attempt+1} attempts  ")
else:
    print("Try a lower number: ") 
    attempt += 1
    user_guess=int(input("Try again: "))
    if user_guess == number:
        print(f"Congratulations! You guessed the {user_guess} in  {attempt+1} attempts.")
    else:
        print(f"Sorry, the number was {number} You took {attempt+1} attempts  ")


