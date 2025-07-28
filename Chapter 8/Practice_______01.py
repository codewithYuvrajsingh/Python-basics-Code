def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a = int(input("enter your number a :" ))
b = int(input("enter your number b :" ))
c = int(input("enter your number c :" ))
print(greatest(a, b, c))
