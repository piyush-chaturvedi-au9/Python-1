#Changing dunder methods / Creating dunder methods
'''
class SuperList():
    def __init__(self,ls):
        self.ls = ls
    
    def __get__(self):
        for each in self.ls:
            print( each )
    def __len__(self):
        print (self.ls)
    
    def __append__(self,num):
        (self.ls).append(num)
        print(self.ls)
    
    def __index__(self,n):
        print(f"{n} is at index {(self.ls).index(n)} of list {self.ls}")

s = SuperList([1,2,3,4,5,6,7])
s.__len__()
s.__append__(8)
s.__index__(5)
'''