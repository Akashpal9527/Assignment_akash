# 7. Write a program to find the greatest key in the dictionary
def gre_key(d):
    gre=-100
    for i in d:
        if i>gre:
            gre=i
    return f"greaest key is:{gre}"


player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
print(gre_key(player))