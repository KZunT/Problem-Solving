from collections import deque

T = int(input())

for _ in range(T):
    q = deque()
    N, M = map(int, input().split())
    doc = input().split()

    for i in range(len(doc)):
        q.append((i, int(doc[i])))  # 문서순서, 중요도 순 입력

    i = 0

    while True:
        if len(q) == 0:
            break
        if q[0][1] == max(q, key=lambda x: x[1])[1]:  # 중요도가 최대인경우 출력
            i += 1
            if q[0][0] == M:
                print(i)
                break
            q.popleft()
        else:  # 더 중요한 문서가 있다면 맨뒤로 보냄
            q.append(q.popleft())
