# 9. Write a function to count how many times a word appears in a given sentence
def count_word(sent,word):
    count=0
    l=sent.split()
    for i in l:
        if i==word:
            count+=1
    return f"{word} occures {count} times"
sent=input("Enter your sentence:")
word=input("Enter the word u wanted to  searrch:")
print(count_word(sent,word))