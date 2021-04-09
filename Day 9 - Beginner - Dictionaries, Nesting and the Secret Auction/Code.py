#1 Day9
dict = {1:'A',2:'B',3:'C',4:'D',5:'E'}
print(dict[1])
print(dict[2])
#  UPDATING DATA
# Before
print(dict[3])
dict[3] = 'F'
# After
print(dict[3])

# Adding data
dict[6] = 'G'
print(dict)

# # empty the disctnory
# dict = {}

#  LOOPING THROUGH LOOOP

for i in dict:
    print(i) # Will print "key" itself
    print(dict[i]) # will print "vallue"
