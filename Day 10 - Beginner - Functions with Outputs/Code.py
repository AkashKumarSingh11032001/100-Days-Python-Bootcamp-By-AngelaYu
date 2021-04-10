# #1 
# def formate_name():
#     f_name = input("Enter 1st name: ").title()
#     l_name = input("Enter  2nd name:").title()

#     return f"Hello {f_name} {l_name}"


# print(formate_name())

##3
# def formate_name(): 
#     f_name = input("Enter 1st name: ").title()
#     l_name = input("Enter  2nd name:").title()

#     return f"Hello {f_name} {l_name}"


# print(formate_name())

# ex-4.1
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")

def days_in_month():
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

