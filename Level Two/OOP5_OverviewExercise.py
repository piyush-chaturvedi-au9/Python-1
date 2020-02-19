'''How to define a class'''
#class Dog():
#    pass
'''
Instance Attributes
All classes create objects, and all objects contain characteristics called attributes 
(referred to as properties in the opening paragraph). Use the __init__() method to initialize 
(e.g., specify) an object’s initial attributes by giving them their default value (or state). 
This method must have at least one argument as well as the self variable, 
which refers to the object itself (e.g., Dog).
'''
#class Dog():
#    def __init__(self,name,age): # Initializer / Instance Attributes
#        self.name = name
#        self.age = age

'''
Class Attributes

While instance attributes are specific to each object, 
class attributes are the same for all instances—which in this case is all dogs.
'''
#class Dog():
#    species = 'Mammal'
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
'''
Instantiating Objects
Instantiating is a fancy term for creating a new, unique instance of a class.
'''
#class Dog():
#    pass
#print(Dog()) #<__main__.Dog object at 0x00000254C662DB08>
#dog1 = Dog() #creating objects
#dog2 = Dog()
#print(dog1,"<Dog1 -- Dog2>",dog2)
#print(dog1 == dog2) # one object is not equal to other bcz each objects takes new location

'''
Let's create a class and object from we learned above
'''
"""
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age =age
    
dog1 = Dog("Bruno",2)
dog2 = Dog("Whisky",1)
print(f"Name of Dog1 : {dog1.name} and  aged : {dog1.age} \nName of Dog2 : {dog2.name} and aged : {dog2.age}")
"""

'''
Exercise:
Using the same Dog class, instantiate three new dogs, each with a different age. 
Then write a function called, get_biggest_number(), that takes any number of ages (*args) and returns the oldest one. 
Then output the age of the oldest dog like so:
'''
'''
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = Dog("Bruno",5)
dog2 = Dog("Whisky",2)
dog3 = Dog("Vodka",4)

def get_biggest_number(*args):
    if dog1.age > dog2.age and dog1.age >dog3.age:
        print(f"{dog1.name} is elder than {dog2.name} and {dog3.name}")
    if dog2.age > dog1.age and dog2.age >dog3.age:
        print(f"{dog2.name} is elder than {dog1.name} and {dog3.name}")
    if dog3.age > dog1.age and dog3.age >dog2.age:
        print(f"{dog3.name} is elder than {dog1.name} and {dog2.name}")
    

get_biggest_number(dog1,dog2,dog3)
'''
'''
Instance Methods
Instance methods are defined inside a class and are used to get the contents of an instance. 
They can also be used to perform operations with the attributes of our objects. Like the __init__ method, 
the first argument is always self:
'''
"""
class Dog():
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says Woooooof!!")

    def description(self):
        print(f"My name is {self.name} and i am {self.age} years old.")
    def get_biggest_number(self):  #instance method
        if dog1.age > dog2.age and dog1.age >dog3.age:
            print(f"{dog1.name} is elder than {dog2.name} and {dog3.name}")
        if dog2.age > dog1.age and dog2.age >dog3.age:
            print(f"{dog2.name} is elder than {dog1.name} and {dog3.name}")
        if dog3.age > dog1.age and dog3.age >dog2.age:
            print(f"{dog3.name} is elder than {dog1.name} and {dog2.name}")

dog1 = Dog("Bruno",5)
dog2 = Dog("Whisky",6)
dog3 = Dog("Vodka",4)
dog1.speak()
dog2.speak()
dog3.speak()
dog1.description()
#dog3.get_biggest_number()
"""

'''
Modifying Attributes
You can change the value of attributes based on some behavior:
'''
"""
class Email:
     def __init__(self):
         self.mailsent = False # initial attribute is false
     def send_email(self):     # once the method is called the attribute cahnges to true
         self.mailsent = True

my_email = Email()
print(my_email.mailsent)
my_email.send_email()
print(my_email.mailsent)
"""
'''
Python Object Inheritance
Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, and the classes that child classes are derived 
from are called parent classes.
It’s important to note that child classes override or extend the functionality (e.g., attributes 
and behaviors) of parent classes. In other words, child classes inherit all of the parent’s attributes 
and behaviors but can also specify different behavior to follow. The most basic type of class is an object, 
which generally all other classes inherit as their parent.
When you define a new class, Python 3 it implicitly uses object as the parent class. 
So the following two definitions are equivalent:
'''
"""
class Dog(): #base class 
    def __init__(self,name,breed,age):
        self.name = name 
        self.breed = breed
        self.age = age
    
    def description(self):
        print(f"My name is : {self.name} \nI am : {self.breed} \nI am : {self.age} years old")
    
    def speak(self,sound):
        print(f"I say {sound}")

#dog1 = Dog("Bruno","Golden Retriever",2)
#dog1.description()
#dog1.speak("Woof!") 

'''
simliar to Dog class ,cat class also will have description ,name ,speak and every features of dog
'''

class Cat(Dog):
    def colour(self,color):
        print(f"{self.name} is {color} coloured.!")


cat1 = Cat("Jessie","Persian",2)
# Now without defining anything inside cat class ,Cat class will have all the features of Dog class

cat1.description() # this method is not at all written in cat class ,but it's available because of inheritance

cat1.speak("Meow")
cat1.colour("white")
"""

'''
Super()
'''
class Book():
    def __init__(self,author,name):
        self.author = author
        self.name = name
    
    def description(self):
        print(f"{self.name}\n   --written by {self.author} ")
    def Name(self):
        print(f"The name of the {type(self).__name__}  is {self.name}")


class Magazine(Book):
    def __init__(self, author, name,publisher):
        super().__init__(author, name) # super refers to Book
        self.publisher = publisher
    def description(self):
        print(f"{self.name} by --{self.author} \nPublisher {self.publisher}")
b1 = Book("Praveen","My Life :)")
#b1.description()

m1 = Magazine("Praveen" , "Python" , "Public")
m1.description()
m1.Name()