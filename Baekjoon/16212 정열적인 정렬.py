N = int(input())

array = sorted(list(map(int, input().split())))

[print(num, end=' ') for num in array]