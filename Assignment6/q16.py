# 16. Write a program to count the frequency of each character in a string using a dictionary. Example: "banana"
def freq(word):
    d={}
    for i in word:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
print(freq("banana"))