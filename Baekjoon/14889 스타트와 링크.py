# from itertools import combinations
#
# N = int(input())
#
# stat = []
#
# for _ in range(N):
#     stat.append(list(map(int,input().split())))
#
# member = list(combinations(list(range(N)),N//2))
#
# score = []
#
# for m in member:
#     a_team = 0
#     b_team = 0
#     for i in range(N//2):
#         for j in range(N//2):
#             if i in m and j in m:
#                 a_team += stat[i][j]
#                 a_team += stat[j][i]
#             if i not in m and j not in m:
#                 b_team += stat[i][j]
#                 b_team += stat[j][i]
#
#     score.append(abs(a_team - b_team))
#
# print(min(score))

def dfs(depth, idx): # 백트래킹..
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)