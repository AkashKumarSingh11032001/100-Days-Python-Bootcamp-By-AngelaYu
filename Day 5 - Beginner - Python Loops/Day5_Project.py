import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['!', '#', '$', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Genrator!!!")

passLen = eval(input("Length Of password: "))
symLen = eval(input("Number of Symbol: "))
numLen = eval(input("NUmber in password: "))

password = ""
for i in range(1,passLen+1):
    password += random.choice(letters)
for j in range(1,symLen+1):
    password += random.choice(symbols)
for k in range(1,numLen+1):
    password += random.choice(numbers)

print(password)
