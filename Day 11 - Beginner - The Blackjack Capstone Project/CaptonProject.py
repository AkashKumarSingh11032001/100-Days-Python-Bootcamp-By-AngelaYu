from art import logo
import random


def final_res(user_card, comp_card, card):
    if(sum(user_card) >= 21):
        print("    Your Final hand: " + str(user_card) +
              ", final scores: " + str(sum(user_card)))
        print("    Computer Final hands: " + str(comp_card) +
              ", final scores: " + str(sum(comp_card)))

    if(sum(user_card) < 21 and sum(user_card) > sum(comp_card)):
        print("You Win !!!")
    elif(sum(user_card) >= 21):
        print("You Loss !!!")


def another(user_card, comp_card, card):
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if(another_card == 'y'):
        if(sum(user_card) < 21):
            game_ext(user_card, comp_card, card)
    else:
        exit()


def game_ext(user_card, comp_card, card):

    user_card.append(random.choice(card))
    print("    Your cards: " + str(user_card) +
          ", current score: "+str(sum(user_card)))
    print("    Computer's first card: " + str(comp_card[0]))
    if(sum(user_card) < 21):
        another(user_card, comp_card, card)
    else:
        final_res(user_card, comp_card, card)


def play():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_card = random.choices(cards, k=2)
    total = sum(user_card)
    print("Your cards: " + str(user_card)+", current score: "+str(total))

    comp_card = random.choices(cards, k=2)
    print("Computer's first card: " + str(comp_card[0]))

    another(user_card, comp_card, cards)


want = input("Do you want to PLAY 'y' or 'n': ")

if (want == 'y'):
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play()
