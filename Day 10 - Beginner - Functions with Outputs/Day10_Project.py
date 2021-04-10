from art import logo
print(logo)


def calc(first,opr,second):
    if(opr == '+'):
        return first + second
    elif(opr == '-'):
        return first - second
    elif(opr == '*'):
        return first * second
    elif(opr == '/'):
        return first / second


test = 'y'
while(test):
    fir_num = eval(input("Enter the first number: "))
    print("+\n-\n*\n/")
    opr = input("Select Operator: ")
    sec_num = eval(input("Enter the Second number: "))

    print(f"Required Output: {fir_num} {opr} {sec_num} = " + str(calc(fir_num,opr,sec_num)))

    rep = input("Want to repeat? (y or n)")
    if rep == 'y': test = 'y'
    else: test = 'n'

