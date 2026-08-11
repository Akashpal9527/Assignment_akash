# 14. Write a function to replace all vowels in a string with *.
def replace_vowels(str1):
    l=list(str1)
    vowels="AEIOUaeiou"
    for i in range(len(l)):
        if l[i] in vowels:
            l[i]="*"
    return "".join(l)

str1="Write a function to replace all vowels in a string with"
print(replace_vowels(str1))