"""#
# with open("weather.csv") as data_file:
#     file_cont = data_file.readlines()
#     print(file_cont)"""

import csv
temperature = []
with open("weather.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != ' temp':
            temperature.append(int(row[1]))
    print(temperature)
