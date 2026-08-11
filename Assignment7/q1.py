# 1. Write a function to print your name and age.

def name_age(name,age):
    return f"Name is:{name} and Age is:{age}"
name=input("Enter your name:")
age=int(input("Enter your age:"))
print(name_age(name,age))