N = int(input())
W = list(map(int, input().split()))

sorted_w = sorted(W)
reversed_w = sorted(W, reverse=True)

arr = []

for i in range(len(W)):
    x = sorted_w[i] + reversed_w[i]
    arr.append(x)

print(min(arr))
