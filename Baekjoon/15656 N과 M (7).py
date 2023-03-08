N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
stack = []

def dfs():
        if len(stack) == M:
            print(' '.join(map(str, stack)))
            return

        for i in range(N):
            stack.append(num[i])
            dfs()
            stack.pop()

dfs()