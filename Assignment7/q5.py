# 5. Write a function to print all even numbers between 1 and 50.

def even_no(num1,num2):
    l=[]
    for i in range(num1,num2+1):
        if i%2==0:
            l.append(i)
    return f"all even no are:{l}"
print(even_no(1,50))