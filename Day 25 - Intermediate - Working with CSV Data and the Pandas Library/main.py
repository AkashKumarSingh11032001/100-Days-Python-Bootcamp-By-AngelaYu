data = []
with open("weather.csv") as data_file:
    file_cont = data_file.readline()

print(file_cont)