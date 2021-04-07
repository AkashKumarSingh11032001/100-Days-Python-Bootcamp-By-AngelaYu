
# 1
import random
import string


word_list = ["hello", "how", "are", "you"]
chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

display = []
for i in range(length):
    display.append("_")
print(display)

while length > 0:
    user_word = input("Guess any word: ").lower()

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == user_word:
            display[pos] = letter

    print(display)

    length -= 1

print("you Win!!!")