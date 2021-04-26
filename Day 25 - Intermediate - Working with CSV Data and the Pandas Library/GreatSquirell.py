import pandas

data = pandas.read_csv("squirel_data.csv")
gray_squ = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squ = data[data["Primary Fur Color"] == "Cinnamon"]
black_squ = data[data["Primary Fur Color"] == "Black"]



print(len(gray_squ))
print(len(cinnamon_squ))
print(len(black_squ))

data_dic = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [len(gray_squ),len(cinnamon_squ),len(black_squ)]
}
df = pandas.DataFrame(data_dic)
df.to_csv("anyas_1_file.csv")