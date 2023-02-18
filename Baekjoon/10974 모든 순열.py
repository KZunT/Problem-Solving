N = int(input())

stack = []

def dfs():
        if len(stack) == N:
            print(' '.join(map(str, stack)))
            return

        for i in range(1,N+1):
            if i not in stack:
                stack.append(i)
                dfs()
                stack.pop()

dfs()