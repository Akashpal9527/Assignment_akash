# 12. Write a program to find the minimum value in the dictionary
def mini_value(d):
    mimi=100
    for i in d:
        if d.get(i)<mimi:
            mimi=d.get(i)
    return f"minimum value in the dictionary:{mimi}"
marks = {"A": 85, "B": 90, "C": 75, "D": 95}
print(mini_value(marks))