def inches_to_cm(inches):
    if inches == 1:
        return 2.54
    else:
        return inches * 2.54
inches = int(input("enter inches :"))
print(f"{inches}is eqaul to  {inches_to_cm(inches)}")