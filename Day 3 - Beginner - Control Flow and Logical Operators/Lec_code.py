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
year = eval(input("Enter Year: "))
if(year % 4 == 0 or year % 100 == 0 or year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap year")