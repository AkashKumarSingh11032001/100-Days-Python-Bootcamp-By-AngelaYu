
with open("Inputs/name.txt") as inv_name:
    names = inv_name.readline()

with open("Inputs/Letter.txt") as letter:
    letter_cont = letter.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_cont.replace("[name]",strip_name)
        with open()


