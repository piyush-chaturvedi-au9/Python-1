# Dictionary dict()
d = {}
print(type(d))

# Creating dict
# 1
d = {"key": "Value", 1: "int", 1.2: "float", "complex": 3 + 2j, "list": ["list", 1, 2]}
print(d)

# 2
'''
d = {}
for i  in range (0,3):
    keys = (input("Enter key : "))
    values =  input(f"enter value for {keys}  : ")
    d[keys] = values
print(d)
'''

# accessing the dict
print(d.keys())
print(d.values())
print(d.get("key"))
print(d.pop(1))
print(d)

