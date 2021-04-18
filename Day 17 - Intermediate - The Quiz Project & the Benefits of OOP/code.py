class User:
    #construtor
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0


user_1 = User("001","Akash")
user_2 = User("002","Angella")
# user_1.id = "001"
# user_1.username = "Akash"

print(user_1.username)
print(user_2.username)
print(user_1.follower)

