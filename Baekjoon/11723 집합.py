# 파이참 환경에서 오류??

import sys

N = int(input())

S = set()  # 공집합 S


def add(x):
    S.add(x)


def remove(x):
    S.discard(x)


def check(x):
    if x in S:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in S:
        S.discard(x)
    else:
        S.add(x)


def all():
    global S
    S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}


def empty():
    global S
    S = set()


for i in range(N):

    order = sys.stdin.readline().split()
    if order[0] == 'add':
        add(int(order[1]))
    if order[0] == 'remove':
        remove(int(order[1]))
    if order[0] == 'check':
        check(int(order[1]))
    if order[0] == 'toggle':
        toggle(int(order[1]))
    if order[0] == 'all':
        all()
    if order[0] == 'empty':
        empty()
