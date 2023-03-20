N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
stack = []

def dfs():
        if len(stack) == M:
            print(' '.join(map(str, stack)))
            return
        flag = 0
        for i in range(N):
            if flag != num[i]:
                stack.append(num[i])
                flag = num[i]
                dfs()
                stack.pop()

dfs()