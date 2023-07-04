T = int(input())

for i in range(T):
    N = int(input())

    vote = [int(input()) for j in range(N)]

    cnt = vote.count(max(vote))
    max_idx = max(vote)
    flag = max(vote) > sum(vote) / 2

    if flag == 1:
        answer = 'majority'
    else:
        answer = 'minority'
    if cnt != 1:
        print("no winner")
    else:
        print(answer, "winner", vote.index(max_idx) + 1)
