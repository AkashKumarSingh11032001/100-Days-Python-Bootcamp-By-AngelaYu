from data import data
from art import logo

print(logo)


def money_cal(sum,var):
    if(sum > data[var][ "cost"] ):
        res = sum - data[var][ "cost"]
        print( f" Here is ${round(res,2)} changes")
        print(f"HEre is your {var} enjoy")
    elif(sum ==  data[var][ "cost"] ):
        print(f"Here is your {var} enjoy")
    else:
        print("Not having sufficient money!. Money refunded")



def take_user(var):
    sum = 0
    print("Please Insert Coins.")
    quarter = int(input("How many Quarter? :"))
    dimes = int(input("How many Dimes? :"))
    nickles = int(input("How many Nickles? :"))
    pennies = int(input("How many Pennies? :"))
    sum += quarter*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    
    return sum


def report_update(var):
    for key in report["ingredients"]:
        # print(report["ingredients"][key])
        # print(data[var]["ingredients"][key])
        report["ingredients"][key] -=  data[var]["ingredients"][key]
        report["cost"] += data[var]["cost"] 
    return report
    

report = {
    "ingredients":{
    "water": 300,
    "milk": 200,
    "coffee": 100
    },
    "cost": 0
}



coffee = input("What would you like? (espresso/latte/cappuccino): ")

if(coffee == "report"):
    for key in report["ingredients"]:
        print(str(key),str(report["ingredients"][key])+ "ml" + str(report["cost"]) + "$")
elif(coffee == "espresso"):
    user_money = take_user("espresso")
    user_ex_money = money_cal(user_money,"espresso")
    print(report_update("espresso"))