try :  
    a = int(input("inter a number"))
    b = int(input("inter a number")) 
    print(f"The division is {a/b}")
except ZeroDivisionError as z :
    print("infinite")