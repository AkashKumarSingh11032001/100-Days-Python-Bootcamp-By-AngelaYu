
with open("Inputs/name.txt") as inv_name:
    names = inv_name.readlines()

with open("Inputs/Letter.txt") as letter:
    letter_cont = letter.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_cont.replace("[name]",strip_name)
        with open(f"Output/letter_for_{strip_name}.txt",mode="w") as updated_letter:
            updated_letter.write(new_letter)


