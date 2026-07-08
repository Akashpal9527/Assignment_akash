# 17. Write a program to create a dictionary where keys are numbers from 1 to 5 and values are their squares.
def create_dic():
    d={}
    for i  in range(1,6):
        d[i]=i*i
    return d
print(create_dic())
