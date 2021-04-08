alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def common_fun(task,tex,shif):
    ciper_text = ""
    if task == "ec":
        for i in tex:
            ciper_text += chr(ord(i)+shif)
    else:
        for i in tex:
            ciper_text += chr(ord(i)-shif)

    return ciper_text


def encrypt(tex, shif):
    # ency_text = ""
    # for i in tex:
    #     ency_text += chr(ord(i)+shif)
    # return ency_text
    return common_fun("ec",tex,shif)


def decrypt(tex, shif):
    # decry_text = ""
    # for i in ency_tex:
    #     decry_text += chr(ord(i)-shif)
    # return decry_text
    return common_fun("dc",tex,shif)


if direction == "encode":
    print("Your Encrypted Message: "+encrypt(text,shift))
else:
    print("Your Decrypted Message: "+decrypt(text,shift))
