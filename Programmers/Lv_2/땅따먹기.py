def solution(land):
    answer = 0

    for i in range(1,len(land)): # i = 행 인덱스
        for j in range(len(land[i])):   # j = 열 인덱스
            land[i][j] += max(land[i -1][: j] + land[i - 1][j + 1:])
    #print(land)

    return max(land[-1])