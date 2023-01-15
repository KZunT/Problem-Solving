def solution(arr1, arr2):
    a, b = len(arr1), len(arr1[0])  # n x m
    c, d = len(arr2), len(arr2[0])  # m x p

    answer = [[0] * d for _ in range(a)]  # 결과는 n x p
    array = [[0] * d] * a  # 이게 왜 안될까?
    print(array == answer)

    for i in range(a):
        for j in range(d):
            for k in range(c):
                answer[i][j] += arr1[i][k] * arr2[k][j]  # [n][p] = arr1[n][m] * arr2[m][p]

    return answer
