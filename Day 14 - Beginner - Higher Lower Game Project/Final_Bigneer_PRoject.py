from random import random
from art import logo,vs
from game_data import data
import random

print(logo)


def check_ans(your_ans,A,B):
    if(A['follower_count'] > B['follower_count']):
        return your_ans == 'A'
    else:
        return your_ans == 'B'


def ram():
    return random.choice(data)


def game_play(A,B):
    your_ans = input("Enter A or B: ")
    

    if(check_ans(your_ans,A,B)):
        return "Corret choice"
    else:
        return "Wrong"
        
    
    

game_continue = True
score = 0
while game_continue:
    player1 = ram()
    print(f"Compare A: {player1['name']}, {player1['description']}, {player1['country']}")
    print(vs)
    player2 = ram()
    print(f"Against B: {player2['name']}, {player2['description']}, {player2['country']}")
    
    if(game_play(player1,player2) == "Corret choice"):
        score += 1
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
