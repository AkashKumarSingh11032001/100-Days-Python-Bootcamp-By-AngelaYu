
#1
enemy = 1
def inc():
    enemy = 2
    print(f"inside function {enemy} ")

inc()
print(f"outside fun {enemy} ")