# 3. Write a function that takes a number and prints whether it is positive, negative, or zero.
def num_po_ne_zero(num):
    if num>0:
        return f"{num} is positive"
    elif num==0:
        return f"{num} is Zero"
    else:
        return f"{num} is Negetive"
print(num_po_ne_zero(int(input())))
