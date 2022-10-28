from collections import deque

N, M, V = map(int, input().split(' '))


# 방문 리스트의 경우 함수의 외부에 선언도 가능하다.

def DFS(v, visited=[]):  # 방문한 리스트의 생성 및 초기화, 재귀호출이라 첫 함수 호출시에 초기화를 진행해야한다.
    visited.append(v)  # 노드 방문
    print(v, end=' ')  # 한줄 출력하기 위해

    for n in range(1, N + 1):  # 모든 노드 순회 , 노드 번호는 1부터 시작
        if graph[n][v] == 1 and (n not in visited):  # 노드가 연결되어 있고, 방문하지 않은 노드라면
            DFS(n, visited)  # DFS 재귀 호출 , 방문 리스트 정보도 준다.


def BFS(v):
    visited = [v]  # 방문 리스트의 선언

    queue = deque()  # 자료구조에서 값을 꺼내는 시간복잡도 측면에서 O(N) 인 리스트보다 O(1)인 덱 사용
    queue.append(v)  # 방문한 노드 큐에 삽입

    while queue:  # 덱이 비어있을때 까지 반복
        v = queue.popleft()  # 큐의 첫번째 노드를 꺼냄 , 노드가 갱신된다.
        print(v, end=' ')

        for n in range(1, N + 1):  # 모든 노드 순회 , 노드 번호는 1부터 시작
            if graph[n][v] == 1 and (n not in visited):  # 노드가 연결되어 있고, 방문하지 않은 노드라면
                visited.append(n)  # v와 이어진 노드 방문처리
                queue.append(n)  # v와 이어진 노드 큐에 삽입


graph = [[0] * (N + 1) for _ in range(N + 1)]
# 인접행렬의 생성(2차원 배열), 0인경우 노드간 연결 안되어있음 1인경우 연결 되어있음

for _ in range(N+1):
    v1, v2 = map(int, input().split(' '))  # 노드간 연결 입력
    graph[v1][v2] = graph[v2][v1] = 1  # 연결 정보 그래프에 삽입 (한 값을 여러곳에 넣기.. ㄷㄷ)

DFS(V)
print()
BFS(V)
