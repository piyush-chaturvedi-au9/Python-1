# Inheritance And Polymorphism
# In object-oriented programming, inheritance is the mechanism of basing an object 
# or class upon another object or class, retaining similar implementation. 
# Also defined as deriving new classes from existing ones and forming them into a hierarchy of classes.
'''
class Animal():          #base class
    def __init__(self):
        print("I am animal")
    def eat(self):
        print("I am hungry")

class Dog(Animal):       # inherited class , this class has all the methods and functunality of Animal class
    def __init__(self):
        print("I am dog")

animal1 = Animal()
animal1.eat()
print("\n")
dog1 = Dog()
dog1.eat()



# Polymorphism -- not used in Python
'''

# Multiple Inheritance
"""
class A():
    def __init__(self,num):
        self.num = num
    def description(self):
        print(f"Class {type(self).__name__}")


class B(A):
    def __init__(self, num):
        super().__init__(num)
    def number(self):
        print(self.num)

class C(B,A):
    def __init__(self, num):
        super().__init__(num)
a = A(8)
a.description()    
b = B(2)
b.description()
b.number()    
c = C(1)
c.description()    
c.number()

"""
#mro plays major role in inheritance
# example 1
'''
class A: pass
class B(A) :pass
class C(A) :pass
class D(C,B,A): pass

d = D()
print(D.__mro__)  # D>C>B>A
<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>
'''

#example 2
class A:pass
class B:pass
class C(A, B):pass
class D(C,B):pass
obj = D()
print(D.__mro__) 
#(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# lets break 
'''
start a D bcz mro of D is called ,then it will check for its base classes which is D(C,B) 
so it will go to C class ,it will check C class which is C(B,A) then it will jump to B class 
where B is not inherited so it will check for remaining class thats A and will jumo to A
The whole algorithm is based on depth first search classD(classA,ClassB) --here classA is the dps.
'''