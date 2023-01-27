# from collections import deque

# def solution(order):
#     Q = deque()
#     for i in range(1,len(order)+1):
#         Q.append(i)

#     st = deque()
#     cnt = 0

#     while Q:
#         if order[cnt] != Q[0]:
#             if st and order[cnt] == st[-1]:
#                 cnt += 1
#                 st.pop()
#             else:
#                 st.append(Q.popleft())
#         else:
#             cnt += 1
#             Q.popleft()

#     while st:
#         if order[cnt] == st[-1]:
#             cnt += 1
#             st.pop()
#         else:
#             break

#     return cnt

def solution(order):
    answer = 0
    stacks = []
    N = len(order)
    i = 1
    idx = 0
    while i < N+1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
        i += 1


    return idx