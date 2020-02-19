"""
# set
s = {1, }
print(type(s))
# empty set is read as dictionary
s = set()
print(type(s))
# Creating set
# 1
s = {1, "String", 1.2, ("tuple", 1)}
print(s)
# set cannot have list ,dict,set inside it
# 2
i = 0
s = set()
while i < 5:
    item = input("enter the items : ")
    s.add(item)
    i += 1
print(s)

# 3
s = set(input("Enter with ',' : "))
print(s)
"""

"""
# adding items to set
# 1 add()
s = {1, "String", 1.2, ("tuple", 1)}
s.add(4)
print(s)


# changing set
s.add(5)
print(s)
s.update([2,3,4,5,6])
print(s)

# removing items from set

s.remove(5)
print(s)
s.discard(4)
print(s)
# pop will remove any one item from set as sets are not indexed pop doesn't take argument like tuple or list
s.pop()
print(s)

s.clear()
print(s)
"""


"""
# set operations
# union or |
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A|B)
print(A.union(B))

# Intersection or &
print(A.intersection(B))
print(A & B)

# Difference or -

print(A.difference(B))
print(A - B)
print(B.difference(A))

# Symmetric Difference or ^
print(A.symmetric_difference(B))
print(A ^ B)
"""
print((1, 2) + (3, 4))