# 재귀알고리즘, 하노이탑 자체가 이해가 어렵다..

N = int(input())


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c) # A번째에 C번째 탑으로 바로 이동
    else:
        hanoi(n - 1, a, c, b)   # n-1 개의 원판을 A번째 기둥에서 B번째 기둥으로 모두 옮겨야 함
        print(a, c) # 그 후 가장 밑의 n 번째 원판을 C번째 기둥으로 옮긴다.
        hanoi(n - 1, b, a, c)   # 다시 n-1 개의 원판을 B번째 기둥에 C번째 기둥으로 모두 옮긴다.
        # 위의 과정 반복


count = 0

for _ in range(N):
    count = 2 * count + 1   # 하노이탑 과정 반복시 2n + 1 만큼 개수가 증가 (이해안됨)
print(count)

hanoi(N, 1, 2, 3)

# n 은 원판의 개수, 1,2,3 은 기둥의 idx
