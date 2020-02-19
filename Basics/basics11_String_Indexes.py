# string is an ordered sequence of characters
Name = "Praveen"
index_P = Name.index("P")
print(index_P)
index_r = Name.index("r")
print(index_r)
index_a = Name.index("a")
print(index_a)
index_n = Name.index("n")
print(index_n)

# slicing using indexes [start : end :step]

print(Name[0:1])  # from index 0 to 1 but not including 1
print(Name[0:2])  # from index 0 to 2 but not including 2
print(Name[0:])  # start from 0 but no end point
print(Name[::-1])  # start from end and end at start or reversing string
print(Name[0::4]) # skip four indexes
print(Name[1:4]) # start from 1 end at 4

print(Name[0:5:2])