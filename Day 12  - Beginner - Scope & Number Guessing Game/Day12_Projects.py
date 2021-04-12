from art import logo
import random

def game_ext(chance,guess_num):
    print(f"You have {chance} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if(user_guess == guess_num):
        print("You Passed !!!")
    elif(user_guess < guess_num):
        print("Too Low.")
    else:
        print("Too High.")
    print("Guess again.")



print("Welcome to the Number Guessing Game!")
print(logo)
print("I'm thinking of a number between 1 and 100.")
guess_num = random.randint(0,100)
print(guess_num)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    chance = 10
    while(chance > 0):
        game_ext(chance,guess_num)
        chance -= 1
else:
    chance = 5
    while(chance > 0):
        game_ext(chance,guess_num)
        chance -= 1
