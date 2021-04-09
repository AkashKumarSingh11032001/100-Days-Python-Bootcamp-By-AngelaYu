# #1 Day9
# dict = {1:'A',2:'B',3:'C',4:'D',5:'E'}
# print(dict[1])
# print(dict[2])
# #  UPDATING DATA
# # Before
# print(dict[3])
# dict[3] = 'F'
# # After
# print(dict[3])

# # Adding data
# dict[6] = 'G'
# print(dict)

# # # empty the disctnory
# # dict = {}

# #  LOOPING THROUGH LOOOP

# for i in dict:
#     print(i) # Will print "key" itself
#     print(dict[i]) # will print "vallue"


# # ex-9.1
# student_scores = {

#     "Harry": 81,

#     "Ron": 78,

#     "Hermione": 99,

#     "Draco": 74,

#     "Neville": 62,

# }

# grade = {}

# for i in student_scores:
#     if(student_scores[i] >= 91):
#         grade[i] = "OUTSTANDING"
#     elif(student_scores[i] >= 81 and student_scores[i] <= 90):
#         grade[i] = "EXCEED EXPECTATION"
#     elif(student_scores[i] >= 71 and student_scores[i] <=80):
#         grade[i] = "ACCEPTABLE"
#     elif(student_scores[i] <= 70):
#         grade[i] = "FAIL"


# print(grade)

# # NESTING
# num = {

#     1:'one',
#     2:'two',
#     3:'three',
# }

# travel_log = {

# "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":[2,5,1]},

# "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"],"total_visits":[2,5,1]}

# }

# ex-9.2
travel_log = [
    {
        "country": "France",

        "visits": 12,

        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",

        "visits": 5,

        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(con,vis,plac):
    new_dict = {}
    new_dict["country"] = con
    new_dict["visits"] = vis
    new_dict["cities"] = plac

    return travel_log.append(new_dict)





add_new_country("Russia",2,["Mosscow","Saint Peterburg"])
print(travel_log)