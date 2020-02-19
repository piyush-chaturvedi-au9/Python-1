"""
# Tuple
tup = ()
print(type(tup))
# creating tuple
# Method one
tup = (1, 2, 3, 4, "string", 1.2, ["list", 54])
print(tup)
# Method two
tup = tuple(input("Enter items with ',' : ").split(","))
print(tup)
# Method 3
i = 0
lst = []
while i < 5:
    tup = input("Enter items with ',' : ")
    lst.append(tup)
    i += 1
tup = tuple(lst)
print(tup)
"""
# Accessing Tuple
# 1 By accessing index location / slicing
tup = (1, 2, 3, 4, "string", 1.2, ["list", 54])
print(tup[0])
print(tup[-1])
print(tup[-1][1])
print(tup.index("string"))
print(tup[1:3])
# changing items ,it's not possible to cahnge tuple because they are immutable but we can change list inside tuple
tup[-1][1] = "changed"
print(tup)

# Deleting a tuple del

del tup
'''Traceback (most recent call last):
  File "D:/FullStack Training/Python/Tuple.py", line 37, in <module>
    print(tup)
NameError: name 'tup' is not defined'''

# Tuple Methods

# index()
tup = (1, 2, 3, 4, "string", 1.2, ["list", 54])
index_4_tup = tup.index(4)
print(index_4_tup)

# count()
tup = (1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 7, 7, 8, 9, 4, 5, 1, 7, 8, 1, 2, 3)
print(tup.count(3))
