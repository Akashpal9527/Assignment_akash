# 19. Write a program to sort a dictionary by its keys
def sort(d):
    return dict(sorted(d.items()))
d = {3: "three", 1: "one", 2: "two"}
print(sort(d))
