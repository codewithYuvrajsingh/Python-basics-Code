n = int(input("enter a number:"))
for i in range(2,n ):
    if n%i == 0:
        print("i is not a prime number")
        break
else:
     print("i is a prime number ")

