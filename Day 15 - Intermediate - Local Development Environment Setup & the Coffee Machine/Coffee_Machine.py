from data import data
from art import logo

print(logo)

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
