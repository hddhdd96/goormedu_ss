A = int(input())
count = 0

for i in range(2, A):
    if A % i == 0:
        count += 1

if count == 0:
    print('True')
else:
    print('False')