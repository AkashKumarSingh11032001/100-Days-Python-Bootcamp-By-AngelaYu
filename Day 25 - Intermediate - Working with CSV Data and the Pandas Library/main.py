"""#
# with open("weather.csv") as data_file:
#     file_cont = data_file.readlines()
#     print(file_cont)"""

# import csv
# temperature = []
# with open("weather.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != ' temp':
#             temperature.append(int(row[1]))
#     print(temperature)
# //ALTERNATIVE
import pandas
data = pandas.read_csv("weather.csv")
#print(data)
print(type(data))
print(data["temp"])

data_dic = data.to_dict()
print(data_dic)

tem_list = data["temp"].to_list()
# avg_temp = sum(tem_list)/len(tem_list)
# print(avg_temp)
print(data["temp"].mean())
print(data["temp"].max())

print(tem_list)

# // GTE DATA IN COLUMN
print(data["condition"])
print(data.condition)

# // GET DATA IN ROW WISE
print(data[data.day == "Monday"])

# Q:
print(data[data.temp == data.temp.max()])