
'''
# create a class named cat :
class cat:
    # add a attribulte species = mammal 
    species = 'Mammal'
    # instantiate the class / add constructor with name and age 
    def __init__(self,name,age):
        self.Name = name 
        self.Age = age

# instantiate the cat object with three cats
cat1 = cat("Spooky",2)
cat2 = cat("whisky",3)
cat3 = cat("vodka",4)

# print names of all cats
print(f"{cat1.Name}\n{cat2.Name}\n{cat3.Name}")

# create a function that finds the oldest cat 
def find_old_cat(*args):
    return max(args)

print(find_old_cat(cat1.Age,cat2.Age,cat3.Age)) 
'''


'''
Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. 
In other words, the Dog class does not inherit from the Pets class. Then assign three dog instances to 
an instance of the Pets class. 
Start with the following code below. Save the file as pets_class.py. Your output should look like this:


I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course.
'''
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"


class Pets(Dog):
    number = int(input("Enter number of dogs : "))
    def __init__(self, name, age):
        super().__init__(name, age)

    #def number_of_dogs(self,number):       
     #   self.number = number
      #  if self.number > 0 :
       #     return f"I have {self.number} Dogs."
    
    def names_of_dogs(self):
        names = []
        for each in range(1,self.number+1):
            name = input(f"enter the name of Dog {each} : ")
            names.append(name)
        return names
        #for i in names:
        #    print(f"Name of dog {names.index(i)+1} is {i}  ")
    def age_of_dogs(self):
        age = []
        for each in range(1,self.number+1):
            ag = input(f"enter the Age of Dog {each} : ")
            age.append(ag)
        return age
    def description(self):
        
        names1 = self.names_of_dogs()
        ages1 =self.age_of_dogs()
        print (f"{list(zip(names1,ages1))}")


pet1 = Pets("Bruno",5) 
#num = int(input ('enter no of dogs in number  : ')) 
#print(pet1.number_of_dogs(num))
pet1.description()
