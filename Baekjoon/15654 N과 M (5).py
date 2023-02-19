N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
stack = []
visited = [False] * N

def dfs():
        if len(stack) == M:
            print(' '.join(map(str, stack)))
            return

        for i in range(N):
            if not visited[i]:
                stack.append(num[i])
                visited[i] = True
                dfs()
                visited[i] = False
                stack.pop()

dfs()