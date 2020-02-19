# Type Conversion is the process of converting one data type into another data type
# Numbers
# 1) int to float int(float)
print(float(2))
# 3) float to int float(int)
print(int(5.1))  # Note .1 to .9 is rounded as 0
print(int(5.9))
# int to complex and float to complex
print(complex(9))  # int to complex
print(complex(2.5))  # float to complex

# complex to int is not supported


# string to int or float
print(int("2"))  # note conversion to int is not supported for real string like "Harley quine"
'''print(int("Harley"))'''

# list to tuple and VS
list_ = [1, 2, 3]
tuple_ = tuple(list_)
print("List--> ", list_, "Tuple -->", tuple_)

tuple_ = (1, 2, 3, 4)
list_ = list(tuple_)
print("Tuple --> ", tuple_, "List -->", list_)