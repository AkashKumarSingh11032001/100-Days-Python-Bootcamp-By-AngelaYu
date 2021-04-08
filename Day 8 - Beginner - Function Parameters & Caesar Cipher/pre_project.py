from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def common_fun(task,tex,shif):
    ciper_text = ""
        
    if task == "encode":
        for i in tex:
            if i in alphabet:
                ciper_text += alphabet[alphabet.index(i) + shif]
            else:
                ciper_text += i
    elif task == "decode":
        for i in tex:
            if i in alphabet:
                ciper_text += alphabet[alphabet.index(i)-shif]
            else:
                ciper_text += i
    return ciper_text



should_continue = True
while(should_continue):

    # basic input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # checking shift is greater than 26
    if(shift >= 26):shift = shift%26

    # calling accordily
    if direction == "encode":
        print("Your Encrypted Message: "+ common_fun(direction,text,shift))
    else:
        print("Your Decrypted Message: "+ common_fun(direction,text,shift))

    # asking user to repeat
    rep = input("What to conntinue again? (Yes or No) ")
    if rep =="Yes":
        should_continue = True
    else:
        should_continue = False




# def encrypt(tex, shif):
#     # ency_text = ""
#     # for i in tex:
#     #     ency_text += chr(ord(i)+shif)
#     # return ency_text
#     return common_fun("ec",tex,shif)


# def decrypt(tex, shif):
#     # decry_text = ""
#     # for i in ency_tex:
#     #     decry_text += chr(ord(i)-shif)
#     # return decry_text
#     return common_fun("dc",tex,shif)
