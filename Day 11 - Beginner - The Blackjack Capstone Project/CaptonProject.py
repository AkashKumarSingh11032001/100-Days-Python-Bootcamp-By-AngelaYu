from art import logo
import random


def play():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card = random.choices(cards,k=2)
    print(user_card)
    comp_card = []


want = input("Do you want to PLAY 'y' or 'n': ")

if (want == 'y'):
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play()