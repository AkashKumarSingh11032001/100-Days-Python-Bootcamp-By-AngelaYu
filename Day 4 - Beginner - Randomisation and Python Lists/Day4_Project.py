# DAY 4 FINAL PROJECTS

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = eval(
    input("Enter you choice 0- Rock || 1- Paper || 2- Scisore: "))
comp_choice = random.randint(0, 2)
img = [rock, paper, scissor]

print("User Picked : " + img[user_choice])
print(f"Computer Picked {comp_choice}: " + img[comp_choice])

print("R E S U L T => ")

if(user_choice == comp_choice):
    print("Its Draw !!!")
elif(user_choice == 0):
    if(comp_choice == 2):
        print("YOU WIN !!!")
    else:
        print("Computer Win !!!")
elif(user_choice == 1):
    if(comp_choice == 0):
        print("YOU WIN !!!")
    else:
        print("Computer Win !!!")
elif(user_choice == 2):
    if(comp_choice == 1):
        print("YOU WIN !!!")
    else:
        print("Computer Win !!!")
