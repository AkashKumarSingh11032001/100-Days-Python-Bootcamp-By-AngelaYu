from art import logo
import random

def game_ext(user_card,comp_card,card):
    user_card += random.choice(card)
    print(user_card)



def play():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    user_card = random.choices(cards,k=2)
    total = sum(user_card)
    print("Your cards: "+ str(user_card)+", current score: "+str(total))
    
    comp_card = random.choices(cards,k=2)
    print("Computer's first card: "+ str(comp_card[0]))

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if(another_card == 'y'):
        game_ext(user_card,comp_card,cards)
    else:
        exit()


want = input("Do you want to PLAY 'y' or 'n': ")

if (want == 'y'):
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play()