import sys
from collections import Counter
N = int(input())

num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

print(round((sum(num_list)) / N))
print(num_list[N//2])

commmon = Counter(num_list).most_common(2)

if commmon[0][1] == commmon[-1][1]:
    print(commmon[-1][0])

else:
    print(commmon[0][0])

print(abs(num_list[-1] - num_list[0]))