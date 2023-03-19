# import sys
#
# T = int(sys.stdin.readline())
#
# for i in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#
#     for j in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#
#     print(N - 1) # 모든국가가 연결되어 있기 때문에 가능한 방법

import sys
from collections import deque

def bfs(x):
    # 들려야 할 정점 저장
    queue = deque([x])

    # 현재 노드 방문 처리
    visited[x] = 1
    cnt = 0

    # 큐가 없을때까지 반복
    while queue:

        # 큐에서 하나의 원소를 팝
        queue.popleft()

        # 모든 국가가 연결되어 있으므로 모든 국가 확인
        for i in range(1, N + 1):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    graph = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    # 방문 여부 파악
    visited = [0] * (N + 1)

    print(bfs(1))