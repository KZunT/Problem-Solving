from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]  # 방문 리스트 생성
    for i in range(n):  # 모든 네트워크를 순회하며 네트워크 영역분리
        if visited[i] == False:
            bfs(n, i, computers, visited)
            answer += 1
    return answer


def bfs(n, x, computers, visited):
    queue = deque([x])

    visited[x] = True

    while queue:
        x = queue.popleft()  # 노드 갱신
        visited[x] = True  # 방문처리
        for i in range(n):
            if i != x and computers[x][i] == 1:  # 네트워크를 순회하며 자기 자신이 아니고 다른 노드와 연결되어있다면
                if visited[i] == False:  # 방문하지 않았다면
                    queue.append(i)


