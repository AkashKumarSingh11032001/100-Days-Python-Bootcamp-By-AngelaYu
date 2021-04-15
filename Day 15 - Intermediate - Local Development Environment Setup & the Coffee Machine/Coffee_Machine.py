from data import data
from art import logo

print(logo)

def take_user(var):
    sum = 0
    print("Please Insert Coins.")
    quarter = int(input("How many Quarter? :"))
    dimes = int(input("How many Dimes? :"))
    nickles = int(input("How many Nickles? :"))
    pennies = int(input("How many Pennies? :"))
    sum += quarter*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if(sum > data[var][ "cost"] ):
        res = sum - data[var][ "cost"]
        print( f" Here is ${round(res,2)}")
    elif(sum ==  data[var][ "cost"] ):
        print(f"HEre is your {var} enjoy")
    else:
        





report = {
    "ingredients":{
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
    },
    "cost": 0
}

coffee = input("What would you like? (espresso/latte/cappuccino): ")

if(coffee == "report"):
    for key in report["ingredients"]:
        print(str(key),str(report["ingredients"][key])+ "ml" + str(report["cost"]) + "$")
elif(coffee == "espresso"):
    take_user("espresso")
