N = int(input())

paper = sorted(list(map(int, input().split())))

for i in range(N, -1, -1):
    if i <= paper[-i]:
        print(i)
        break
