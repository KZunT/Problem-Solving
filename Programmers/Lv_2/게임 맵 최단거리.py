from collections import deque


def bfs(maps, x, y):
    queue = deque([(x, y)])  # 0,0 부터 시작
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    move_x = [-1, 1, 0, 0]  # 동서남북
    move_y = [0, 0, 1, -1]

    visited[x][y] = True  # 시작노드 방문처리

    while queue:
        x, y = queue.popleft()  # 방문할 노드 갱신

        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:  # 맵 범위내에 좌표가 있고 길이열려 있을경우
                # 범위를 주의해야 한다
                if visited[nx][ny] == False:  # 방문하지않았으면
                    queue.append((nx, ny))  # 방문할 노드에 넣기
                    visited[nx][ny] = True  # 방문처리
                    maps[nx][ny] += maps[x][y]


def solution(maps):
    bfs(maps, 0, 0)
    for m in maps:
        print(m)
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    return answer