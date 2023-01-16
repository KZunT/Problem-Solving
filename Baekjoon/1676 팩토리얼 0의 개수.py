import math

N = int(input())

for i, num in enumerate(reversed(str(math.factorial(N)))):
    if num != '0':
        print(i)
        break
