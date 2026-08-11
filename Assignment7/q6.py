# 6. Write a function that takes a number and prints its multiplication table.

def multi(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
print(multi(int(input())))