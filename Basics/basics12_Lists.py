print("Creating lists")
"""
# create lists
li = [1, "string", 8.2, ["nested list"], {"set"}, ("tuple"), {"key": "value"}]
print(li)
# taking input as list
# 1 method
li = list(input("enter the list with spaces : ").split(" "))
print(li)
# 1.1
li = list(input("enter the list with ',' after each item : ").split(","))

print(li)

# method 2 using loops
n = int(input("Enter no of items : "))
ls=[]
for i in range(0,n):
    i = input("Enter the items anf hit enter: \n ")
    ls.append(i)
print(ls)

"""

print("Accessing lists")
"""
# Accessing the list

li = ["hello", 8, 8.5, ("tuple", 8)]
# slicing
print(type(li[-1]))
# positive slicing for 2nd item
print(li[1])

# negative slicing/indexing for last 2nd item
print(li[-2])

# accessing all items in list

print(li[0:])

# knowing data types of each item
for each in li:
    print(type(each))

# Altering items / Changing items
print(f"before alter {li[0:]}")
li[0] = "changed"
print(f"after alter {li[0:]}")

# deleting or removing
# using pop()
print(f"before delete {li}")
li.pop()
print(f"after delete {li}")

# using pop(x) with index
print(f"before delete with index  {li}")
li.pop(0)
print(f"after delete with 0 {li}")

# using del keyword

print(f"before delete with del  {li}")
del li
li = []  # because li gets deleted
print(f"after delete with del  {li}")

# using del with index
li = [1, "string", 8.2, ["nested list"], {"set"}, ("tuple", 8), {"key": "value"}]

print(f"before delete with del index  {li}")
del li[0]
print(f"after delete with del  index 0 {li}")

# using clear

print(f"before delete clear  {li}")
li.clear()
print(f"after delete with del  index 0 {li}")
"""
print("List methods")

# index()
print("Indexing")
li = [1, "string", 8.2, ["nested list"], {"set"}, ("tuple", 8), {"key": "value"}]
print(f"prints the index position 'string' {li.index('string')}")
print(f"prints the index position  'key : value' {li.index({'key': 'value'})}")

# returning value from index

index_ = li.index(8.2)
print(index_)
# changing item with index position acquired
li[index_] = "new item"
print(li)

# append()
print("Append list")
li = []
li.append(9)
print(li)
# adding another list using append
li2 = [1, "string", 8.2, ["nested list"]]
li.append(li2)
print(li)

# extend()
language = ['French', 'English', 'German']
language1 = ['Spanish', 'Portuguese']
language.extend(language1)
print('Language List: ', language)

# append and extend does same function


# insert()
# insert methods require two argument one position and another element
li = [0, 1, 2, 3]
li.insert(4, 4)
print(li)
li.insert(3, "Three")
print(li)

# remove()
# takes only one argument
li = [1, 2, 3, 4, 5, 6]
li.remove(3)
print(li)

# count
# takes only one argument
li = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(li.count(4))
print(li.count(3))
print(li.count(2))
print(li.count(1))

# pop() already done in delete

print("pop")

# reverse()
print("Reverse")
li = [1, 2, 3, 4, 5, 6]
print(f"before reverse {li}")
li.reverse()
print(f"after reverse {li}")
li = [1, 2, 3, 4, 5, 6]
# reversing each
for each in reversed(li):
    print(each)

# sort()
print("Sorting")
# ascending
li = [2, 7, 5, 1, 0, 6, 8, 9, 4, 1, 5, 8, 7, 1, 2, 6, 4, 8, 2, 1, 3, 6]
print("Before sort", li)
li.sort()
print("After sort", li)

# descending
li = [2, 7, 5, 1, 0, 6, 8, 9, 4, 1, 5, 8, 7, 1, 2, 6, 4, 8, 2, 1, 3, 6]
print("Before sort", li)
li.sort(reverse=True)
print("After sort", li)

# sort takes two arguments key and reverse
li = [2, 7, 5, 1, 0, 6, 8, 9, 4, 1, 5, 8, 7, 1, 2, 6, 4, 8, 2, 1, 3, 6]
print("Before sort", li)
li.sort(reverse=True)
print("After sort", li)


# key
def takeSecond(elem):
    return elem[1]


# function takes 2nd element in tuple
li = [(1, 2), (1, 6), (1, 4), (1, 9), (1, 8)]
print("Before sort", li)
li.sort(key=takeSecond)
print("After sort", li)


# copy
print("Copy")
li = [1, 2, 3, 4, 5, 6]
li2 = li
print("method 1 li2 = li1 ", li2)
li2.append(7)
print(li)
print(li2)
# this is like both the list will be same if change li or li2 to change only the new list we use copy()

li = [1, 2, 3, 4, 5, 6]
li2 = li.copy()
print("method 2 copy()", li2)
li2.append(7)
print(li)
print(li2)
# only li2 is affected

# List comprehension
# [expression for loop]
pow2 = [x**2 for x in range(0, 10)]
print(pow2)
