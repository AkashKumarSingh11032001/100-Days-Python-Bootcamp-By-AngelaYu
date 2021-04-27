with open("q3_file1.txt") as file1:
    file1_data = file1.readlines()

with open("q3_file2.txt") as file2:
    file2_data = file2.readlines()

print([i for i in file1_data for j in file2_data if i == j ])
