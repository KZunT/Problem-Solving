import sys
from math import gcd
input = sys.stdin.readline
N = int(input())

pre_tree = int(input())

tree_list = []

for _ in range(N-1):
    pos = int(input())  # 가로수 위치
    tree_list.append(pos - pre_tree)  # 가로수 사이 간격 저장
    pre_tree = pos

distance = tree_list[0]

for idx in range(1, N-1):  # 가로수 사이 최대 공약수 구하기
    distance = gcd(distance, tree_list[idx])

cnt = 0

for tree in tree_list:  # 얼마나 나무를 심어야하는지 세기
    cnt += tree // distance - 1

print(cnt)
