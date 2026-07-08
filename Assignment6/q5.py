# 5. Write a program to calculate the total score of all students
def total_score(d):
    score=0
    for i in d:
        score+=d.get(i)
    return score
student_score = {1: 44, 2: 45, 3: 55}
print(total_score(student_score))