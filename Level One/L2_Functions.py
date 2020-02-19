# basic
def greet():
    print("Hello")


greet()


# with argument kargs

def greet_argu(name):
    print("Hello " + name)


greet_argu("praveen")

# *args and **kwargs 
# with arguments /*args
# *args creats list while **kwargs creats dict
def greet_args(*names):
    for each in names:
        print("hello " + each)



greet_args("praveen", "nagaraj", "shashi")

# with **kwargs

def greet_kwargs(**names_age):
    print(names_age)
    

greet_kwargs(Praveen=21, Nagaraj=25 , Shashi = 22)

# return
def return_(r):
    return r * r


print(return_(2))


# recursive

def recur(x):
    if x == 1:
        return 1
    else:
        return x + recur(x - 1)


print(recur(4))


# using one function inside another

def another():
    greet()


another()


