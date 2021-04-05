#1
# for loop
# fruits = ['a','b','c']

# for i in fruits:
#     print(i)
#     print(i + " pie")

#2 ex-5.1
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# sum =0
# for height in student_heights:
#     sum += height
# avg = sum/len(student_heights)

# print(round(avg))

#3 ex-5.2
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# # student_scores = input("Input a list of student scores ").split()
# # for n in range(0, len(student_scores)):
# #   student_scores[n] = int(student_scores[n])
# # print(student_scores)
# print(max(student_scores))

#4 range().
# sum = 0
# for i in range(2,101,2):
#     print(i)
#     sum += i
# print(sum)

#5 FizzBuzz
for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i% 3 ==0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    # else:
    #     print(i)
