from data import data
from art import logo

print(logo)


def money_cal(sum,var):
    if(sum > data[var][ "cost"] ):
        res = sum - data[var][ "cost"]
        print( f" Here is ${round(res,2)} changes")
        print(f"HEre is your {var} enjoy")
        return 1
    elif(sum ==  data[var][ "cost"] ):
        print(f"Here is your {var} enjoy")
        return 2
    else:
        print("Not having sufficient money!. Money refunded")
        return 3



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

flag = True
while flag:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if(coffee == "report"):
        for key in report["ingredients"]:
            print(str(key),str(report["ingredients"][key])+ "ml" )
        print("cost " + str(report["cost"]) + "$")


    if(coffee == "espresso"):
        user_money = take_user("espresso")
        user_ex_money = money_cal(user_money,"espresso")
        if user_ex_money == 1 or user_ex_money == 2:
            report_update("espresso")
    elif(coffee == "latte"):
        user_money = take_user("latte")
        user_ex_money = money_cal(user_money,"latte")
        if user_ex_money == 1 or user_ex_money == 2:
            report_update("latte")
    elif(coffee == "cappuccino"):
        user_money = take_user("cappuccino")
        user_ex_money = money_cal(user_money,"cappuccino")
        if user_ex_money == 1 or user_ex_money == 2:
            report_update("cappuccino")
    if(coffee != "report"):
        for i in report["ingredients"]:
            # print(report["ingredients"][i])
            # print(data[coffee]["ingredients"][i])
            if(report["ingredients"][i] < data[coffee]["ingredients"][i]):
                print("We are out of Stocks")
                flag = False
            else:
                continue