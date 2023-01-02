import sys

sys.setrecursionlimit(10 ** 6)  # 파이썬 재귀 제한
input = sys.stdin.readline


def dfs(v):
    visited[v] = 1  # 노드 방문처리
    for i in adjList[v]:  # 연결된 노드중에서
        if not visited[i]:  # 방문하지 않은 노드가 있다면 방문처리
            dfs(i)


N, M = map(int, input().split())
visited = [0 for _ in range(N + 1)]
adjList = [[] for _ in range(N + 1)]
cnt = 0

for _ in range(M):
    n1, n2 = map(int, input().split())  # 노드의 정보를 인접리스트 형태로 배치
    adjList[n1].append(n2)
    adjList[n2].append(n1)

for i in range(1, N + 1):  # 모든 노드를 순회하면서 방문, dfs 호출이 끝날때 마다 연결요소가 한개씩 추가된다.
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
