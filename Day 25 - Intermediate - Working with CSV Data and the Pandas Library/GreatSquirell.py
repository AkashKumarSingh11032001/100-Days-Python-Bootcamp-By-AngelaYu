import pandas

data = pandas.read_csv("squirel_data.csv")
gray_squ = data[data["Primary Fur Color"] == "Gray"]


print(gray_squ)