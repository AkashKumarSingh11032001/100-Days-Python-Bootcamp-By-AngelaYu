# #1 Day8
# def greet(str):
#     print(f"Hello {str}\n"+ f"Bye {str}\n"+ f"See you {str}")

# greet("Akash")

# # multiple input

# def mul_input(str1,str2):
#     print(f"{str1} loves {str2}")

# def mul_input(str1,str2):
#     print(f"{str1} loves {str2}")

# mul_input("Akash","Archana")
# mul_input(str1="Archana",str2="Akash")

# # ex-8.1

# def area(height,width,cov):
#     return round((height*width)/cov)

# print(area(2,4,5))

# ex-8.2 
def prime_checker(num):
    is_prime = True
    for i in range(2,num):
        if(num%i == 0):
            is_prime = False
            # print("Not aprime Number.")
    if is_prime:
        print("prime Number.")
    else:
        print("Not prime Number.")


prime_checker(3)

