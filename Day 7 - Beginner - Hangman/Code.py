
# 1
import random


word_list = ["abcd","efgh","ijkl"]

rand_word = random.choice(word_list)

print(rand_word)

user_word = input("Guess any word: ")
if(user_word in rand_word):
    print("YES")
else:
    print("NO")