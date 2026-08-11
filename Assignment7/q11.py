# 11. Write a function to count the number of vowels in a given string.
def vowels_count(str1):
    vowels="AEIOUaeiou"
    count=0
    for i  in str1:
        if i in vowels:
            count+=1
    return f"no of vowels in given strin is {count}"
str1="Write a function to count the number of vowels in a given string"
print(vowels_count(str1))