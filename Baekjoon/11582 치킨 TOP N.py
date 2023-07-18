N = int(input())
chicken = list(map(int, input().split()))
K = int(input())

step = N // K
answer = []

for i in range(0, N, step):
    answer = chicken[i:i + step]
    answer.sort()
    for ele in answer:
        print(ele)
