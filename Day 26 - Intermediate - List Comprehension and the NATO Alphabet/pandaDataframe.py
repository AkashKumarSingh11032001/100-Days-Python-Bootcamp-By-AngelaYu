student_dict = {
    "student": ["Akash","James","Lily"],
    "score": [56,76,98]
}

for (key,value) in student_dict.items():
    print(key)
    print(value)

#pandas
import pandas
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

#loop throw dataframe
for (key,value) in student_dataframe.items():
    print(value)
