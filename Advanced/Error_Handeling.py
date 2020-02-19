
while True:
    try:
        a = input("enter value for a : ") 
        print(int(a) ** 2) 
    except: 
        print("a should be number  ")   
        continue
    else: 
        print("your value : ",a) 
    finally: 
        print("Completed")
        