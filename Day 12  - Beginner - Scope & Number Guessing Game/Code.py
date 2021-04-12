
# 1
# enemy = 1


# def inc():
#     enemy = 2
#     print(f"inside function {enemy} ")


# inc()
# print(f"outside fun {enemy} ")

# # 2
# game_level = 3
# def cre_emy():
#     enemy = ['a', 'b', 'c']
#     if game_level < 5:
#         new_emy = enemy[0]


# modify global scope
a = 1
def update():
    global a
    a += 1
    print(f"inside {a}")

update()
print(f"outside {a}")