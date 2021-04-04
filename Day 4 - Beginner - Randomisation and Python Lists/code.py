# 1
# Random modulee
import random

# // int num
# num = random.randint(1,10)
# print(num)

# float num
# num_f = random.random()
# print(num_f)

# ex-4.1
# num = random.randint(0,1)
# if(num == 1):
#     print("Heads")
# else:
#     print("Tails")


# LIST

# name = ['A','B','C','D','E']
# print(name[0])
# name.append('F')
# name.extend(['a','b','c'])
# print(name)

# ex-4.2

# name = input("Enter your friend name separted by comma: ")
# ind_name = name.split(",")
# # rand = random.randint(0,len(ind_name)-1)
# # or
# rand = random.choice(ind_name)
# print("bill will be payed by: "+ rand)

# nested list

# ex-4.3
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
# row1 = ["1","2","3"]
# row2 = ["4","5","6"]
# row3 = ["7","8","9"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = int(position[0]) 
col = int(position[1])

map[row][col] = 'X'

print(f"{row1}\n{row2}\n{row3}")



