# 12. Write a function to check whether a string starts with a vowel.
def start_with_vowels(str1):
    vowels="AEIOUaeiou"
    if str1[0] in vowels:
        return F"Strat with vowels"
    return f"not start with vowels"
    return f"no of vowels in given strin is {count}"
str1="akash Write a function to check whether a string starts with a vowel"
print(start_with_vowels(str1))