"""
Part 1:
# Object Oriented Programming
# class is the blueprint that defines the nature the future object
# objects are the instances of class
# we use keyword class to create class
class Sample():         # class is created using keyword class with classname Sample >Note classname is always singular
    pass                # pass is skip the logic or code 

s1 = Sample()           # object s1 is created using class Sample 
print(s1)               # object will be stored at some location say <__main__.Sample object at 0x000001BAB9045948>


# Above class doesn't have anything , so let's create a new class with attributes or a class that does something
# let's create a class Dog which holds breed and some other info about dog

class Dog():              # Create a class Named Dog
    '''def __init__(self):''' # self is used to refer itself, __init__ is the special magic method 
                        # or dunder method we use to instantiate
        # Above class doesn't have any attributes ,so lets go back and some attributes to our __init__
    def __init__(self,breed,origin): # we added breed and origin attributes to our class Dog
        self.Breed = breed
        self.Origin = origin

breed = input("Enter the breed of the dog : ")
origin= input("Enter the origin of the dog : ")
dog1 = Dog(breed,origin)
print(dog1.Breed)
"""

"""
Part 2 : 

# create a class with name Employee()

# instantiate the class with name,age,salary,designation attributes 
        





        
# create a object named employee1 and pass the arguments

# print the employee details by formatting

"""

"""
part 3
Object Attributes and Methods
"""
'''
# 3.1
class Dog():

    # class object attribute
    # same for all instance of a class
    # self is not used here
    species = 'mammal'  # this is like pre-defined attribute which can be called after creating object of the class 

    def __init__(self,breed,origin):
        self.Breed = breed
        self.Origin= origin

dog1 = Dog("Husky","Siberia")

print(dog1.species)   # we have not assigned this in our init but this is applicable to all objects .
'''
class Dog():

    # class object attribute
    # same for all instance of a class
    # self is not used here
    species = 'mammal'  # this is like pre-defined attribute which can be called after creating object of the class 

    def __init__(self,breed,origin):
        self.Breed = breed
        self.Origin= origin
    
    # now we have created attributes which we use by .Breed to call that attribute
    # what if i want to call both the attribute together as method 

    def doggie(self):   # creating method
        print(f"The breed of the dog is {self.Breed} and Origin of the dog is {self.Origin}")

dog1 = Dog("Husky","Siberia") # creating objects

# who do we call the method
# unlike attribute where we use to call using dog1.breed here we use  dog1.doggie() method > Note while calling method use () 
dog1.doggie()  # method is called



























'''
solution for part 2
class Employee:
    def __init__(self,name,age,salary,designation): # initialization or constructor
        self.Name = name
        self.Age = age
        self.Salary = salary
        self.Designation = designation  
Employee1 = Employee("Praveen",21,45000,"Developer") # creating object names Employee1 
Employee1 = (f" Name : {Employee1.Name} \n Age : {Employee1.Age} \n Salary : {Employee1.Salary} \n Designation : {Employee1.Designation}")
print(Employee1)

'''