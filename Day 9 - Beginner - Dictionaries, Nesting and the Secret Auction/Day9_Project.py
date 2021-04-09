from logo import logo
from replit import clear


def fina_res(user):
    for i in user:
        x = max(user[i])
    return x


print(logo)
print("Welcome to the SECRET AUTION program.")

user = {}
more_user = True
while(more_user):
    user_name = input("What's your name?: ")
    user_bid = input("What's your bid?: ")
    user[user_name] = user_bid
    ask = input("Any more User?(Yes or No): ")
    if(ask == "No"):
        clear()
        print(f"The winner is {str(fina_res(user))} user that is", f"user {user}")

        more_user = False

    else:
        clear()
