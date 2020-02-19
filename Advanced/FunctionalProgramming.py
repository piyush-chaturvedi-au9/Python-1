#pure functions
# without map add two numbers
def multiply_by_2(): # example of pure function
    ls  = list(input("enter the number with spaces ").split(" "))
    new_ls = []
    for each in ls:
        new_ls.append(int(each)*2)
    return new_ls
#print(multiply_by_2())

# map, filter, zip, reduce
# add numbers in list with map

def add_num(num,num2):
    return num + num2
#print(list(map(add_num,[1,2,3],[2,2,2])))

# multiply with map

def multiply(item):
    return item * item
 
#print(list(map(multiply,[1,2,3,4,5])))

# filter 

# find even 

def even(item):
    return item % 2 == 0

list1 = [1,2,3,4,5,6,7,8,9,10]

#print(list(filter(even,list1)))


def odd(item):
    return item % 2 != 0

#print("The old list is : ",list(filter(odd,list1)),f" of {list1}")

#zip

names = ["Praveen","Rakshi","Suman","Manu"]
id_no = [1,2,3,4]

x = (list(zip(names,id_no)))

#for each in x:
#    print(each)

#reduce
from functools import reduce 
def accum (accu,item):
    return accu + item
#print("Original List : ",list1 ,"Reduce list :  ",reduce(accum,list1))
# without reduce
sum_ = 0
#for each in list1:
 #   sum_ = each + sum_
#print(sum_)

# lambda
#print("original list :",list1,"\n Modified list :",list(map(lambda x : x**2 ,list1 )))
#print(list(filter(lambda item :item % 2 ,list1  )))

# List Comprehensions
# iterating 

#for item in "Hello":
 #   print("Without comprehension ",item)

#print([item for item in "Hello"])

'''
print("Original List : " ,list1)
print("Multiplies of two : ",list(num*2 for num in list1))
print("odd numbers in the list : ",list(num for num in list1 if num % 2 !=0))
print("even numbers in the list : ",[num for num in list1 if num % 2 == 0 ])
'''
'''
# set Comprehensions
print("Original set : " ,set(list1))
print("Multiplies of two : ",set(num*2 for num in list1))
print("odd numbers in the set : ",set(num for num in list1 if num % 2 !=0))
print("even numbers in the set : ",{num for num in list1 if num % 2 == 0 })
'''

# Dict Comprehensions
dicti = {"a":1 ,'b':2 ,'c':3}

print(dicti)
print( {k : v ** 2 for k,v in dicti.items()})

print({num : num**2 for num in list1})