import sys

input = sys.stdin.readline

K, L = map(int, input().split())

student = {}

for i in range(L):
    student[input().rstrip()] = i

result = sorted(student.items(), key=lambda x: x[1])

if (K > len(result)):
    K = len(result)

for i in range(K):
    print(result[i][0])
