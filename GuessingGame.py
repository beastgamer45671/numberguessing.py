import random
print("Number Guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9):")

while chances < 5:
     guess = int(input("Enter your guess:- "))
     
     if guess == number:
     print("Congratulations, You Won!")
     break
     
 elif guess < number:
 print("Your guess is too low, guess a number higher than" guess)
 
 else:
      print("Your guess is too high, guess a number higher than" guess)
      
chance += 1

if not chances < 5:
      print("Sorry, You Lose! The number is" number)
      
 
 
 
