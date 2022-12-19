from collections import deque

def bfs():
    q = deque()
    q.append(N)  # 큐에 시작 지점 삽입

    while q:
        x = q.popleft()
        if x == K:  # 만약 목적지에 도착하면
            print(dist[x])  # 소요된 count 를 출력
            break

        for i in (x - 1, x + 1, x * 2):  # 3가지의 방법을 모두 경유
            if 0 <= i <= MAX and not dist[i]:  # 해당구간에 도착하지 아직 않았고, 유효 범위내에 숫자가 있을경우
                dist[i] = dist[x] + 1  # count 갱신
                q.append(i)


MAX = 100000  # 문제에서 주어진 최대 범위 수
N, K = map(int, input().split())
dist = [0] * (MAX + 1)

bfs()
