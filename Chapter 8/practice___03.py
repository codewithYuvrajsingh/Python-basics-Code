def sum(c):
    if c== 1:
     return 1 
    else:
       return sum(c-1)+c
print(sum(3))