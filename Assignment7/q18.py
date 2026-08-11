# 18. Write a function to count the number of words in a given sentence.
def count_word(str1):
    l=str1.split()
    return len(l)
str1="Write a function to count the number of words in a given sentence"
print(count_word(str1))