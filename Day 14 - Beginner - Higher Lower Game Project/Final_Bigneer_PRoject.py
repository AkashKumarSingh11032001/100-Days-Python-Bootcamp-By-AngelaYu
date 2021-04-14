from random import random
from art import logo,vs
from game_data import data
import random

print(logo)


def check_ans(A,B):
    print(f"A: {type(A['follower_count'])} B: {B['follower_count']}")
    if(A['follower_count'] > B['follower_count']):
        return 'yes'
    else:
        return B 


def ram():
    return random.choice(data)


def game_play(A,B):
    your_ans = input("Enter A or B: ")
    

    if(your_ans == check_ans(A,B)):
        print("Corret choice")
    else:
        print(f"A: {A['follower_count']} B: {B['follower_count']}")
        print("Wrong")
        
    
    



player1 = ram()
print(f"Compare A: {player1['name']}, {player1['description']}, {player1['country']}")
print(vs)
player2 = ram()
print(f"Against B: {player2['name']}, {player2['description']}, {player2['country']}")

count = 0
if(game_play(player1,player2) == "Corret choice"):
    count += 1
else:
    print(f"Your score: {count}")
    exit()

# x = True
# while(x == True):
#     if(game_play(player1,player2)):
#         count += 1
# else:
#     x = False
    
# 




# a = random.choice(data)
# b = random.randint(0,len(data))
# print(f" User 1: data first elemnt {data[a]} and first elemt name {data[a]['name']} and follower {data[a]['follower_count']} and description {data[a]['description']} and country {data[a]['country']} \n")
# print(f" User 2: data first elemnt {data[b]} and first elemt name {data[b]['name']} and follower {data[b]['follower_count']} and description {data[b]['description']} and country {data[b]['country']} ")
