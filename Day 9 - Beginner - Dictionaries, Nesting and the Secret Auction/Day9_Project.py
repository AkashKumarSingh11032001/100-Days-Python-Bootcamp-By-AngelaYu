from logo import logo
import replit import clear

print(logo)
print("Welcome to the SECRET AUTION program.")

user = {}
user_name = eval(input("What's your name?: "))
user_bid = eval(input("What's your bid?: "))
user[user_name] = user_bid

print(user)