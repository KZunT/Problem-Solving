N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
stack = []
visited = [False] * N

def dfs():
        if len(stack) == M:
            print(' '.join(map(str, stack)))
            return
        flag = 0
        for i in range(N):
            if not visited[i] and flag != num[i]:
                visited[i] = True
                stack.append(num[i])
                flag = num[i]
                dfs()
                visited[i] = False
                stack.pop()

dfs()