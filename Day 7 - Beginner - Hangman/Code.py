
# 1
import random
import string


word_list = ["hello","how","are","you"]
rand_word = random.choice(word_list)

user_word = input("Guess any word: ").lower()

for letter in rand_word:
    if letter == user_word:
        print("Right")
    else:
        print("Wrong")