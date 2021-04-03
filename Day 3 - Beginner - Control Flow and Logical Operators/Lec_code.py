# 1
# if-else
# height = eval(input("Enter your height: "))

# if(height > 120):
#     print("Sell Ticket")
# else:
#     print("Not Eligible")

# 2
# ex-3.1
# num = eval(input("Enter Number. : "))
# if(num % 2 == 0):
#     print("Even Num.")
# else:
#     print("Odd Num.")

# 3
# nested If-else
# height = eval(input("Enter your height: "))
# age = eval(input("Enter your age: "))
# if(height > 120):
#     if(age < 18):
#         print("$7 ")
#     else:
#         print("$12")
# else:
#     print("Not Eligible")

# 4
# ex-3.2
# BMI 2.0
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# #bmi = round(weight / height**2)
# bmi = 25

# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight.")

# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight.")

# elif bmi < 30:
#     print(f"Your bmi is {bmi}, you are overweight.")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, you are obese.")
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese.")

# ex-3.3
# year = eval(input("Enter Year: "))
# if(year % 4 == 0 or year % 100 == 0 or year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap year")

# 5
# Multiple If statement

# 6
# ex-3.3
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# cost = 0
# if(size == 'S'):
#     if(add_pepperoni == 'Y'):
#         cost += 17
#     else:
#         cost += 15

# elif(size == 'M'):
#     if(add_pepperoni == 'Y'):
#         cost += 23
#     else:
#         cost += 20
# elif(size == 'L'):
#     if(add_pepperoni == 'Y'):
#         cost += 28
#     else:
#         cost += 25

# if(extra_cheese == 'Y'):
#     cost += 1

# print(f"Total price you have to pay: ${cost}")

# 10 
# ex-3.5
# Love Calulator
my_name = input("Enter Your name: ")
crush_name = input("Enter Crush name: ")
name = (my_name + crush_name).lower()
print(my_name +" weds "+crush_name)
T,R,U,E = name.count('t'),name.count('r'),name.count('u'),name.count('e')
L,O,V,E = name.count('l'),name.count('o'),name.count('v'),name.count('e')

print(f"Chance Of Marriage: {T+R+U+E}{L+O+V+E}%")