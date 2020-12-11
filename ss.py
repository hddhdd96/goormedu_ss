# https://level.goorm.io/exam/43238/%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84/quiz/1

A = int(input())
count = 0

for i in range(2, A):
    if A % i == 0:
        count += 1

if count == 0:
    print('True')
else:
    print('False')
