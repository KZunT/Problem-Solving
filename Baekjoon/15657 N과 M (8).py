N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
stack = []

def dfs(start):
        if len(stack) == M:
            print(' '.join(map(str, stack)))
            return

        for i in range(start, N):
            stack.append(num[i])
            dfs(i)
            stack.pop()

dfs(0)