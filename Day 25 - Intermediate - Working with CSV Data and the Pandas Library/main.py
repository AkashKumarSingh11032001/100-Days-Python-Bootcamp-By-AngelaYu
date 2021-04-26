data = []
with open("weather.csv") as data_file:
    file_cont = data_file.readlines()
    data.append(file_cont)

print(data)