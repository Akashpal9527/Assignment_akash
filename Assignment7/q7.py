# 7. Write a function to check whether a number is divisible by 5 or not.
def div_by_five(num):
    if num%5==0:
        return f"{num} is divide by 5"
    else:
        return f"{num} is not divide y 5"
print(div_by_five(int(input())))
